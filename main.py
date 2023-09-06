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

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Welcome to Kw4rgs's validators and extractors"}

# Extractor endpoints
@app.post("/api/v1/extractor/cedula")
async def cedula_endpoint(data: dict):
    extracted_data = cedula_extractor(data)
    return extracted_data

@app.post("/api/v1/extractor/dni")
async def dni_endpoint(data: dict):
    extracted_data = dni_extractor(data)
    return extracted_data

# Validators endpoints
@app.post("/api/v1/validator/car")
async def car_endpoint(data: dict):
    validate = car_validator(data)
    return validate

@app.post("/api/v1/validator/cedula")
async def cedula_validator_endpoint(data: dict):
    validate = cedula_validator(data)
    return validate

@app.post("/api/v1/validator/dni")
async def dni_validator_endpoint(data: dict):
    validate = dni_validator(data)
    return validate

@app.post("/api/v1/validator/licencia/front")
async def licencia_front_validator_endpoint(data: dict):
    validate = licencia_front_validator(data)
    return validate

@app.post("/api/v1/validator/licencia/back")
async def licencia_back_validator_endpoint(data: dict):
    validate = licencia_back_validator(data)
    return validate

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=6969, reload=True, workers=1)
