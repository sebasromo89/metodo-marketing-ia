# No fue suerte, fue por diseño · El método, listo para usar con tu IA

Repositorio de trabajo de la conferencia-taller **"No fue suerte, fue por diseño"** de Sebastián Romo, en el **Anáhuac Business Summit 2026** (Vision Hub, Universidad Anáhuac Querétaro).

Micrositio de la conferencia: https://visionhub.com.mx/business-summit/ia-marketing/

## Qué es esto

Es el método que usamos para que el marketing de una marca deje de depender de la suerte, convertido en un repositorio que tu IA puede leer. Le das este repo a tu IA (Claude Code, Codex, Cursor, Gemini CLI, o ChatGPT y Claude en el navegador) y ella te lleva paso a paso, con **tu** marca, por los 6 pasos del método. Al final tienes en la carpeta `mi-marca/` seis documentos: quién es tu cliente, qué lo mueve, qué decirle, dónde vive, qué estrategia seguir y cómo producir el contenido.

No es un curso para leer: es un taller para hacer. La IA no te va a dar respuestas mágicas; te va a hacer preguntas, te va a pedir datos y va a investigar contigo.

## El método en 6 pasos

| Paso | Qué haces | Qué te llevas |
|---|---|---|
| 1. Entiende a tu cliente | Detectas quién compra, quién paga más y quién vuelve | `mi-marca/01_cliente.md` |
| 2. Escúchalo con Forces Canvas | Entrevistas a clientes reales y ordenas qué los empuja y qué los frena | `mi-marca/02_fuerzas.md` |
| 3. Tradúcelo a mensajes con JTBD | Conviertes la investigación en Jobs to be Done y un mapa de mensajes | `mi-marca/03_mensajes.md` |
| 4. Encuentra dónde vive y qué consume | Investigas cuentas, creadores, competidores y (opcional) auditas sus videos con Apify y Gemini | `mi-marca/04_ecosistema.md` |
| 5. Consejo de expertos decide la estrategia | Cinco referentes del marketing proponen, critican y votan estrategias | `mi-marca/05_estrategia.md` |
| 6. Produce con método | Estilo, storyboard, guion, imágenes, voz y animación, en ese orden | `mi-marca/06_produccion.md` |

El detalle de cada paso está en `metodologia/`.

## Cómo usarlo: 3 modos

### Modo A · Con una IA que tiene terminal (Claude Code, Codex, Cursor, Gemini CLI)

Es el modo más completo, porque la IA puede guardar tus entregables y correr las herramientas de video.

1. Clona o descarga este repositorio:
   ```
   git clone https://github.com/sebasromo89/metodo-marketing-ia.git
   cd metodo-marketing-ia
   ```
2. Abre tu IA dentro de esa carpeta.
3. Escríbele: **"Lee AGENTS.md y guíame."**

La IA te va a preguntar por tu marca y te va a llevar paso por paso. Cada entregable se guarda en `mi-marca/`.

### Modo B · Con una IA en el navegador (ChatGPT, Claude, Gemini)

1. Pega la liga de este repositorio en el chat.
2. Escríbele: **"Lee el archivo AGENTS.md de este repositorio y guíame paso a paso con mi marca, haciéndome preguntas."**
3. Como la IA web no puede guardar archivos en tu computadora, al cerrar cada paso pídele: "Dame el entregable completo en Markdown para guardarlo como `mi-marca/01_cliente.md`" y guárdalo tú.

En este modo no puedes correr la auditoría de videos (paso 4C), pero sí todo lo demás.

### Modo C · A mano

Abre `metodologia/01_entiende_a_tu_cliente.md`, copia el prompt, cambia lo que está entre corchetes por los datos de tu marca y pégalo en tu IA favorita. Llena la plantilla correspondiente de `plantillas/` con lo que salga y pasa al siguiente paso.

## Qué hay en cada carpeta

```
metodo-marketing-ia/
├── AGENTS.md            Instrucciones para la IA que te guía
├── CLAUDE.md, GEMINI.md Remiten a AGENTS.md
├── INSTALAR.md          Cómo instalar Apify, Gemini y Python (paso 4C)
├── metodologia/         Los 6 pasos: para qué, prompt, entregable, checklist, ejemplo
├── agentes/             Un agente por tarea, con su prompt de sistema
├── .claude/agents/      Los mismos agentes como subagentes de Claude Code
├── plantillas/          Formatos para llenar cada entregable
├── herramientas/        Scripts de Apify y Gemini para auditar videos
├── mi-marca/            Aquí se guarda tu trabajo
└── datos/               Videos y métricas descargadas (no se suben a git)
```

## Las reglas que no se negocian

1. Primero el cliente, después el contenido.
2. Pídele a la IA el camino, no el resultado.
3. La primera respuesta es un borrador: corrígela, pídele que se critique, pídele tres opciones.
4. Datos de clientes: sin nombres, teléfonos ni correos.
5. Verifica cifras, nombres de cuentas y datos antes de publicar.
6. Mide clientes, no vistas.

## El caso que inspiró el método

En la clínica dental TAND analizamos 2,947 pacientes y descubrimos que las mujeres de 35 años en adelante eran el 19% de los pacientes pero el 29% del ingreso. Las escuchamos, auditamos 40 cuentas y 224 videos con Apify y Gemini, y de ahí salió la estrategia: un podcast, "Ahora Hablemos". Tres clips pasaron de 100,000 vistas en TikTok y el 20% de los pacientes nuevos de ese mes llegaron por esos videos. No fue suerte, fue por diseño.

## Licencia

MIT. Úsalo, adáptalo y compártelo. Ver `LICENSE`.
