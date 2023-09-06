# kvalidator/extractors/cedula_extractor.py
from zxing import BarCodeReader
import cv2
import numpy as np
import tempfile
import base64

class BarcodeProcessor:
    def __init__(self):
        self.reader = BarCodeReader()

    def decode_barcode(self, image_path):
        return self.reader.decode(image_path)

class CedulaExtractor:
    def __init__(self):
        self.barcode_processor = BarcodeProcessor()

    def enhance_image(self, image):
        enhanced_image = cv2.convertScaleAbs(image, alpha=1.2, beta=50)
        return enhanced_image

    def extract_cedula_data(self, image_data):
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            enhanced_image = self.enhance_image(image)
            cv2.imwrite(temp_file.name, enhanced_image)

        barcode = self.barcode_processor.decode_barcode(temp_file.name)
        
        if barcode is not None:
            barcode_data = barcode.raw
            if barcode_data is None:
                return None 
            formatted_data = self.format_data(barcode_data)
            return formatted_data

    def format_data(self, barcode_data):
        data_splitted = barcode_data.split(sep='\n')
        data = {
            'cedula_id': data_splitted[0],
            'dominio': data_splitted[1],
            'chasis': data_splitted[2],
        }
        return data

def cedula_extractor(data: dict):
    try: 
        image_data = data.get('data')
        if image_data is None:
            return {'error': 'No image data was provided'}
        image_bytes = base64.b64decode(image_data)
        cedula_extractor = CedulaExtractor()
        extracted_data = cedula_extractor.extract_cedula_data(image_bytes)
        return extracted_data
    except Exception as e:
        return {'error': f'An unexpected error occurred: {e}'}
