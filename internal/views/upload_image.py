from internal.app import app
from flask import request, jsonify, render_template
import os
from internal.utils.validate_filename import validate_filename
import json


@app.route("/api/uploadImage", methods=["POST"])
def index():
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
