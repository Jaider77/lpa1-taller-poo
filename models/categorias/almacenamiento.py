"""
Clase abstracta para muebles de almacenamiento.
"""
from abc import ABC, abstractmethod
from models.mueble import Mueble

class Almacenamiento(Mueble, ABC):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float, puertas: int, cajones: int):
        super().__init__(nombre, material, color, precio_base)
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
