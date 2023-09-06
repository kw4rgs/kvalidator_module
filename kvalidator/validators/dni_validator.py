import cv2
import numpy as np
import base64

class DNIBackValidator:
    def __init__(self):
        self.logo_images = self.load_references()
        self.threshold = 0.80

    def load_references(self):
        pais_logo = cv2.imread('kvalidator/validators/assets/kw4rgs_logo_collection/dni_back/dni_pais.png', cv2.IMREAD_UNCHANGED)
        arrows_logo = cv2.imread('kvalidator/validators/assets/kw4rgs_logo_collection/dni_back/dni_arrows.png', cv2.IMREAD_UNCHANGED)
        pulgar_logo = cv2.imread('kvalidator/validators/assets/kw4rgs_logo_collection/dni_back/dni_pulgar.png', cv2.IMREAD_UNCHANGED)
        return [pais_logo, arrows_logo, pulgar_logo]

    def validate(self, image_data):
        target_image = base64.b64decode(image_data)
        nparr = np.frombuffer(target_image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        found_logos = []

        for logo in self.logo_images:
            result = cv2.matchTemplate(img, logo, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= self.threshold)
            
            if loc[0].size > 0:
                found_logos.append(logo)

        return len(found_logos) > 0



def dni_validator(data: dict):
    try:
        image_data = data.get('data')
        if image_data is None:
            return {'error': 'No image data was provided'}
        validator_instance = DNIBackValidator()
        result = validator_instance.validate(image_data)

        if result is None:
            return {'error': 'An error occurred while processing the image'}
        return {'is_valid': result}

    except Exception as e:
        return {'error': f'An unexpected error occurred: {e}'}
