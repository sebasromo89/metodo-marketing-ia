# Instalar Apify y Gemini para auditar videos (paso 4C)

Esta guía es solo para el paso 4C, que es opcional. Con ella vas a poder descargar los videos de las cuentas que consume tu cliente y analizarlos con inteligencia artificial. Tiempo aproximado la primera vez: 30 a 60 minutos.

Si tu IA tiene terminal (Claude Code, Codex, Cursor, Gemini CLI), puede ayudarte con cada paso. Las llaves, eso sí, las pegas tú en el archivo `.env`: nunca en el chat.

## Cuánto cuesta (aproximado)

- **Apify:** el plan gratuito incluye créditos mensuales (alrededor de 5 dólares al mes al momento de escribir esto). Con eso alcanza para probar y para varias decenas de cuentas con pocos videos cada una. Descargar videos gasta más que solo bajar métricas. Revisa tu consumo en la consola de Apify.
- **Gemini:** la API tiene un nivel gratuito con límites de solicitudes por minuto y por día. Para unos cuantos cientos de videos cortos suele alcanzar si vas con calma; si te topas con el límite, el script espera y reintenta, y puedes reanudar al día siguiente.
- Los precios y límites cambian: revisa las páginas de precios de Apify y de Google AI Studio antes de una corrida grande.

## Paso 1 · Cuenta de Apify y token

1. Entra a https://apify.com y crea una cuenta gratuita.
2. Ve a **Settings > API & Integrations**.
3. Copia tu **Personal API token**. No lo pegues en ningún chat: lo vas a poner en el archivo `.env` en el paso 4.

## Paso 2 · API key de Gemini

1. Entra a https://aistudio.google.com con tu cuenta de Google.
2. Haz clic en **Get API key** y luego en **Create API key**.
3. Copia la llave. Igual que el token de Apify: va solo en `.env`.

## Paso 3 · Python y dependencias

Necesitas Python 3.10 o superior.

### Windows

1. Abre la terminal (PowerShell) y escribe `python --version`.
2. Si no aparece una versión, instala Python desde https://www.python.org/downloads/ y, en el instalador, marca la casilla **Add Python to PATH**. Cierra y vuelve a abrir la terminal.
3. Entra a la carpeta del repositorio e instala las dependencias:
   ```
   cd ruta\a\metodo-marketing-ia
   python -m pip install -r herramientas\requirements.txt
   ```

### Mac

1. Abre la Terminal y escribe `python3 --version`.
2. Si no tienes Python 3.10 o superior, instálalo desde https://www.python.org/downloads/ (o con Homebrew: `brew install python`).
3. Entra a la carpeta e instala las dependencias:
   ```
   cd ruta/a/metodo-marketing-ia
   python3 -m pip install -r herramientas/requirements.txt
   ```

En Mac usa `python3` en lugar de `python` en todos los comandos de esta guía.

Opcional pero recomendado: crea un entorno virtual antes de instalar (`python -m venv .venv` y luego `.venv\Scripts\activate` en Windows o `source .venv/bin/activate` en Mac).

## Paso 4 · Pon tus llaves en `.env`

1. Copia el archivo de ejemplo:
   - Windows: `copy herramientas\.env.example herramientas\.env`
   - Mac: `cp herramientas/.env.example herramientas/.env`
2. Abre `herramientas/.env` con tu editor (Bloc de notas, VS Code, TextEdit en modo texto) y pega tus llaves después del signo `=`, sin comillas ni espacios:
   ```
   APIFY_TOKEN=tu_token_aquí
   GEMINI_API_KEY=tu_llave_aquí
   ```
3. Guarda el archivo.

Reglas de seguridad:
- `.env` ya está en `.gitignore`: no se sube a git. No lo quites de ahí.
- Nunca pegues tus llaves en un chat con una IA, en un correo ni en una captura de pantalla.
- Si una llave se filtró, revócala en Apify o en Google AI Studio y crea una nueva.

## Paso 5 · Prueba con 1 cuenta y 5 videos

Antes de correr 40 cuentas, prueba con una sola cuenta pública de TikTok o Instagram:

```
python herramientas/apify_descargar.py --red tiktok --cuentas nombre_de_cuenta --limite 5
python herramientas/gemini_analizar_videos.py
python herramientas/gemini_resumen.py
```

Si todo salió bien vas a tener:
- `datos/metricas_tiktok_nombre_de_cuenta.json` con las métricas.
- `datos/videos/nombre_de_cuenta/` con 5 videos mp4 (o menos, si la cuenta tiene fotos).
- `datos/analisis.jsonl` con un análisis por video.
- `mi-marca/04_auditoria_videos.md` con el resumen.

Abre el resumen y revisa que tenga sentido. Después corre la lista completa (de 10 a 30 videos por cuenta suele ser suficiente):

```
python herramientas/apify_descargar.py --red tiktok --cuentas cuenta1 cuenta2 cuenta3 --limite 20
python herramientas/apify_descargar.py --red instagram --cuentas cuenta4 cuenta5 --limite 20
python herramientas/gemini_analizar_videos.py
python herramientas/gemini_resumen.py
```

Si el análisis se corta, vuelve a correr `gemini_analizar_videos.py`: se salta lo que ya analizó.

Los videos ocupan espacio en disco (de 2 a 10 MB cada uno). Cuando termines la auditoría puedes borrar `datos/videos/`; el análisis queda en `datos/analisis.jsonl` y en `mi-marca/`.

## Errores comunes

| Mensaje | Qué pasa | Qué hacer |
|---|---|---|
| `python no se reconoce como comando` | Python no está instalado o no está en el PATH | Reinstala marcando "Add Python to PATH" y abre una terminal nueva. En Mac usa `python3`. |
| `ModuleNotFoundError: No module named 'dotenv'` (o `requests`, `google`) | Faltan las dependencias | Corre de nuevo `python -m pip install -r herramientas/requirements.txt`. |
| `Falta APIFY_TOKEN` o `Falta GEMINI_API_KEY` | El script no encontró la llave | Revisa que el archivo se llame exactamente `herramientas/.env` (no `.env.txt`) y que la llave esté después del `=`. En Windows, activa "Extensiones de nombre de archivo" en el Explorador para ver la extensión real. |
| `Error HTTP 401` en Apify | Token incorrecto o revocado | Copia de nuevo el token desde Settings > API & Integrations. |
| `Error HTTP 402` en Apify | Se acabaron los créditos del mes | Espera al siguiente mes, reduce `--limite` o revisa tu plan. |
| `Error HTTP 408` o la corrida tarda mucho | La corrida síncrona pasó de 5 minutos | Usa menos videos por cuenta (`--limite 10`) o menos cuentas por comando. |
| `0 publicaciones` | La cuenta es privada, no existe o el nombre está mal | Verifica el usuario exacto, sin `@`. Solo funcionan cuentas públicas. |
| `No se pudo bajar el video` | El enlace del video caducó o la publicación es una foto | Vuelve a correr la descarga de esa cuenta; las fotos se ignoran. |
| `429` o `RESOURCE_EXHAUSTED` en Gemini | Pasaste el límite del nivel gratuito | El script espera y reintenta; si sigue, continúa más tarde. Se reanuda solo. |
| `404` o `not found` con el modelo | El nombre del modelo cambió | El script prueba el modelo de respaldo. También puedes poner otro en `.env` con `GEMINI_MODEL=`. Revisa los modelos disponibles en Google AI Studio. |
| `El archivo quedó en estado FAILED` | Gemini no pudo procesar ese video | Se salta y sigue con el siguiente. Si pasa con todos, revisa que los mp4 se abran en tu computadora. |
