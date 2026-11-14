# Registro de prompts — Gestor de tareas

Registro obligatorio de toda instrucción relevante dada al asistente de
IA durante esta actividad (cubre las Tareas 2 y 4 del enunciado:
"Documentar las conversaciones clave con el asistente" y
"Documentación del proceso y análisis crítico de la experiencia").
Cada entrada: qué se pidió, qué se generó/decidió, y cómo se verificó.

---

## Entrada 1 — Prompt de arranque del proyecto

**Prompt literal** (resumen; el prompt completo definía contexto,
restricción de no-código-manual, stack propuesto, funcionalidad mínima
y el método de trabajo en 8 puntos — ver conversación original):

> "Vamos a construir, desde cero, en esta carpeta vacía, un GESTOR DE
> TAREAS con persistencia en base de datos local. Stack: Python, Flask
> + Jinja2, SQLite [...] Primer paso ahora: redacta
> `docs/definicion_proyecto.md` [...] y detente ahí a esperar mi
> confirmación."

**Resultado generado**:
- Carpeta del proyecto creada: `actividad1_gestor_tareas/`.
- `docs/definicion_proyecto.md` — descripción funcional, objetivo,
  6 requisitos mínimos, enfoque técnico (Flask + Jinja2 + `sqlite3`
  sin ORM, con justificación explícita) y sección "Fuera de alcance"
  para no ampliar sin acordarlo explícitamente.
- Este mismo archivo (`docs/registro_prompts.md`), creado para dejar
  constancia desde la primera interacción.

**Decisión técnica tomada y por qué**: `sqlite3` de la librería
estándar en vez de SQLAlchemy — una sola entidad (`tarea`) con CRUD
simple no justifica la capa de abstracción de un ORM ni una
dependencia adicional. Documentado también en `definicion_proyecto.md`
para que quede trazado junto a la decisión funcional.

**Cómo se verificó**: pendiente — este primer paso es solo
documentación; no hay código que ejecutar todavía. La verificación
corresponde al usuario: leer `definicion_proyecto.md` y confirmar o
pedir cambios antes de que se proponga el plan de incrementos (paso 2
del prompt de arranque).

**Cómo reproducirlo**: pegar el prompt de arranque completo (guardado
también en el histórico de la conversación de planificación) en una
sesión nueva de un asistente de IA con acceso a esta carpeta vacía.

---

## Entrada 2 — Confirmación de la definición y petición de plan de incrementos

**Prompt literal**:

> "confirmo, sigamos con la practica (acuerdate de ir documentando y
> dime en cada paso que debo hacer)"

**Resultado generado**: plan de 5 incrementos pequeños y verificables
(ver sección "Plan de incrementos" más abajo en este documento),
siguiendo el paso 2 del prompt de arranque. No se ha escrito código
todavía — a la espera de confirmación del plan completo antes de
implementar el Incremento 1.

**Cómo se verificó**: no aplica (es un paso de planificación, sin
artefacto ejecutable).

**Cómo reproducirlo**: tras tener `docs/definicion_proyecto.md`
confirmado, pedir "propón el plan de incrementos" equivalente al punto
2 del prompt de arranque.

## Plan de incrementos

1. **Estructura del proyecto + modelo de datos**: esqueleto Flask
   mínimo, conexión a SQLite, creación automática de la tabla
   `tareas` si no existe. Una única ruta de comprobación (página de
   inicio que confirma que el servidor arranca y la base de datos
   está accesible, aunque todavía sin listar tareas reales).
2. **Crear y listar tareas**: formulario de alta (título +
   descripción opcional) y página principal que lista todas las
   tareas guardadas en SQLite.
3. **Marcar como completada/pendiente y editar**: alternar el estado
   de una tarea existente; formulario de edición de título/descripción.
4. **Eliminar tarea**: acción de borrado permanente con confirmación
   previa (pantalla o diálogo de "¿seguro?").
5. **Pulir interfaz y documentación de ejecución**: estilos mínimos
   (legibilidad, distinguir visualmente completadas/pendientes),
   mensajes de confirmación de las acciones, `requirements.txt` y
   `README.md` con instrucciones reales y probadas para ejecutar la
   app en local.

---

## Entrada 3 — Confirmación del plan, Incremento 1 implementado

**Prompt literal**:

> "confirmo, acuerdate de ir documentando y todo ok?"

**Resultado generado — Incremento 1 (estructura + modelo de datos)**:
- `database.py` — conexión SQLite (`tareas.db`, creada junto al
  proyecto) y `inicializar_bd()`, que crea la tabla `tareas`
  (`id`, `titulo`, `descripcion`, `completada`) solo si no existe
  todavía.
- `app.py` — aplicación Flask mínima; llama a `inicializar_bd()` al
  arrancar y expone una única ruta `/` de comprobación.
- `templates/index.html` — página que confirma la conexión a la base
  de datos mostrando cuántas tareas hay guardadas (0 por ahora).
- `.venv/` — entorno virtual Python 3.12 creado en el propio proyecto,
  con Flask 3.1.3 instalado.
- `requirements.txt` — `Flask==3.1.3`.

**Cómo se verificó**: se ejecutó la app con el cliente de pruebas de
Flask (sin levantar un servidor real) contra una base de datos nueva:
la petición a `/` devolvió código 200 y el texto "Tareas guardadas
actualmente: 0"; se inspeccionó `tareas.db` y el esquema de la tabla
creada coincide exactamente con el diseñado.

