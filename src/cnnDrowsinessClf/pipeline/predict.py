import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import pyttsx3

class DrowsinessEffect:
    def __init__(self, filename):
        self.filename = filename

    def prediction(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Load the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make prediction
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        # Interpret prediction
        if result[0] == 1:
            prediction = 'The person is not yawning. Have a safe drive and good day!'
        elif result[0] == 2:
            prediction = 'The person has open eyes. Have a safe drive and good day!'
        elif result[0] == 3:
            prediction = 'The person is yawning. Alert the driver! Please ensure you are well-rested and take breaks if needed.'
            self.trigger_alert()
        else:
            prediction = 'The person has closed eyes. Alert the driver! Please ensure you are well-rested and take breaks if needed.'
            self.trigger_alert()

        # Speak the prediction using pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust the speaking rate (words per minute)
        engine.setProperty('volume', 1.5)  # Adjust the volume (0.0 to 1.0)
        engine.say(prediction)
        engine.runAndWait()

        return {'prediction': prediction, 'audio_message': f"The prediction is {prediction}"}

    def trigger_alert(self):
        # Implement your alert mechanism here
        # For demonstration, let's use a simple alert function
        alert("Driver Alert: Pay attention!")


