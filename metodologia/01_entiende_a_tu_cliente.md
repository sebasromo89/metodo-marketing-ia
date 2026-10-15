# Paso 1 · Entiende a tu cliente

## Para qué sirve

Para dejar de hablarle a "todo el mundo". Antes de pensar en contenido, necesitas saber quién compra, quién paga más y quién vuelve. Casi siempre hay un segmento que vale mucho más de lo que pesa en número, y ese es el que buscas.

## Qué necesitas

- Nombre de tu marca, qué vende y precio aproximado.
- Dónde vende: ciudad, país y canal (tienda, en línea, a empresas).
- **Si ya tienes clientes:** tu base de ventas o de clientes exportada a Excel o CSV, **sin nombres, teléfonos ni correos**. Idealmente con producto, monto, fecha, edad, género, zona y cómo llegó cada cliente.
- **Si no tienes clientes:** solo tu conocimiento del producto y del mercado.

Agente: `agentes/01a_investigador_mercado.md` (sin datos) o `agentes/01b_analista_datos_clientes.md` (con datos).

## El prompt

### Prompt 1A · Si todavía no tienes clientes o datos

```
Eres un investigador de oportunidades de mercado y especialista en psicología del consumidor.

Mi marca: [nombre y qué vende]
Precio aproximado: [rango de precio]
Dónde vendo: [ciudad, país, canal: tienda, en línea, a empresas]

Detecta quién es el cliente principal de este producto. Antes de responder, hazme las preguntas que necesites.

Después entrégame:
1. Los 3 segmentos de cliente más probables, ordenados por potencial.
2. Para cada uno: edad, género, nivel socioeconómico, ocupación, qué le preocupa y en qué momento de su vida compra esto.
3. Cuál de los 3 me recomiendas atacar primero y por qué.
4. Qué datos tendría que conseguir para confirmar que no me estoy equivocando.
```

### Prompt 1B · Si ya tienes clientes

Exporta tus ventas o tu base de clientes a Excel o CSV (sin nombres, teléfonos ni correos) y adjúntala.

```
Eres un analista de marketing y negocio. Te comparto la base de clientes del negocio al que quiero ayudar a hacer mejor marketing: [giro, ciudad].

Analiza:
1. Qué productos o servicios se venden más.
2. Cuáles convierten más (cotizado contra comprado).
3. Cuáles cuesta menos trabajo cerrar.
4. Ticket promedio por producto y por tipo de cliente.
5. Qué perfil de cliente (edad, género, zona, cómo llegó) compra más, paga más y vuelve más.

Entrégame una tabla con los hallazgos y, al final, una sola conclusión: cuál es mi cliente clave y con qué producto debo hablarle primero. Si algún dato no alcanza para concluir algo, dímelo en lugar de suponer.
```

## Qué debe salir

`mi-marca/01_cliente.md`, con la plantilla `plantillas/perfil_cliente.md`:

- Los segmentos detectados y, si hay datos, la tabla de hallazgos (ventas, conversión, ticket promedio, recompra).
- **Un solo cliente clave** y el producto con el que conviene hablarle primero.
- Qué datos faltan para confirmar la conclusión.

## Checklist para pasar al paso 2

- [ ] Hay un cliente clave elegido, descrito con edad, género, situación de vida y qué le preocupa.
- [ ] Sé por qué es ese y no otro (con datos o, si no tengo, con una hipótesis explícita).
- [ ] Sé con qué producto o servicio le hablo primero.
- [ ] Los datos que usé no tienen nombres, teléfonos ni correos.
- [ ] Anoté qué datos me faltan y cómo los voy a conseguir.

## El ejemplo real: clínica TAND

Analizamos 2,947 pacientes. Las mujeres de 35 años en adelante eran el 19% de los pacientes, pero el 29% del ingreso, con 77% de conversión y un ticket promedio de $7,638. Ese fue nuestro cliente clave: no el más numeroso, el más valioso.
