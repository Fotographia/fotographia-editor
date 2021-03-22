import cv2
from flask import request, jsonify
from internal.app import app
from internal.lib.get_resolution import get_resolution


@app.route("/api/resolution")
def resolution():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    resolution = get_resolution(path)

    return jsonify(resolution), 200
