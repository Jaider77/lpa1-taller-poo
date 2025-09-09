"""
Clase abstracta para muebles de almacenamiento.
"""
from abc import ABC, abstractmethod
from models.mueble import Mueble

class Almacenamiento(Mueble, ABC):
    def __init__(self, material: str, color: str, alto: float, ancho: float, profundo: float):
        super().__init__(material, color, alto, ancho, profundo)
        self._puertas = puertas
        self._cajones = cajones
    
    @property
    def puertas(self):
        return self._puertas
    @property
    def cajones(self):
        return self._cajones
    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass 
