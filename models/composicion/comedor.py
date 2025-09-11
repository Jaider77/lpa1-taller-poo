"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""

#  Importar las clases necesarias
# from ..concretos.mesa import Mesa
# from ..concretos.silla import Silla
# from typing import List
from ..concretos.mesa import Mesa
from ..concretos.silla import Silla
from typing import List

class Comedor:
    """
    Clase que implementa composición conteniendo una mesa y sillas.
    
    Un comedor es un conjunto de muebles que trabajan juntos.
    La relación es de composición porque el comedor "tiene" una mesa
    y "tiene" sillas, pero estas pueden existir independientemente.
    
    Conceptos OOP aplicados:
    - Composición: El comedor contiene otros objetos (mesa y sillas)
    - Agregación: Los objetos contenidos pueden existir independientemente
    - Encapsulación: Controla el acceso a los componentes internos
    - Abstracción: Simplifica la gestión de múltiples muebles
    """
    
    def __init__(self, nombre: str, mesa: 'Mesa', sillas: List['Silla'] = None):
        self._nombre = nombre
        self._mesa = mesa
        self._sillas = sillas if sillas is not None else []
        """
        Constructor del comedor.
        
        Args:
            nombre: Nombre del set de comedor
            mesa: Objeto Mesa que forma parte del comedor
            sillas: Lista de objetos Silla (opcional, se puede crear vacía)
        """
        #  Inicializar atributos
        # self._nombre = nombre
        # self._mesa = mesa
        # self._sillas = sillas if sillas is not None else []
        
    
    #  Implementar propiedades
    # @property
    # def nombre(self) -> str:
    #     """Getter para el nombre del comedor."""
    #     return self._nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    
    # @property
    # def mesa(self) -> 'Mesa':
    #     """Getter para la mesa del comedor."""
    #     return self._mesa
    @property
    def mesa(self) -> 'Mesa':
        return self._mesa
    
    # @property
    # def sillas(self) -> List['Silla']:
    #     """Getter para la lista de sillas."""
    #     return self._sillas.copy()  # Retorna una copia para proteger la lista interna
    def agregar_silla(self, silla: 'Silla') -> str:
        self._sillas.copy()  
        """
        Agrega una silla al comedor.
        
        Args:
            silla: Objeto Silla a agregar
            
        Returns:
            str: Mensaje de confirmación
        """
        # Implementar lógica para agregar silla
        # Validar que sea realmente una Silla
        # if not isinstance(silla, Silla):
        #     return "Error: Solo se pueden agregar objetos de tipo Silla"
    def agregar_silla(self, silla: 'Silla') -> str:
        if not isinstance(silla, Silla):
            return "Error: Solo se pueden agregar objetos de tipo Silla"
        # Verificar capacidad máxima (por ejemplo, basada en el tamaño de la mesa)
        # capacidad_maxima = self._calcular_capacidad_maxima()
        # if len(self._sillas) >= capacidad_maxima:
        #     return f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}"
        capacidad_maxima = self._calcular_capacidad_maxima()
        if len(self._sillas) >= capacidad_maxima:
            return f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}"
        # self._sillas.append(silla)
        # return f"Silla {silla.nombre} agregada exitosamente al comedor"
        self._sillas.append(silla)
        return f"Silla {silla.nombre} agregada exitosamente al comedor"

    def quitar_silla(self, indice: int = -1) -> str:
        """
        Quita una silla del comedor.
        
        Args:
            indice: Índice de la silla a quitar (-1 para la última)
            
        Returns:
            str: Mensaje de confirmación
        """
        # Implementar lógica para quitar silla
        # if not self._sillas:
        #     return "No hay sillas para quitar"
        if not self._sillas:
            return "No hay sillas para quitar"
        # try:
        try:
        #     silla_removida = self._sillas.pop(indice)
            silla_removida = self._sillas.pop(indice)

        #     return f"Silla {silla_removida.nombre} removida del comedor"
            return f"Silla {silla_removida.nombre} removida del comedor"
        # except IndexError:
        except IndexError:
        #     return "Índice de silla inválido"
            return "Índice de silla inválido"
        
    
    def calcular_precio_total(self) -> float:
        """
        Calcula el precio total del comedor sumando todos sus componentes.
        
        Returns:
            float: Precio total del set de comedor
        """
        # Implementar cálculo de precio total
        precio_total = self._mesa.calcular_precio()
        # precio_total = self._mesa.calcular_precio()
        
        # for silla in self._sillas:
        #     precio_total += silla.calcular_precio()
        for silla in self._sillas:
            precio_total += silla.calcular_precio()
        # # Aplicar descuento por set completo (5% si tiene 4 o más sillas)
        # if len(self._sillas) >= 4:
        if len(self._sillas) >= 4:
        #     precio_total *= 0.95  # 5% de descuento
            precio_total *= 0.95
        
        # return round(precio_total, 2)
        return round(precio_total, 2)
    
    def obtener_descripcion_completa(self) -> str:
        """
        Obtiene una descripción completa del comedor y todos sus componentes.
        
        Returns:
            str: Descripción detallada del comedor
        """
        # Implementar descripción completa
        descripcion = f"=== COMEDOR {self.nombre.upper()} ===\n\n"
        descripcion += "MESA:\n"
        descripcion += self._mesa.obtener_descripcion() + "\n\n"
        
        if self._sillas:
           descripcion += f"SILLAS ({len(self._sillas)} unidades):\n"
           for i, silla in enumerate(self._sillas, 1):
               descripcion += f"{i}. {silla.obtener_descripcion()}\n"
        else:
             descripcion += "SILLAS: Ninguna incluida\n"
        
        descripcion += f"\n--- PRECIO TOTAL: ${self.calcular_precio_total():.2f} ---"
        if len(self._sillas) >= 4:
          descripcion += "\n(Incluye 5% de descuento por set completo)"
          return descripcion
    
    def _calcular_capacidad_maxima(self) -> int:
        """
        Calcula la capacidad máxima de sillas basada en el tamaño de la mesa.
        Método privado auxiliar.
        
        Returns:
            int: Número máximo de sillas que pueden acomodarse
        """
        # Implementar cálculo de capacidad
        # Este cálculo depende del tamaño de la mesa
        # Asumir que la mesa tiene un atributo como 'capacidad_personas' o 'forma'
        
        # Ejemplo de lógica:
        if hasattr(self._mesa, 'capacidad_personas'):
            return self._mesa.capacidad_personas
        else:
            # Capacidad por defecto basada en el tamaño
            return 6  # Valor por defecto
    
    def obtener_resumen(self) -> dict:
        """
        Obtiene un resumen estadístico del comedor.
        
        Returns:
            dict: Diccionario con información resumida
        """
        #  Implementar resumen estadístico
        resumen = {
             "nombre": self.nombre,
             "total_muebles": 1 + len(self._sillas),  # mesa + sillas
             "precio_mesa": self._mesa.calcular_precio(),
             "precio_sillas": sum(silla.calcular_precio() for silla in self._sillas),
            "precio_total": self.calcular_precio_total(),
            "capacidad_personas": len(self._sillas),
            "materiales_utilizados": self._obtener_materiales_unicos()
         }
        return resumen
    
    def _obtener_materiales_unicos(self) -> list:
        """
        Obtiene una lista de materiales únicos usados en el comedor.
        Método privado auxiliar.
        
        Returns:
            list: Lista de materiales únicos
        """
        # Implementar obtención de materiales
        materiales = {self._mesa.material}  # Usar set para evitar duplicados
        for silla in self._sillas:
             materiales.add(silla.material)
             if hasattr(silla, 'material_tapizado') and silla.material_tapizado:
                 materiales.add(silla.material_tapizado)
        return list(materiales)

    def __str__(self) -> str:
        """Representación en cadena del comedor."""
        # Implementar representación
        return f"Comedor {self.nombre}: Mesa + {len(self._sillas)} sillas"

    
    def __len__(self) -> int:
        """Retorna el número total de muebles en el comedor."""
        # Implementar longitud
        return 1 + len(self._sillas)  # mesa + sillas
      

