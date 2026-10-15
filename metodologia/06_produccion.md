# Paso 6 · Produce con método

## Para qué sirve

El video no se "promptea": se diseña. Pedirle a una IA "hazme un video" da algo genérico. Lo que funciona es producir en orden, como lo haría un equipo de producción, y que cada decisión salga de tu investigación: el gancho sale de los ganchos que funcionan (paso 4), las palabras salen de tu cliente (paso 3) y el tema sale de la estrategia (paso 5).

## Qué necesitas

- `mi-marca/03_mensajes.md` (palabras exactas del cliente).
- `mi-marca/04_ecosistema.md` y, si existe, `04_auditoria_videos.md` (formatos y ganchos).
- `mi-marca/05_estrategia.md` (pilares, formato y las 10 ideas).
- La descripción de tu marca: colores, tipografía, tono.
- Una de las 10 ideas elegida para producir primero.

Agente: `agentes/06_director_produccion.md`.

## Los prompts, en orden

1. **Estilo visual y ritmo.**
   ```
   Con mi marca [descripción, colores, tono] y esta audiencia [perfil], propón 3 estilos visuales y de ritmo para mis videos, con referencias.
   ```
2. **Storyboard.**
   ```
   Con el estilo elegido, haz el storyboard toma por toma de este video: qué se ve, qué se dice, cuánto dura cada toma.
   ```
3. **Guion.**
   ```
   Escribe el guion con el gancho en los primeros 3 segundos, usando las palabras exactas de mi cliente: [pega del paso 3].
   ```
4. **Imágenes y personaje.** Se generan cuadro por cuadro con el mismo personaje y el mismo estilo. Pide a la IA una "ficha de personaje" (rasgos, ropa, luz, encuadre) y úsala en cada imagen para que no cambie de un cuadro a otro.
5. **Voz.** Tu voz o una voz con IA (por ejemplo, ElevenLabs). El audio es de lo más importante: un buen video con mal audio se pierde.
6. **Animación y edición.** Animación (por ejemplo, Omni Flash), video con personajes realistas (por ejemplo, Higgsfield) y subtítulos.

## Qué debe salir

`mi-marca/06_produccion.md`, con la plantilla `plantillas/storyboard.md`:

- Los 3 estilos propuestos y el elegido.
- Storyboard toma por toma (qué se ve, qué se dice, duración).
- Guion con gancho en los primeros 3 segundos.
- Ficha de personaje y lista de imágenes por cuadro.
- Decisión de voz y de herramienta de animación y edición.
- Cómo vas a saber si ese video trajo clientes.

## Checklist para cerrar el método

- [ ] El gancho de los primeros 3 segundos usa palabras reales de mi cliente.
- [ ] El video ataca un dolor, fricción o motivador concreto de la investigación.
- [ ] Hay texto en pantalla desde el inicio y subtítulos.
- [ ] El audio es claro (lo probé con audífonos y con la bocina del teléfono).
- [ ] Verifiqué cifras, nombres y datos antes de publicar.
- [ ] Tengo cómo medir clientes, no solo vistas (por ejemplo, preguntar "¿cómo nos conociste?").

## El ejemplo real: clínica TAND

Del podcast "Ahora Hablemos" salieron clips de 371,600, 157,100 y 103,400 vistas en TikTok. Lo que importa: el 20% de los pacientes nuevos de ese mes llegaron por esos videos. No fue suerte, fue por diseño.
