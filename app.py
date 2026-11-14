"""Gestor de tareas — punto de entrada de la aplicación Flask.

Incremento 1: estructura del proyecto + modelo de datos. Ruta de
comprobación única; todavía no hay alta/listado real de tareas.
"""

from flask import Flask, render_template

from database import contar_tareas, inicializar_bd

app = Flask(__name__)
inicializar_bd()


@app.route("/")
def inicio():
    total = contar_tareas()
    return render_template("index.html", total_tareas=total)


if __name__ == "__main__":
    app.run(debug=True)
