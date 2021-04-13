from flask import Flask, render_template, url_for, request, jsonify
from utils.validate_filename import validate_filename
from utils.get_resolution import get_resolution
from utils.resize import resize
from utils.blur import blur
from utils.grayscale import grayscale
from utils.negate import negate
from utils.flip import flip
import json
import os

# The app variable
app = Flask(__name__)

# Constants
PORT = os.getenv("PORT")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, "static/img")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/editor")
def editor():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")
    path = "img/" + session_id + "/" + filename
    return render_template("editor.html", filename=path)


@app.route("/api/upload", methods=["POST"])
def upload():

    # request file from frontend
    file = request.files["file"]
    session_id = request.args.get("session_id")

    # Upload Folder path
    UPLOAD_FOLDER = os.path.join(app.config["UPLOAD_FOLDER"], session_id)
    os.makedirs(UPLOAD_FOLDER)

    # check if file is valid
    is_file_valid = validate_filename(file.filename)
    if file and is_file_valid:
        filename = file.filename or ""

        # save file
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        return jsonify("Image Uploaded Successfully."), 200
    else:
        return jsonify("An error occured!"), 400


@app.route("/api/resolution")
def resolution():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    resolution = get_resolution(path)

    return jsonify(resolution), 200


@app.route("/api/resize", methods=["POST"])
def resize_image():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    width = int(data["width"])
    height = int(data["height"])

    resize(path, width, height)

    return jsonify("OK"), 200


@app.route("/api/grayscale")
def grayscale_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    grayscale(path)

    return jsonify("OK"), 200


@app.route("/api/blur")
def feature_blur():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename
    blur(path)

    return jsonify("OK"), 200


@app.route("/api/negate")
def negate_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename
    negate(path)

    return jsonify("OK"), 200


@app.route("/api/flip", methods=["POST"])
def flip_image():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.get_json("val")
    select_val = data["val"]

    flip(path, select_val)

    return jsonify("OK"), 200


# Main
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
