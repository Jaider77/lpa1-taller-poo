"""
Clase concreta Mesa.
"""
from models.categorias.superficies import Superficie
class Mesa(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float, superficie_trabajo: float, capacidad_personas: int = 4):
        super().__init__(nombre, material, color, precio_base, superficie_trabajo)
        self._capacidad_personas = capacidad_personas
       
    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas
    @capacidad_personas.setter
    def capacidad_personas(self, value: int):
        """Setter para capacidad con validación."""
        if value <= 1:
            raise ValueError("La capacidad debe ser mayor a 1")
        self._capacidad_personas = value

    def calcular_precio(self) -> float:
        return self.precio_base + (self.superficie_trabajo * 15) + (self.capacidad_personas * 10)
    
    def obtener_descripcion(self) -> str:
        return (f"Mesa '{self._nombre}' de {self._material}, color {self._color}, "
                f"superficie {self._superficie_trabajo} m², capacidad para {self._capacidad_personas} personas. "
                f"Precio: ${self.calcular_precio():,.2f}")
       