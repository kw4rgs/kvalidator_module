import tensorflow as tf
import cv2
import numpy as np
import base64

model_path = 'kvalidator/validators/assets/kw4rgs_car_model_v1'

class CarValidator:
    def __init__(self, model_path: str):
        self.model = tf.keras.models.load_model(model_path)
        self.categories = {0: False, 1: True}

    def predict_base64_image(self, image_data: str) -> bool:
        try:
            image_bytes = base64.b64decode(image_data)
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img is not None:
                img = cv2.resize(img, (224, 224))
                img = img.astype(float) / 255

                predictions = self.model.predict(img.reshape(-1, 224, 224, 3))
                predicted_class = np.argmax(predictions[0], axis=-1)
                
                return bool(predicted_class == 1)
            else:
                raise ValueError("Failed to process the image.")
        except Exception as e:
            return False  

def car_validator(data: dict):
    try:
        image_data = data.get('data')
        if image_data is None:
            return {'error': 'No image data was provided'}
        car_validator_instance = CarValidator(model_path)
        result = car_validator_instance.predict_base64_image(image_data)
        
        if result is None:
            return {'error': 'An error occurred while processing the image'}
        return {'is_valid': result}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {e}'}
