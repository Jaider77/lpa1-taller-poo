"""
Clase concreta Sofa.
"""
from models.categorias.asientos import Asiento

class Sofa(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float, capacidad_personas: int=3, tiene_respaldo: bool=True, material_tapizado: str="tela"):
       super().__init__(nombre, material, color, precio_base, capacidad_personas, tiene_respaldo, material_tapizado)

    def calcular_precio(self) -> float:
        precio = self.precio_base
        precio += self.calcular_factor_comodidad() * 30
        if self.tiene_respaldo:
            precio += 50
        precio += self.capacidad_personas * 40
        return round(precio, 2)
    def obtener_descripcion(self)-> str:
        return (f"sofá '{self.nombre}' de material {self.material}, color {self.color}, "
                f"capacidad para {self.capacidad_personas} personas, "
                f"tapizado en {self.material_tapizado if self.material_tapizado else 'sin tapizado'}, "
                f"precio: ${self.calcular_precio():.2f}")

       