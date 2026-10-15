"""Descarga métricas y videos de cuentas de TikTok o Instagram con Apify.

Uso:
    python herramientas/apify_descargar.py --red tiktok --cuentas cuenta1 cuenta2 --limite 5
    python herramientas/apify_descargar.py --red instagram --cuentas cuenta3 --limite 10

Guarda:
    datos/metricas_<red>_<cuenta>.json   métricas de cada video
    datos/videos/<cuenta>/<id>.mp4       los videos

Necesita APIFY_TOKEN en herramientas/.env (o en .env en la raíz del repo).
Nunca imprime el token.
"""
import argparse
import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos"

# Busca las llaves primero en herramientas/.env y luego en la raíz del repo.
load_dotenv(RAIZ / "herramientas" / ".env")
load_dotenv(RAIZ / ".env")

# Actores de Apify (la ~ separa usuario y nombre del actor en la API).
ACTORES = {
    "tiktok": "clockworks~tiktok-scraper",
    "instagram": "apify~instagram-scraper",
}


def ocultar(texto, token):
    """Quita el token de cualquier texto antes de imprimirlo, por si acaso."""
    return texto.replace(token, "***") if token else texto


def correr_actor(red, cuenta, limite, token):
    """Corre el actor en modo síncrono y regresa la lista de publicaciones."""
    if red == "tiktok":
        entrada = {
            "profiles": [cuenta],
            "resultsPerPage": limite,
            "shouldDownloadVideos": True,
            "shouldDownloadCovers": False,
        }
    else:
        entrada = {
            "directUrls": [f"https://www.instagram.com/{cuenta}/"],
            "resultsType": "posts",
            "resultsLimit": limite,
        }
    url = f"https://api.apify.com/v2/acts/{ACTORES[red]}/run-sync-get-dataset-items"
    # El token va como parámetro; Apify corta las corridas síncronas a los 300 s.
    r = requests.post(url, params={"token": token, "timeout": 280}, json=entrada, timeout=320)
    if r.status_code >= 300:
        print(f"  Error HTTP {r.status_code}: {ocultar(r.text[:300], token)}")
        return []
    return r.json()


def url_del_video(item):
    """Busca la URL del mp4 en los campos que existan, según el actor."""
    if item.get("videoUrl"):
        return item["videoUrl"]
    medios = item.get("mediaUrls") or []
    if medios:
        return medios[0]
    meta = item.get("videoMeta") or {}
    return meta.get("downloadAddr")


def normalizar(red, cuenta, item):
    """Deja las métricas de TikTok e Instagram con los mismos nombres de campo."""
    if red == "tiktok":
        return {
            "id": str(item.get("id", "")),
            "cuenta": cuenta,
            "red": red,
            "url": item.get("webVideoUrl"),
            "texto": item.get("text"),
            "fecha": item.get("createTimeISO"),
            "vistas": item.get("playCount"),
            "likes": item.get("diggCount"),
            "comentarios": item.get("commentCount"),
            "compartidos": item.get("shareCount"),
            "guardados": item.get("collectCount"),
            "duracion_s": (item.get("videoMeta") or {}).get("duration"),
        }
    return {
        "id": str(item.get("id") or item.get("shortCode", "")),
        "cuenta": cuenta,
        "red": red,
        "url": item.get("url"),
        "texto": item.get("caption"),
        "fecha": item.get("timestamp"),
        "vistas": item.get("videoPlayCount") or item.get("videoViewCount"),
        "likes": item.get("likesCount"),
        "comentarios": item.get("commentsCount"),
        "compartidos": None,
        "guardados": None,
        "duracion_s": item.get("videoDuration"),
    }


def bajar_video(url, destino, token):
    """Descarga el mp4 por partes. Si ya existe, no lo vuelve a bajar."""
    if destino.exists() and destino.stat().st_size > 0:
        return True
    # Los videos guardados por Apify viven en su almacenamiento y pueden pedir token.
    params = {"token": token} if "api.apify.com" in url else None
    try:
        with requests.get(url, params=params, stream=True, timeout=120,
                          headers={"User-Agent": "Mozilla/5.0"}) as r:
            if r.status_code >= 300:
                return False
            with open(destino, "wb") as f:
                for parte in r.iter_content(chunk_size=1 << 20):
                    f.write(parte)
        return True
    except requests.RequestException:
        return False


def main():
    p = argparse.ArgumentParser(description="Descarga videos y métricas con Apify.")
    p.add_argument("--red", choices=["tiktok", "instagram"], required=True)
    p.add_argument("--cuentas", nargs="+", required=True, help="usuarios sin @")
    p.add_argument("--limite", type=int, default=10, help="videos por cuenta")
    args = p.parse_args()

    token = os.getenv("APIFY_TOKEN", "").strip()
    if not token:
        sys.exit("Falta APIFY_TOKEN en herramientas/.env (revisa INSTALAR.md).")

    for cuenta in args.cuentas:
        cuenta = cuenta.lstrip("@").strip()
        print(f"[{args.red}] {cuenta}: pidiendo hasta {args.limite} publicaciones a Apify...")
        items = correr_actor(args.red, cuenta, args.limite, token)

        carpeta = DATOS / "videos" / cuenta
        carpeta.mkdir(parents=True, exist_ok=True)
        metricas = []
        for item in items:
            fila = normalizar(args.red, cuenta, item)
            url = url_del_video(item)
            if not url or not fila["id"]:
                continue  # fotos o carruseles sin video
            destino = carpeta / f"{fila['id']}.mp4"
            if bajar_video(url, destino, token):
                fila["archivo"] = str(destino.relative_to(RAIZ)).replace("\\", "/")
            else:
                fila["archivo"] = None
                print(f"  No se pudo bajar el video {fila['id']}")
            metricas.append(fila)

        salida = DATOS / f"metricas_{args.red}_{cuenta}.json"
        salida.write_text(json.dumps(metricas, ensure_ascii=False, indent=1), encoding="utf-8")
        bajados = sum(1 for m in metricas if m.get("archivo"))
        print(f"  {len(items)} publicaciones, {bajados} videos guardados en {carpeta}")


if __name__ == "__main__":
    main()
