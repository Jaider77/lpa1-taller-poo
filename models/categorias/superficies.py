"""
Clase abstracta para muebles para superficios de trabajo o del hogar .
"""
from abc import ABC, abstractmethod
from models.mueble import Mueble
class Superficie(Mueble, ABC):
    class Superficie (Mueble, ABC):
        def __init__(self, nombre: str, material: str, color: str, precio_base: float, superficie_trabajo: float):
            super().__init__(nombre, material, color, precio_base)
            self._superficie_trabajo = superficie_trabajo

    @property
    def superficie_trabajo(self):
        return self._superficie_trabajo

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass