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


def contar_tareas():
    """Número total de tareas guardadas. Usado solo como comprobación en el Incremento 1."""
    conexion = obtener_conexion()
    total = conexion.execute("SELECT COUNT(*) AS total FROM tareas").fetchone()["total"]
    conexion.close()
    return total
