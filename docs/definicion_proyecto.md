# Definición del proyecto — Gestor de tareas

**Actividad**: PSU IA Generativa — Actividad 1, "Desarrollo de
aplicaciones con asistentes de programación basados en IA" (máster
DevOps, UNIR).

## Descripción funcional

Aplicación web de gestión de tareas personales de un único usuario, sin
autenticación (no hay multi-usuario: se asume un solo usuario local).
Permite crear, consultar, editar, marcar como completadas y eliminar
tareas, con persistencia real en una base de datos SQLite local — los
datos sobreviven a reiniciar la aplicación.

La interfaz es navegable mediante páginas HTML renderizadas por el
servidor (no una API JSON pura), para que la aplicación se pueda
demostrar y capturar en pantalla directamente desde un navegador.

## Objetivo

Resolver una necesidad concreta y sencilla (llevar el control de una
lista de tareas pendientes) con una aplicación mínima pero
completamente funcional, construida en su totalidad mediante
interacción con un asistente de IA (Claude Code), sin escribir código a
mano.

## Requisitos mínimos / funcionalidades esenciales

1. **Crear tarea**: formulario con al menos un campo de título
   (obligatorio) y, opcionalmente, una descripción.
2. **Listar tareas**: página principal que muestra todas las tareas
   existentes, distinguiendo visualmente las completadas de las
   pendientes.
3. **Marcar como completada / pendiente**: alternar el estado de una
   tarea existente.
4. **Editar tarea**: modificar el título y/o la descripción de una
   tarea ya creada.
5. **Eliminar tarea**: borrar una tarea de forma permanente (con
   confirmación antes de borrar).
6. **Persistencia real**: todos los cambios se guardan en SQLite; los
   datos no se pierden al reiniciar el servidor.

## Enfoque técnico

- **Backend**: Python + Flask.
- **Plantillas**: Jinja2 (HTML servido por el propio Flask, sin
  frontend separado).
- **Persistencia**: módulo `sqlite3` de la librería estándar de
  Python, sin ORM. Justificación: la aplicación tiene una sola entidad
  (`tarea`) con operaciones CRUD simples; un ORM como SQLAlchemy
  añadiría una capa de abstracción y una dependencia extra sin
  aportar nada que `sqlite3` no resuelva ya de forma directa para este
  alcance. Si el alcance creciera (varias entidades relacionadas,
  migraciones complejas), SQLAlchemy pasaría a ser la opción más
  razonable.

## Fuera de alcance (explícitamente, para no ampliar sin acordarlo)

- Autenticación o multi-usuario.
- Categorías, etiquetas, prioridades, fechas límite o recordatorios.
- API JSON además de las páginas HTML.
- Despliegue en un servidor remoto (se ejecuta y se demuestra en
  local).
- Tests automatizados (no los pide el enunciado de esta actividad; si
  se decide añadir alguno más adelante, será una decisión explícita,
  no implícita).

Cualquier funcionalidad no listada arriba que surja como idea durante
el desarrollo se propondrá antes de implementarla, no se añadirá por
iniciativa propia.
