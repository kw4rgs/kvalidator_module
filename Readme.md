<div align="center">
  <img src="https://github.com/kw4rgs/kvalidators/blob/4e55a4d7877eecc9e35bee3d58ac584b8ecdbd7a/kvalidator.png" alt="kvalidator_logo">
</div>

# kvalidator: Image validators and data extractors
 

The Kw4rgs's Document/Image Validation and Data Extraction is a powerful tool that combines:

-   Advanced OCR (Optical Character Recognition) techniques.
-   State-of-the-art Neuronal Networks / Machine Learning algorithms.
-   Robust Computer Vision capabilities and techniques.
-  QR code readers

Whether you're dealing with identification cards, licenses, or other types of documents, this package empowers you to efficiently verify document authenticity, validate their content, and extract pertinent information accurately.

Additionally, it has the capability to determine whether a provided photo is a car photo or not.

## Key Features:

- **Document Validation:** Leverage cutting-edge Computer Vision techniques to authenticate documents by detecting logos, watermarks, and other visual cues.
- **Data Extraction:** Utilize OCR technologies to automatically extract textual and numeric information from images, transforming them into structured and usable data.
- **Customizable Validation:** Tailor validation criteria based on predefined templates and models, allowing adaptation of the API to specific document types and standards.
- **Machine Learning and Neural Networks Integration:** Employ Machine Learning models to enhance accuracy over time, enabling the API to adjust to evolving document formats and potential forgery attempts.
- **Pythonic and User-Friendly:** Developed with Pythonic conventions and an intuitive design, making it accessible for developers to seamlessly integrate into their projects.
- **API Documentation:** Comprehensive API documentation and customizable OpenAPI specifications help developers comprehend endpoints, input requirements, and anticipated responses.

## Use Cases:

- **Document Authentication:** Verify the authenticity of identification cards, licenses, and certificates by detecting hidden security features and logos.
- **Data Extraction:** Automatically extract key data such as names, dates, addresses, and other pertinent information from scanned documents.
- **Fraud Prevention:** Implement advanced algorithms to identify signs of tampering, ensuring that submitted documents are authentic and unaltered.
- **Automated Workflows:** Integrate the API into your workflows to streamline document processing and decrease manual data entry efforts.


## Car Validator:

The Car Validator feature of the KVALIDATOR employs a trained TensorFlow model and advanced OpenCV image processing techniques to accurately determine whether a provided photo is an image of a car or not.

<div align='center' style="display: flex; justify-content: center;">
  <img src="https://github.com/kw4rgs/kvalidators/blob/7999e67da38df77952301edb730cf18c32c30d7c/examples/car1.png" alt="example_1" style="width: 300px; height: 300px; flex: 1;">
  <img src="https://github.com/kw4rgs/kvalidators/blob/7999e67da38df77952301edb730cf18c32c30d7c/examples/car2.jpeg" alt="example_2" style="width: 300px; height: 300px; flex: 1;">
  <img src="https://github.com/kw4rgs/kvalidators/blob/7999e67da38df77952301edb730cf18c32c30d7c/examples/not_car.jpeg" alt="example_3" style="width: 300px; height: 300px; flex: 1;">
</div>

## Installation


Clone the repository and install kvalidator using pip:

  

```bash

pip  install  kvalidator

```

  

Make sure you have the following dependencies installed:

  

```bash

pip  install  pydantic  httpx  opencv-python  pyzbar  numpy  tensorflow  pytesseract  zxing

```
And also you will need tesseract on your machine (spanish version):
```bash

sudo apt-get install tesseract-ocr -y

sudo apt-get install tesseract-ocr-spa -y

```
  

## How to Use
I will attach and use a minimal FastAPI example for all the modules:
  

```python

from fastapi import FastAPI

import uvicorn

from kvalidator import (

cedula_extractor,

dni_extractor,

car_validator,

cedula_validator,

dni_validator,

licencia_front_validator,

licencia_back_validator,

)

  

app  = FastAPI()

  

@app.get("/")

def  health_check():

return {"message": "Welcome to Kw4rgs's validators and extractors"}

  

# Extractor endpoints

@app.post("/api/v1/extractor/cedula")

async  def  cedula_endpoint(data:  dict):

extracted_data  =  cedula_extractor(data)

return  extracted_data

  

@app.post("/api/v1/extractor/dni")

async  def  dni_endpoint(data:  dict):

extracted_data  =  dni_extractor(data)

return  extracted_data

  

# Validators endpoints

@app.post("/api/v1/validator/car")

async  def  car_endpoint(data:  dict):

validate  =  car_validator(data)

return  validate

  

@app.post("/api/v1/validator/cedula")

async  def  cedula_validator_endpoint(data:  dict):

validate  =  cedula_validator(data)

return  validate

  

@app.post("/api/v1/validator/dni")

async  def  dni_validator_endpoint(data:  dict):

validate  =  dni_validator(data)

return  validate

  

@app.post("/api/v1/validator/licencia/front")

async  def  licencia_front_validator_endpoint(data:  dict):

validate  =  licencia_front_validator(data)

return  validate

  

@app.post("/api/v1/validator/licencia/back")

async  def  licencia_back_validator_endpoint(data:  dict):

validate  =  licencia_back_validator(data)

return  validate

  

if  __name__  ==  "__main__":

	uvicorn.run(app)

```

  

## Examples

  

Check the `examples` directory for more usage examples and sample images.

  

## Functions Explained

- `Validators`: 
**car_validator**, **cedula_validator**, **dni_validator** and **licencia_validator**
These functions will be useful to validate if a:
	- Cedula image, is valid or not.
	-  DNI image, is valid or not.
	- Licencia image, is valid or not.
	- A Car image, is valid or not.

- `DataExtractor`: 
**cedula_extractor** and **dni_extractor**
These functions will be useful to extract data from:
	- Cedula image.
	-  DNI image.

All the images provided should be in base64 format. 
You have to pass the image (str) as a key:value (dict), like this:

```bash
{ 
	"data": "<image base64>"
}
```

## Versions

  - v1.0.0: Initial release (September 2023)


  

## References

  

- [TensorFlow Documentation](https://www.tensorflow.org/)

- [PyTesseract Documentation](https://pypi.org/project/pytesseract/)


  

## Future Plans

  

- Add support for different images recognition.

- Improve data extraction accuracy.

  

## Dependencies

  

- FastAPI

- Uvicorn

- Python-dotenv

- Pydantic

- Httpx

- OpenCV-python

- Pyzbar

- Numpy

- TensorFlow

- PyTesseract

- Zxing

  

## Contact Information

  

For questions or feedback, please contact us at:

- Email: kw4rgs@gmail.com

- GitHub: [https://github.com/kw4rgs](https://github.com/kw4rgs)

