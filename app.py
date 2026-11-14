"""Gestor de tareas — punto de entrada de la aplicación Flask.

Incremento 4: eliminar tarea, con pantalla de confirmación previa.
"""

from flask import Flask, abort, redirect, render_template, request, url_for

from database import (
    actualizar_tarea,
    alternar_estado,
    crear_tarea,
    eliminar_tarea,
    inicializar_bd,
    obtener_tarea,
    obtener_tareas,
)

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


@app.route("/tareas/<int:id_tarea>/editar", methods=["GET", "POST"])
def editar_tarea(id_tarea):
    tarea = obtener_tarea(id_tarea)
    if tarea is None:
        abort(404)
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        if titulo:
            actualizar_tarea(id_tarea, titulo, descripcion)
            return redirect(url_for("listar_tareas"))
        return render_template(
            "editar_tarea.html", tarea=tarea, error="El título es obligatorio."
        )
    return render_template("editar_tarea.html", tarea=tarea, error=None)


@app.route("/tareas/<int:id_tarea>/alternar", methods=["POST"])
def alternar(id_tarea):
    if obtener_tarea(id_tarea) is None:
        abort(404)
    alternar_estado(id_tarea)
    return redirect(url_for("listar_tareas"))


@app.route("/tareas/<int:id_tarea>/eliminar", methods=["GET", "POST"])
def eliminar(id_tarea):
    tarea = obtener_tarea(id_tarea)
    if tarea is None:
        abort(404)
    if request.method == "POST":
        eliminar_tarea(id_tarea)
        return redirect(url_for("listar_tareas"))
    return render_template("eliminar_tarea.html", tarea=tarea)


if __name__ == "__main__":
    app.run(debug=True)