**Cómo reproducirlo**: desde la carpeta del proyecto, con el entorno
virtual activado, ejecutar `python app.py` y abrir
`http://127.0.0.1:5000/` en el navegador — debe mostrar el mensaje de
comprobación con 0 tareas guardadas (o el número real si ya existía
`tareas.db` de una ejecución anterior).

---

## Entrada 4 — Confirmación del Incremento 1 con evidencia

**Prompt literal**:

> "Revisado y aceptado, funciona correctamente. Capturas añadidas."

**Resultado generado**: confirmación verificada por el propio usuario
(terminal de Flask arrancando y navegador mostrando la página de
comprobación con el mensaje del Incremento 1). Las dos capturas
estaban guardadas por error en la carpeta del proyecto antiguo
archivado (`actividad1/capturas/`, el Termómetro de Centro) en vez de
en la de este proyecto — se movieron a
`actividad1_gestor_tareas/capturas/`, renombradas de forma descriptiva
(`incremento1-terminal.png`, `incremento1-navegador.png`), y se borró
la carpeta `capturas/` que había quedado vacía en `actividad1/`.

**Cómo se verificó**: se abrieron ambas imágenes para confirmar que
correspondían efectivamente a este proyecto (el prompt de la terminal
muestra la ruta `actividad1_gestor_tareas`, y la página en el
navegador muestra el texto exacto del Incremento 1).

**Cómo reproducirlo**: no aplica — es una corrección de ubicación de
archivos, no un paso de desarrollo.

---

## Entrada 5 — Incremento 2: crear y listar tareas

**Contexto**: continuación directa del plan de incrementos aprobado en
la Entrada 2 (no hubo un prompt nuevo del usuario para este paso
concreto; se ejecutó tras la confirmación de la Entrada 4).

**Resultado generado**:
- `database.py` — `obtener_tareas()` (lista todas las tareas por
  `id`) y `crear_tarea(titulo, descripcion)`. Se retiró
  `contar_tareas()` del Incremento 1 por quedar sin uso (la página de
  comprobación queda sustituida por el listado real).
- `app.py` — ruta `/` ahora lista las tareas reales; ruta nueva
  `/tareas/nueva` (GET muestra el formulario, POST valida que el
  título no esté vacío y, si es válido, inserta la tarea y redirige
  al listado; si el título falta, reaparece el formulario con un
  mensaje de error).
- `templates/index.html` — listado de tareas con título, descripción
  (si existe) y estado (Pendiente/Completada); mensaje "No hay tareas
  todavía" cuando está vacío.
- `templates/nueva_tarea.html` — formulario de alta nuevo.

**Decisión técnica tomada y por qué**: la validación del título
obligatorio se hace en el propio backend (Flask), no solo con el
atributo `required` del HTML — así la regla se cumple aunque el
formulario se manipule o el JavaScript del navegador esté
desactivado.

**Cómo se verificó**: pruebas automáticas con el cliente de test de
Flask contra una base de datos limpia: (1) listado vacío muestra el
mensaje correcto; (2) enviar el formulario sin título no crea ninguna
tarea y muestra el error; (3) enviar el formulario con título y
descripción válidos crea exactamente una tarea y aparece en el
listado como "Pendiente". Se verificó además que el guion largo
("—") que separa título y descripción llega correctamente codificado
en UTF-8 en la respuesta HTTP (un mojibake visto en un run de prueba
anterior era solo un problema de cómo esta terminal imprime el
carácter, no del contenido real servido por Flask). Tras verificar,
se borró el archivo `tareas.db` de pruebas para no dejar datos de
prueba en el proyecto.

**Cómo reproducirlo**: con el entorno virtual activado, ejecutar
`python app.py`, abrir `http://127.0.0.1:5000/`, pulsar "+ Nueva
tarea", intentar guardar sin título (debe mostrar el error) y luego
con un título y descripción (debe aparecer en el listado como
"Pendiente").

---

## Entrada 6 — Confirmación del Incremento 2 con evidencia

**Prompt literal**:

> "Capturas añadidas. Revisado y aceptado, sigamos."

**Resultado generado**: confirmación verificada del Incremento 2 con
tres capturas (terminal con el log de peticiones `GET /`, `GET
/tareas/nueva`, `POST /tareas/nueva` → 302, `GET /` de nuevo;
navegador mostrando el listado con una tarea creada marcada como
"Pendiente"; navegador mostrando el formulario de alta vacío). De
nuevo aparecieron en `actividad1/capturas/` (el proyecto archivado del
Termómetro de Centro) en vez de en este proyecto — se movieron a
`actividad1_gestor_tareas/capturas/` con nombres descriptivos
(`incremento2-terminal.png`, `incremento2-listado.png`,
`incremento2-formulario.png`) y se dejó sin cambios el repositorio Git
de `actividad1/` (los archivos habían quedado en stage ahí; se
revirtieron con `git reset HEAD` antes de moverlos, para no dejar ese
proyecto archivado con cambios pendientes).

**Nota para el usuario** (no bloqueante): esto ya ha pasado dos veces
seguidas — probablemente la herramienta de capturas tenga
`actividad1/capturas/` configurada como carpeta de guardado por
defecto desde la sesión anterior. Si cambias ese destino a
`actividad1_gestor_tareas/capturas/` te ahorras que seamos nosotros
quienes lo corrijamos cada vez.

**Cómo se verificó**: se abrieron las tres imágenes para confirmar que
correspondían al Incremento 2 de este proyecto (URLs
`127.0.0.1:5000/` y `127.0.0.1:5000/tareas/nueva`, contenido textual
coincidente con las plantillas `index.html`/`nueva_tarea.html`).

**Cómo reproducirlo**: no aplica — corrección de ubicación de
archivos.

