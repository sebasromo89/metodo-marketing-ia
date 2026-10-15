# Paso 4 · Encuentra dónde vive y qué consume

## Para qué sirve

Ya sabes quién es tu cliente y qué decirle. Ahora necesitas saber dónde está: qué cuentas sigue, en quién confía, qué marcas admira, qué busca, qué formatos consume y quién compite por su atención. Y, si te animas, ver con datos qué videos le funcionan a esas cuentas y por qué.

Tiene tres partes:
- **4A.** El ecosistema digital de tu cliente.
- **4B.** Tus competidores bien posicionados, incluidos los indirectos y los sustitutos.
- **4C (opcional).** Auditoría de videos con Apify y Gemini.

## Qué necesitas

- `mi-marca/01_cliente.md` y `mi-marca/03_mensajes.md`.
- Una IA que pueda buscar en internet (para 4A y 4B).
- Para 4C: cuenta de Apify, API key de Gemini y Python. Todo está en `INSTALAR.md`.

Agentes: `agentes/04_investigador_ecosistema.md` (4A y 4B) y `agentes/04c_auditor_videos.md` (4C).

## Los prompts

### Prompt 4A · El ecosistema de tu cliente

```
Eres un investigador de comportamiento digital. Basado en este perfil de cliente: [pega el perfil y los Jobs to be Done]

Investiga y detecta:
1. Qué cuentas de Instagram, TikTok y YouTube consume.
2. Qué creadores e influencers sigue y confía.
3. Qué marcas compra y admira (de mi industria y de otras).
4. Qué busca en Google y qué le pregunta a ChatGPT sobre este tema.
5. Qué formatos consume más (reels, carruseles, podcast, video largo, lives).

Dame nombres concretos de cuentas en [país o ciudad] y dime cómo verificaste cada una.
```

### Prompt 4B · Tus competidores bien posicionados

```
Investiga quiénes son los competidores mejor posicionados para [producto] en [ciudad o país], incluidos los indirectos y los sustitutos (lo que compra mi cliente en lugar de lo mío).

Para cada uno: qué promete, a quién le habla, qué contenido publica, qué tipo de anuncios corre, qué le funciona y qué le reclaman sus clientes en reseñas y comentarios.

Al final dime qué tema o formato nadie está ocupando.
```

### Paso 4C · Audita el contenido que ya consume tu cliente (Apify + Gemini)

Con Apify bajas los perfiles y los videos de las cuentas que salieron en 4A y 4B; con Gemini, que puede ver video, cada video se analiza. Los scripts de `herramientas/` hacen todo; las instrucciones de instalación están en `INSTALAR.md`.

El prompt para cada video (ya viene dentro de `herramientas/gemini_analizar_videos.py`):

```
Analiza este video. Dime:
1. Gancho de los primeros 3 segundos (texto exacto y qué se ve).
2. Formato (a cámara, podcast, animación, tutorial, testimonio, tendencia).
3. Tema y dolor del cliente al que le habla.
4. Estructura (gancho, desarrollo, cierre, llamada a la acción).
5. Por qué crees que funcionó o no funcionó, comparando sus vistas con el promedio de la cuenta.
```

Y para juntarlos todos (ya viene dentro de `herramientas/gemini_resumen.py`):

```
Con el análisis de estos [número] videos de las cuentas que consume mi cliente, dime:
1. Los formatos de video, de anuncio y de reel que más funcionan para esta audiencia.
2. Los 10 ganchos que más se repiten en los videos que más vistas tienen.
3. Los temas que ya están saturados y los que nadie trabaja.
```

Los comandos, en orden:

```
python herramientas/apify_descargar.py --red tiktok --cuentas cuenta1 cuenta2 --limite 20
python herramientas/apify_descargar.py --red instagram --cuentas cuenta3 --limite 20
python herramientas/gemini_analizar_videos.py
python herramientas/gemini_resumen.py
```

## Qué debe salir

`mi-marca/04_ecosistema.md`, con la plantilla `plantillas/ecosistema.md`:

- Cuentas, creadores y marcas que consume tu cliente, cada una con cómo se verificó.
- Qué busca y qué pregunta.
- Formatos que más consume.
- Competidores (directos, indirectos y sustitutos) y qué tema o formato nadie ocupa.
- Si hiciste 4C: `mi-marca/04_auditoria_videos.md` con formatos ganadores, 10 ganchos, temas saturados y huecos, y su resumen dentro de `04_ecosistema.md`.

## Checklist para pasar al paso 5

- [ ] Tengo al menos 10 cuentas concretas y verifiqué que existen.
- [ ] Tengo al menos 3 competidores, incluido uno indirecto o sustituto.
- [ ] Sé qué les reclaman a los competidores en reseñas y comentarios.
- [ ] Identifiqué al menos un tema o formato que nadie está ocupando.
- [ ] Si hice 4C: probé primero con 1 cuenta y 5 videos, y el resumen está en `mi-marca/04_auditoria_videos.md`.
- [ ] Ninguna llave de API quedó en el chat ni en un archivo que no sea `.env`.

## El ejemplo real: clínica TAND

Con Apify y Gemini auditamos 40 cuentas que consume nuestra clienta y 224 videos propios. El hallazgo: lo que más funcionaba conectaba la salud de la boca con la salud del cuerpo, ponía texto en pantalla desde el segundo 0 y era una conversación a dos voces.
