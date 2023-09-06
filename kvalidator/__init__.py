from .extractors.cedula_extractor import cedula_extractor
from .extractors.dni_extractor import dni_extractor
from .validators.car_validator import car_validator
from .validators.cedula_validator import cedula_validator
from .validators.dni_validator import dni_validator
from .validators.licencia_validator import licencia_front_validator, licencia_back_validator

"""
kvalidator: Un paquete Python que contiene extractores y validadores para documentos personales.
"""

__all__ = ["cedula_extractor", "dni_extractor", "car_validator", "cedula_validator", "dni_validator", "licencia_front_validator", "licencia_back_validator"]

__version__ = "1.0.0"

