from fastapi import FastAPI
import uvicorn
from kvalidator import cedula_extractor, dni_extractor, car_validator, cedula_validator, dni_validator, licencia_front_validator, licencia_back_validator

app = FastAPI()

@app.get("/")
def health_Check():
    return {"message": "Welcome to Kw4rgs's validators and extractors"}

#TEST

# Extractor endpoints
    # Cedula
    # DNI
    
@app.post("/api/v1/extractor/cedula")
async def cedula_endpoint(data: dict):
    extracted_data = cedula_extractor(data)
    return extracted_data

@app.post("/api/v1/extractor/dni")
async def dni_endpoint(data: dict):
    extracted_data = dni_extractor(data)
    return extracted_data

# Validators endpoints
    # Car
    # Cedula
    # DNI
    # Licencia

# Car
@app.post("/api/v1/validator/car")
async def car_endpoint(data: dict):
    validate = car_validator(data)
    return validate

# Cedula
@app.post("/api/v1/validator/cedula")
async def cedula_endpoint(data: dict):
    validate = cedula_validator(data)
    return validate

# DNI
@app.post("/api/v1/validator/dni")
async def dni_back_endpoint(data: dict):
    validate = dni_validator(data)
    return validate

# Licencia Front
@app.post("/api/v1/validator/licencia/front")
async def licencia_back_endpoint(data: dict):
    validate = licencia_front_validator(data)
    return validate

# Licencia Back
@app.post("/api/v1/validator/licencia/back")
async def licencia_back_endpoint(data: dict):
    validate = licencia_back_validator(data)
    return validate



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=6969, reload=True, workers=1)
