import base64
from pyzbar import pyzbar
import cv2
import numpy as np
from flask import Flask
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)
class BarcodeReader(Resource):
    def get(self,base64string):
        image = base64.urlsafe_b64decode(base64string)
        decoded = cv2.imdecode(np.frombuffer(image, np.uint8), -1)
        image_decode = pyzbar.decode(decoded)
        if(len(image_decode)==0):
            return {"status":404,"error":"barcode not found"}
        data = image_decode[0].data
        print(data)
        return {"status":200,"barcodedata":data.decode('UTF-8')}

api.add_resource(BarcodeReader,"/barcodereader/<string:base64string>")

if __name__ == "__main__":
    app.run(debug=True)


