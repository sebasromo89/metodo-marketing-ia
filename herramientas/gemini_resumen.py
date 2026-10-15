"""Junta todos los análisis de video y pide a Gemini el resumen de la auditoría.

Uso:
    python herramientas/gemini_resumen.py

Lee datos/analisis.jsonl y escribe mi-marca/04_auditoria_videos.md con:
formatos ganadores, los 10 ganchos más repetidos en los videos con más vistas,
temas saturados y huecos.
"""
import json
import os
import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
from google import genai

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "datos" / "analisis.jsonl"
SALIDA = RAIZ / "mi-marca" / "04_auditoria_videos.md"

load_dotenv(RAIZ / "herramientas" / ".env")
load_dotenv(RAIZ / ".env")

MODELO = os.getenv("GEMINI_MODEL", "").strip() or "gemini-3.5-flash"
RESPALDO = "gemini-3.8-flash"

PROMPT = """Con el análisis de estos {n} videos de las cuentas que consume mi cliente, dime:
1. Los formatos de video, de anuncio y de reel que más funcionan para esta audiencia.
2. Los 10 ganchos que más se repiten en los videos que más vistas tienen.
3. Los temas que ya están saturados y los que nadie trabaja.

Cada video trae sus vistas y el promedio de vistas de su cuenta: un video funcionó si
superó el promedio de SU cuenta, no por su número absoluto. Cita ejemplos (cuenta y
gancho) para cada conclusión y di sobre cuántos videos se basa. Responde en español
de México, en Markdown, con títulos ## para cada una de las 3 secciones.

Análisis:
{datos}"""


def main():
    llave = os.getenv("GEMINI_API_KEY", "").strip()
    if not llave:
        sys.exit("Falta GEMINI_API_KEY en herramientas/.env (revisa INSTALAR.md).")
    if not ENTRADA.exists():
        sys.exit("No existe datos/analisis.jsonl. Corre antes gemini_analizar_videos.py.")

    filas = [json.loads(l) for l in ENTRADA.read_text(encoding="utf-8").splitlines() if l.strip()]
    # Ordenamos por qué tanto superó cada video el promedio de su cuenta.
    for f in filas:
        prom = f.get("promedio_cuenta") or 0
        f["veces_promedio"] = round((f.get("vistas") or 0) / prom, 2) if prom else None
    filas.sort(key=lambda f: f["veces_promedio"] or 0, reverse=True)

    # Mandamos solo lo necesario para no gastar de más.
    compacto = [
        {
            "cuenta": f["cuenta"],
            "vistas": f.get("vistas"),
            "veces_promedio": f["veces_promedio"],
            **{k: f["analisis"].get(k) for k in ("gancho", "formato", "tema", "dolor", "estructura")},
        }
        for f in filas
        if isinstance(f.get("analisis"), dict)
    ]
    prompt = PROMPT.format(n=len(compacto), datos=json.dumps(compacto, ensure_ascii=False))

    cliente = genai.Client(api_key=llave)
    try:
        texto = cliente.models.generate_content(model=MODELO, contents=prompt).text
    except Exception as e:
        if "404" in str(e) or "not found" in str(e).lower():
            print(f"El modelo {MODELO} no respondió; uso {RESPALDO}")
            texto = cliente.models.generate_content(model=RESPALDO, contents=prompt).text
        else:
            raise

    cuentas = sorted({f["cuenta"] for f in filas})
    encabezado = (
        "# Auditoría de videos (paso 4C)\n\n"
        f"Fecha: {date.today().isoformat()} · Videos analizados: {len(compacto)} · "
        f"Cuentas: {', '.join(cuentas)}\n\n"
        "Generado con Apify + Gemini. Revisa y verifica antes de usarlo en la estrategia.\n\n"
    )
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(encabezado + texto.strip() + "\n", encoding="utf-8")
    print(f"Listo: {SALIDA}")


if __name__ == "__main__":
    main()
