# Paso 3 · Tradúcelo a mensajes con JTBD

## Para qué sirve

Para convertir la investigación en palabras que vas a usar. Jobs to be Done (JTBD, "el trabajo que el cliente contrata a tu producto para hacer") separa lo que el cliente quiere lograr, cómo quiere sentirse y cómo quiere que lo vean. En este paso la IA trabaja como analista del comportamiento del consumidor y como psicóloga del comportamiento: además de tu investigación, revisa qué dice tu segmento cuando nadie le está vendiendo (foros, Reddit, reseñas, comentarios) y lo contrasta.

## Qué necesitas

- `mi-marca/01_cliente.md` (perfil de cliente).
- `mi-marca/02_fuerzas.md` (Forces Canvas y frases de entrevistas).
- Tus datos de ventas, si los tienes.
- Una IA que pueda buscar en internet. Si la tuya no puede, busca tú en foros, Reddit, reseñas de Google y comentarios de redes, y pega lo que encuentres con su liga.

Agente: `agentes/03_analista_comportamiento.md`.

## El prompt

```
Eres un analista en comportamiento del consumidor y un psicólogo del comportamiento. Vas a analizar a este segmento: [perfil del paso 1].

Esto es lo que ya investigamos: [Forces Canvas, entrevistas, datos de ventas]

Antes de concluir, investiga en línea qué dice este segmento cuando nadie le está vendiendo: foros, Reddit, comentarios en redes, reseñas y grupos. Contrasta lo que encuentres con nuestra investigación y dime en qué coincide, en qué no y qué se nos estaba escapando. Cita de dónde sale cada hallazgo.

Después ayúdame a diseñar:
1. Los Jobs to be Done de mi cliente: funcional (qué quiere lograr), emocional (cómo quiere sentirse) y social (cómo quiere que lo vean).
2. Los 5 motivadores de compra más fuertes.
3. Los 5 dolores y las 5 fricciones más fuertes.
4. Un mapa de mensajes: qué le tengo que decir en cada etapa (no me conoce, me está evaluando, está a punto de comprar, ya compró) para irlo avanzando en el proceso de venta.
5. Las palabras exactas que usa mi cliente y las que debo evitar.
```

## Qué debe salir

`mi-marca/03_mensajes.md`, con la plantilla `plantillas/mapa_mensajes.md`:

- Contraste entre tu investigación y lo que dice el segmento en línea, con fuentes citadas.
- Jobs to be Done: funcional, emocional y social.
- 5 motivadores, 5 dolores y 5 fricciones.
- Mapa de mensajes por etapa.
- Lista de palabras que usa tu cliente y palabras que debes evitar.

## Checklist para pasar al paso 4

- [ ] Cada hallazgo de foros o reseñas tiene su fuente (liga o lugar concreto).
- [ ] Sé en qué coincide y en qué no lo que dicen en línea con mis entrevistas.
- [ ] Tengo los tres Jobs to be Done escritos en palabras del cliente, no en jerga de marketing.
- [ ] El mapa de mensajes tiene al menos un mensaje para cada una de las cuatro etapas.
- [ ] Los mensajes atacan la ansiedad y la inercia del paso 2.
- [ ] Tengo mi lista de palabras que sí y palabras que no.

## El ejemplo real: clínica TAND

Las frases de las 50 entrevistas se volvieron el diccionario de los mensajes. A "Siempre me cambian lo que me dijeron que costaba" se le responde con claridad de precio desde el primer contacto; a "Mientras no sea grave, mejor me aguanto", explicando por qué esperar sale más caro. Las palabras de ellas, no las de la clínica.
