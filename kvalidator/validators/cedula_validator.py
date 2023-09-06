import cv2
import numpy as np
import base64
import pytesseract
import re

class CedulaBackValidator:
    def __init__(self):
        self.logo_images = self.load_references()
        self.threshold = 0.70

    def load_references(self):
        dnrpa_logo_path = 'kvalidator/validators/assets/kw4rgs_logo_collection/cedula_back/cd_dnrpa.png'
        cedula_logo_path = 'kvalidator/validators/assets/kw4rgs_logo_collection/cedula_back/cd_logo.png'
        return [cv2.imread(dnrpa_logo_path, cv2.IMREAD_UNCHANGED), cv2.imread(cedula_logo_path, cv2.IMREAD_UNCHANGED)]

    def validate(self, image_data):
        try:
            target_image = base64.b64decode(image_data)
            nparr = np.frombuffer(target_image, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            found_logos = [logo for logo in self.logo_images if np.any(cv2.matchTemplate(img, logo, cv2.TM_CCOEFF_NORMED) >= self.threshold)]

            return bool(found_logos)
        except Exception as e:
            raise ValueError(f"Validation error: {e}")

class ImageProcessor:
    def process_image(self, image_base64):
        try:
            image_bytes = base64.b64decode(image_base64)
            image_array = np.frombuffer(image_bytes, dtype=np.uint8)

            decoded_image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            image_rgb = cv2.cvtColor(decoded_image, cv2.COLOR_BGR2RGB)
            image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

            alpha = -2
            beta = 60
            prepro_image = cv2.convertScaleAbs(image_gray, alpha=alpha, beta=beta)

            return prepro_image
        except Exception as e:
            raise ValueError(f"Image processing error: {e}")

class TextExtractor:
    def extract_text(self, image):
        try:
            return pytesseract.image_to_string(image, lang="spa")
        except Exception as e:
            raise ValueError(f"Text extraction error: {e}")

class KeywordChecker:
    def __init__(self):
        self.keywords = ['AUTOMOTOR', 'DNRPA']

    def check_keywords(self, extracted_text):
        try:
            found_words = [word for word in self.keywords if re.search(r'\b' + re.escape(word) + r'\b', extracted_text, re.IGNORECASE)]
            return found_words
        except Exception as e:
            raise ValueError(f"Keyword checking error: {e}")
        
class CedulaBackValidatorAlt:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.text_extractor = TextExtractor()
        self.keyword_checker = KeywordChecker()
        
    def validate(self, image_base64):
        try:
            prepro_image = self.image_processor.process_image(image_base64)
            extracted_text = self.text_extractor.extract_text(prepro_image)
            found_keywords = self.keyword_checker.check_keywords(extracted_text)

            return bool(found_keywords)
        except Exception as e:
            raise ValueError(f"Alternative validation error: {e}")

def cedula_validator(data: dict):
    try:
        image_data = data.get('data')
        if image_data is None:
            return {'error': 'No image data was provided'}
        validator_instance = CedulaBackValidator()
        validator_instance_alt = CedulaBackValidatorAlt()
        
        is_valid = validator_instance.validate(image_data)
        is_valid_alt = validator_instance_alt.validate(image_data)
        
        result = is_valid or is_valid_alt
        
        if result is None:
            return {'error': 'An error occurred while processing the image'}
        
        return {'is_valid': result}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {e}'}
