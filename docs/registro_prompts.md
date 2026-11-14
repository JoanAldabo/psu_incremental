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

