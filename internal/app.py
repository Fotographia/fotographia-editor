from flask import Flask
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT, "static/images")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
