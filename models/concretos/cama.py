"""
Clase concreta Cama.
"""
from models.categorias.almacenamiento import Almacenamiento
class Cama(Almacenamiento):
       def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True):
        # Puertas y cajones en cama suelen ser 0
        super().__init__(nombre, material, color, precio_base, puertas=0, cajones=0)
        self._tamaño_cama = tamaño_cama
        self._incluye_colchon = incluye_colchon

       @property
       def tamaño_cama(self) -> str:
          return self._tamaño_cama

       @property
       def incluye_colchon(self) -> bool:
           return self._incluye_colchon
       
       def calcular_precio(self) -> float:
              precio = self.precio_base
              if self.tamaño_cama == "individual":
                precio += 200
              elif self.tamaño_cama == "matrimonial":
                precio += 350
              elif self.tamaño_cama == "queen":
                precio += 300
              elif self.tamaño_cama == "king":                      
                precio += 400
              if self.incluye_colchon:
                precio += 250
              return round(precio, 2)
       def obtener_descripcion(self) -> str:
          return (f"Cama '{self.nombre}' de tamaño {self.tamaño_cama}, material {self.material}, "
                  f"color {self.color}, {'incluye colchón' if self.incluye_colchon else 'sin colchón'}, "
                  f"precio: ${self.calcular_precio():.2f}")
       
     