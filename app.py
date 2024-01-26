from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnDrowsinessClf.utils import decodeImage
from src.cnnDrowsinessClf.pipeline.predict import DrowsinessEffect

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = DrowsinessEffect(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image_data = request.json['image']
    decodeImage(image_data, clApp.filename)
    
    # Get prediction result and audio message
    prediction_result = clApp.classifier.prediction()
    
    # Return a JSON response with both prediction and audio_message
    response = {'prediction': prediction_result['prediction'], 'audio_message': prediction_result['audio_message']}
    
    return jsonify(response)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)