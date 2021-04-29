from flask import Flask, render_template, url_for, request, jsonify
from utils.validate_filename import validate_filename
from utils.get_resolution import get_resolution
from utils.resize import resize
from utils.blur import blur
from utils.grayscale import grayscale
from utils.gamma_correction import gamma_correction
from utils.negate import negate
from utils.rotate import rotate
from utils.flip import flip
from utils.sepia import sepia
from utils.contrast import contrast
from utils.pixelize import pixelize
from utils.edge_detection import edge_detection
from utils.threshold import threshold
from utils.crop import crop
from utils.brightness import brightness
from utils.emboss import emboss
from utils.water_color import water_color
from utils.add_text import add_text
from utils.sketching import sketching
from utils.smooth import smooth
from utils.sharpen import sharpen
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


@app.route("/api/rotate")
def rotate_image():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename
    rotate(path)

    return jsonify("OK"), 200


@app.route("/api/gamma-correction", methods=["POST"])
def feature_gamma_correction():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename
    data = request.json
    gamma = float(data["gamma_value"])

    gamma_correction(path, gamma)

    return jsonify("OK"), 200


@app.route("/api/contrast", methods=["POST"])
def feature_contrast():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.get_json("contrastVal")
    value = int(data["contrastVal"])

    contrast(path, value)

    return jsonify("OK"), 200


@app.route("/api/pixelize", methods=["POST"])
def feature_pixelize():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json
    value = int(data["pixels"])

    pixelize(path, value)

    return jsonify("OK"), 200


@app.route("/api/edge-detection", methods=["POST"])
def feature_edge_detection():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.get_json("val")
    select_val = data["val"]

    edge_detection(path, select_val)

    return jsonify("OK"), 200


@app.route("/api/sepia")
def feature_sepia():

    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    sepia(path)

    return jsonify("OK"), 200


@app.route("/api/threshold", methods=["POST"])
def feature_threshold():

    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.get_json("thres_value")
    values = data["thres_value"]

    threshold(path, values)

    return jsonify("OK"), 200


@app.route("/api/crop", methods=["POST"])
def crop_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    X = int(data["X"])
    Y = int(data["Y"])
    xOffset = int(data["xOffset"])
    yOffset = int(data["yOffset"])

    crop(path, X, Y, xOffset, yOffset)

    return jsonify("OK"), 200


@app.route("/api/brightness", methods=["POST"])
def brightness_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json
    value = int(data["bright_value"])

    brightness(path, value)

    return jsonify("OK"), 200


@app.route("/api/emboss", methods=["POST"])
def emboss_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    sel_depth = int(data["embDepth"])
    scale = float(data["embScale"])
    offset = int(data["embOffset"])

    emboss(path, sel_depth, scale, offset)

    return jsonify("OK"), 200


@app.route("/api/water-color", methods=["POST"])
def watercolor_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    wc_value = float(data["watercolor_val"])

    water_color(path, wc_value)

    return jsonify("OK"), 200


@app.route("/api/add-text", methods=["POST"])
def add_text_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    ftext = data["instext"]
    x = int(data["xpos"])
    y = int(data["ypos"])
    ffamily = data["selfamily"]
    fstyle = data["selstyle"]
    fcolor = data["pickcolor"]
    fsize = int(data["selsize"])
    falign = data["selalign"]

    add_text(path, ftext, x, y, ffamily, fstyle, fcolor, fsize, falign)

    return jsonify("OK"), 200


@app.route("/api/sketch", methods=["POST"])
def sketch_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    mode = int(data["skmode"])
    sr = float(data["skdensity"])
    sf = float(data["skshading"])

    sketching(path, mode, sr, sf)

    return jsonify("OK"), 200


@app.route("/api/smooth", methods=["POST"])
def smooth_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json

    value = int(data["smooth_val"])

    smooth(path, value)

    return jsonify("OK"), 200


@app.route("/api/sharpen", methods=["POST"])
def sharpen_func():
    session_id = request.args.get("session_id")
    filename = request.args.get("filename")

    path = app.config["UPLOAD_FOLDER"] + "/" + session_id + "/" + filename

    data = request.json
    value = int(data["sharpen_val"])

    sharpen(path, value)

    return jsonify("OK"), 200


# Main
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
