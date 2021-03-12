from internal.app import app
from flask import render_template, request


@app.route("/editor")
def editor():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = "images/" + session_id + "/" + filename
    return render_template("editor.html", filename=path)
