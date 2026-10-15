"""Analiza con Gemini cada video descargado por apify_descargar.py.

Uso:
    python herramientas/gemini_analizar_videos.py
    python herramientas/gemini_analizar_videos.py --limite 5     # solo los primeros 5 pendientes

Lee datos/metricas_*.json, sube cada mp4 con la Files API de Gemini, espera a
que esté ACTIVE y pide un análisis en JSON. Guarda una línea por video en
datos/analisis.jsonl. Si se corta, vuelve a correrlo: se salta lo ya analizado.

Necesita GEMINI_API_KEY en herramientas/.env. Modelo configurable con GEMINI_MODEL.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos"
SALIDA = DATOS / "analisis.jsonl"

load_dotenv(RAIZ / "herramientas" / ".env")
load_dotenv(RAIZ / ".env")

MODELO = os.getenv("GEMINI_MODEL", "").strip() or "gemini-3.5-flash"
RESPALDO = "gemini-3.8-flash"

PROMPT = """Analiza este video. Responde SOLO con un objeto JSON con estas claves:
"gancho": gancho de los primeros 3 segundos (texto exacto y qué se ve),
"formato": a cámara, podcast, animación, tutorial, testimonio, tendencia u otro,
"tema": tema del video,
"dolor": dolor o deseo del cliente al que le habla,
"estructura": gancho, desarrollo, cierre y llamada a la acción, en una o dos frases,
"por_que_funciono": por qué crees que funcionó o no funcionó, comparando sus vistas con el promedio de la cuenta,
"transcripcion": lo que se dice en el video, resumido si es largo.

Datos del video: cuenta {cuenta}, {vistas} vistas; promedio de la cuenta: {promedio} vistas.
Texto de la publicación: {texto}
Responde en español."""


def cargar_videos():
    """Junta los videos de todos los archivos de métricas y calcula el promedio por cuenta."""
    videos = []
    for archivo in sorted(DATOS.glob("metricas_*.json")):
        filas = json.loads(archivo.read_text(encoding="utf-8"))
        vistas = [f["vistas"] for f in filas if isinstance(f.get("vistas"), (int, float))]
        promedio = round(sum(vistas) / len(vistas)) if vistas else None
        for f in filas:
            if f.get("archivo"):
                f["promedio_cuenta"] = promedio
                videos.append(f)
    return videos


def ya_analizados():
    """Regresa los archivos que ya están en el archivo SALIDA, para poder reanudar."""
    hechos = set()
    if SALIDA.exists():
        for linea in SALIDA.read_text(encoding="utf-8").splitlines():
            try:
                hechos.add(json.loads(linea)["archivo"])
            except (json.JSONDecodeError, KeyError):
                pass
    return hechos


def subir_y_esperar(cliente, ruta):
    """Sube el video y espera a que Gemini lo termine de procesar."""
    archivo = cliente.files.upload(file=str(ruta))
    while archivo.state.name == "PROCESSING":
        time.sleep(3)
        archivo = cliente.files.get(name=archivo.name)
    if archivo.state.name != "ACTIVE":
        raise RuntimeError(f"El archivo quedó en estado {archivo.state.name}")
    return archivo


def pedir_analisis(cliente, modelo, archivo, video):
    prompt = PROMPT.format(
        cuenta=video["cuenta"],
        vistas=video.get("vistas"),
        promedio=video.get("promedio_cuenta"),
        texto=(video.get("texto") or "")[:500],
    )
    respuesta = cliente.models.generate_content(
        model=modelo,
        contents=[archivo, prompt],
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    return json.loads(respuesta.text)


def main():
    p = argparse.ArgumentParser(description="Analiza videos con Gemini.")
    p.add_argument("--limite", type=int, default=0, help="máximo de videos a analizar en esta corrida")
    args = p.parse_args()

    llave = os.getenv("GEMINI_API_KEY", "").strip()
    if not llave:
        sys.exit("Falta GEMINI_API_KEY en herramientas/.env (revisa INSTALAR.md).")

    cliente = genai.Client(api_key=llave)
    hechos = ya_analizados()
    pendientes = [v for v in cargar_videos() if v["archivo"] not in hechos]
    if args.limite:
        pendientes = pendientes[: args.limite]
    print(f"Videos por analizar: {len(pendientes)} (ya analizados: {len(hechos)}). Modelo: {MODELO}")

    modelo = MODELO
    for i, video in enumerate(pendientes, 1):
        ruta = RAIZ / video["archivo"]
        print(f"[{i}/{len(pendientes)}] {video['archivo']}")
        try:
            archivo = subir_y_esperar(cliente, ruta)
            try:
                analisis = pedir_analisis(cliente, modelo, archivo, video)
            except Exception as e:
                # Si el modelo no existe o no está disponible, probamos el de respaldo.
                if modelo != RESPALDO and ("404" in str(e) or "not found" in str(e).lower()):
                    print(f"  El modelo {modelo} no respondió; cambio a {RESPALDO}")
                    modelo = RESPALDO
                    analisis = pedir_analisis(cliente, modelo, archivo, video)
                elif "429" in str(e):
                    print("  Límite de uso alcanzado; espero 60 segundos y reintento.")
                    time.sleep(60)
                    analisis = pedir_analisis(cliente, modelo, archivo, video)
                else:
                    raise
            cliente.files.delete(name=archivo.name)  # no dejamos videos en la nube
        except Exception as e:
            print(f"  Falló este video, sigo con el siguiente: {str(e)[:200]}")
            continue

        fila = {k: video.get(k) for k in ("archivo", "cuenta", "red", "url", "vistas", "promedio_cuenta", "fecha")}
        fila["modelo"] = modelo
        fila["analisis"] = analisis
        with open(SALIDA, "a", encoding="utf-8") as f:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print(f"Listo. Resultados en {SALIDA}")


if __name__ == "__main__":
    main()
