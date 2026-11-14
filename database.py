"""Capa de acceso a datos: conexión SQLite y creación del esquema.

Decisión documentada en docs/definicion_proyecto.md: se usa el módulo
sqlite3 de la librería estándar (sin ORM) porque hay una sola entidad
(tarea) con operaciones CRUD simples.
"""

import sqlite3
from pathlib import Path

RUTA_BD = Path(__file__).parent / "tareas.db"


def obtener_conexion():
    """Devuelve una conexión SQLite con filas accesibles por nombre de columna."""
    conexion = sqlite3.connect(RUTA_BD)
    conexion.row_factory = sqlite3.Row
    return conexion


def inicializar_bd():
    """Crea la tabla `tareas` si todavía no existe. Es seguro llamarla siempre."""
    conexion = obtener_conexion()
    conexion.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            completada INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conexion.commit()
    conexion.close()


def obtener_tareas():
    """Todas las tareas guardadas, ordenadas por id ascendente."""
    conexion = obtener_conexion()
    filas = conexion.execute(
        "SELECT id, titulo, descripcion, completada FROM tareas ORDER BY id"
    ).fetchall()
    conexion.close()
    return filas


def crear_tarea(titulo, descripcion):
    """Inserta una tarea nueva. `titulo` es obligatorio; `descripcion` puede ser vacía."""
    conexion = obtener_conexion()
    conexion.execute(
        "INSERT INTO tareas (titulo, descripcion, completada) VALUES (?, ?, 0)",
        (titulo, descripcion),
    )
    conexion.commit()
    conexion.close()


def obtener_tarea(id_tarea):
    """Una tarea por id, o None si no existe."""
    conexion = obtener_conexion()
    fila = conexion.execute(
        "SELECT id, titulo, descripcion, completada FROM tareas WHERE id = ?",
        (id_tarea,),
    ).fetchone()
    conexion.close()
    return fila


def actualizar_tarea(id_tarea, titulo, descripcion):
    """Actualiza el título y la descripción de una tarea existente."""
    conexion = obtener_conexion()
    conexion.execute(
        "UPDATE tareas SET titulo = ?, descripcion = ? WHERE id = ?",
        (titulo, descripcion, id_tarea),
    )
    conexion.commit()
    conexion.close()


def alternar_estado(id_tarea):
    """Invierte el estado completada/pendiente de una tarea."""
    conexion = obtener_conexion()
    conexion.execute(
        "UPDATE tareas SET completada = 1 - completada WHERE id = ?",
        (id_tarea,),
    )
    conexion.commit()
    conexion.close()
