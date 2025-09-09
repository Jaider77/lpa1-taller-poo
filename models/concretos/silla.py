"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

from models.categorias.asientos import Asiento

class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    """
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas
        self._altura_actual = 45  # Altura en cm, valor por defecto

    @property
    def altura_regulable(self) -> bool:
        return self._altura_regulable

    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        self._altura_regulable = value

    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        self._tiene_ruedas = bool(value)

    @property
    def altura_actual(self) -> int:
        return self._altura_actual

    def calcular_precio(self) -> float:
        precio = self._precio_base
        precio += self.calcular_factor_comodidad() * 20
        if self._altura_regulable:
            precio += 15
        if self._tiene_ruedas:
            precio += 25
        if self._material_tapizado:
            precio += 15
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        desc = f"Silla '{self.nombre}' de {self.material}, color {self.color}, "
        desc += "con respaldo" if self.tiene_respaldo else "sin respaldo"
        if self.material_tapizado:
            desc += f", tapizada en {self.material_tapizado}"
        desc += f". Altura regulable: {'Sí' if self._altura_regulable else 'No'}"
        desc += f". Ruedas: {'Sí' if self._tiene_ruedas else 'No'}"
        desc += f". Precio: ${self.calcular_precio():,.2f}"
        return desc

    def regular_altura(self, nueva_altura: int) -> str:
        if not self._altura_regulable:
            return "Esta silla no permite regular la altura."
        if 40 <= nueva_altura <= 55:
            self._altura_actual = nueva_altura
            return f"Altura ajustada a {nueva_altura} cm."
        return "Altura fuera de rango permitido (40-55 cm)."

    def es_silla_oficina(self) -> bool:
        return self._tiene_ruedas and self._altura_regulable