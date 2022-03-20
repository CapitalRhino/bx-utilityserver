import base64
from pyzbar import pyzbar
import cv2
import numpy as np
from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
from flask import request
import ast
app = Flask(__name__)
CORS(app)
@app.route("/barcodereader", methods=["POST"])
def barcodereader():
    data = request.data.decode('utf-8')
    data = ast.literal_eval(data)
    base64string = data["image"]
    image = base64.urlsafe_b64decode(base64string)
    decoded = cv2.imdecode(np.frombuffer(image, np.uint8), -1)
    image_decode = pyzbar.decode(decoded)
    if(len(image_decode)==0):
        return {"status":404,"error":"barcode not found"}
    data = image_decode[0].data
    print(data)
    return {"status":200,"barcodedata":data.decode('UTF-8')}
@app.route("/hello", methods=["GET"])
def hello():
    return "hello"
