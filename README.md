# Gestor de tareas

Aplicación web mínima para gestionar una lista de tareas personales,
con persistencia real en SQLite. Desarrollada como Actividad 1 de la
asignatura PSU IA Generativa (máster DevOps, UNIR): todo el código fue
generado mediante interacción con un asistente de IA (Claude), sin
escritura manual de código — ver `docs/registro_prompts.md` para el
registro completo de la interacción.

Ver `docs/definicion_proyecto.md` para la descripción funcional
completa y los requisitos mínimos.

## Requisitos

- Python 3.12 o superior.

## Cómo ejecutarla en local

1. Crear y activar un entorno virtual (si no existe ya `.venv/`):

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instalar las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

3. Arrancar la aplicación:

   ```powershell
   python app.py
   ```

4. Abrir `http://127.0.0.1:5000/` en el navegador.

La base de datos (`tareas.db`) se crea automáticamente en la carpeta
del proyecto la primera vez que se arranca la aplicación, si no existe
ya.

## Funcionalidad

- Crear tareas (título obligatorio, descripción opcional).
- Listar todas las tareas, distinguiendo visualmente las completadas
  de las pendientes.
- Marcar una tarea como completada o pendiente.
- Editar el título/descripción de una tarea existente.
- Eliminar una tarea de forma permanente (con pantalla de
  confirmación previa).

## Estructura del proyecto

```
actividad1_gestor_tareas/
├── app.py              # Rutas de Flask
├── database.py         # Acceso a SQLite (sin ORM)
├── templates/          # Plantillas Jinja2
├── static/style.css    # Estilos mínimos
├── requirements.txt
├── docs/
│   ├── definicion_proyecto.md
│   └── registro_prompts.md   # Registro de la interacción con la IA
└── capturas/            # Capturas de pantalla de cada incremento
```
