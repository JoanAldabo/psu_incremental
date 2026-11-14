"""Gestor de tareas — punto de entrada de la aplicación Flask.

Incremento 2: crear y listar tareas.
"""

from flask import Flask, redirect, render_template, request, url_for

from database import crear_tarea, inicializar_bd, obtener_tareas

app = Flask(__name__)
inicializar_bd()


@app.route("/")
def listar_tareas():
    tareas = obtener_tareas()
    return render_template("index.html", tareas=tareas)


@app.route("/tareas/nueva", methods=["GET", "POST"])
def nueva_tarea():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        if titulo:
            crear_tarea(titulo, descripcion)
            return redirect(url_for("listar_tareas"))
        return render_template("nueva_tarea.html", error="El título es obligatorio.")
    return render_template("nueva_tarea.html", error=None)


if __name__ == "__main__":
    app.run(debug=True)
