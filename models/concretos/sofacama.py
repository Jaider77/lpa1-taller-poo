"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

# TODO: Importar las clases padre
# from .sofa import Sofa
# from .cama import Cama
from .sofa import Sofa
from .cama import Cama

class SofaCama:
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    
    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        super().__init__(nombre, material, color, precio_base, capacidad_personas, True, material_tapizado)
        self._tamaño_cama = tamaño_cama
        self._incluye_colchon = incluye_colchon
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"  # Puede ser "sofa" o

        """
        Constructor del sofá-cama.
        
        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """
        # Inicializar usando las clases padre
        # Nota: En herencia múltiple, solo se llama super().__init__ una vez
        # Esto llama al primer padre en el MRO (Method Resolution Order)
        # super().__init__(nombre, material, color, precio_base, capacidad_personas, True, material_tapizado)
        
        # Inicializar atributos específicos de cama
        # Necesitamos configurar manualmente los atributos de Cama ya que solo se llama un __init__
        # self._tamaño_cama = tamaño_cama
        # self._incluye_colchon = incluye_colchon
        
        # Inicializar atributos únicos del sofá-cama
        # self._mecanismo_conversion = mecanismo_conversion
        # self._modo_actual = "sofa"  # Puede ser "sofa" o "cama"
    
    # Implementar propiedades para los nuevos atributos
    # @property
    # def mecanismo_conversion(self) -> str:
    #     """Getter para el mecanismo de conversión."""
    #     return self._mecanismo_conversion
    @property
    def mecanismo_conversion(self) -> str:
        return self._mecanismo_conversion
    @property
    def modo_actual(self) -> str:
        return self._modo_actual
    @property
    def tamaño_cama(self) -> str:
        return self._tamaño_cama
    @property
    def incluye_colchon(self) -> bool:
        return self._incluye_colchon
    

    # @property
    # def modo_actual(self) -> str:
    #     """Getter para el modo actual (sofa o cama)."""
    #     return self._modo_actual
    
    def convertir_a_cama(self) -> str:
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"
        
        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"
    
        # Implementar lógica de conversión
        # if self._modo_actual == "cama":
        #     return "El sofá-cama ya está en modo cama"
        
        # self._modo_actual = "cama"
        # return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"
    
    def convertir_a_sofa(self) -> str:
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"
        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
        # Implementar lógica de conversión
        # if self._modo_actual == "sofa":
        #     return "El sofá-cama ya está en modo sofá"
        
        # self._modo_actual = "sofa"
        # return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
         # Implementar cálculo de precio combinado
        # El sofá-cama es más caro que un sofá o cama individual
        # 1. Comenzar con precio base
        # precio = self.precio_base
        
        # 2. Aplicar factor de comodidad de asiento
        # precio *= self.calcular_factor_comodidad()
        
        # 3. Agregar valor por funcionalidad dual
        # precio *= 1.5  # 50% más caro por ser dual
        
        # 4. Agregar costo por mecanismo de conversión
        # if self.mecanismo_conversion == "electrico":
        #     precio += 200
        # elif self.mecanismo_conversion == "hidraulico":
        #     precio += 150
        # else:  # manual/plegable
        #     precio += 100
        
        # 5. Agregar costo si incluye colchón
        # if self.incluye_colchon:
        #     precio += 300
        
        # return round(precio, 2)


    def calcular_precio(self) -> float:
        precio = self.precio_base
        precio += self.calcular_factor_comodidad() * 30
        precio *= 1.5  # 50% más caro por ser dual
        if self.mecanismo_conversion == "electrico":
            precio += 200
        elif self.mecanismo_conversion == "hidraulico":
            precio += 150
        else:  # manual/plegable
            precio += 100
        if self.incluye_colchon:
            precio += 300
        return round(precio, 2)
       
    
    def obtener_descripcion(self) -> str:
        descripcion = f"Sofá-cama '{self.nombre}' fabricado en {self.material} color {self.color}."
        descripcion += f"\nCapacidad como sofá: {self.capacidad_personas} personas"
        descripcion += f"\nTapizado: {self.material_tapizado}"
        descripcion += f"\nTamaño de cama: {self.tamaño_cama}"
        descripcion += f"\nMecanismo de conversión: {self.mecanismo_conversion}"
        descripcion += f"\nColchón incluido: {'Sí' if self.incluye_colchon else 'No'}"
        descripcion += f"\nModo actual: {self.modo_actual}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion
    
        #  Crear descripción combinada
        # descripcion = f"Sofá-cama {self.nombre} fabricado en {self.material} color {self.color}."
        # descripcion += f"\n{self.obtener_info_asiento()}"
        # descripcion += f"\nTamaño de cama: {self.tamaño_cama}"
        # descripcion += f"\nMecanismo de conversión: {self.mecanismo_conversion}"
        # descripcion += f"\nColchón incluido: {'Sí' if self.incluye_colchon else 'No'}"
        # descripcion += f"\nModo actual: {self.modo_actual}"
        # descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        # return descripcion
        
        #  Implementar capacidades
        # capacidades = {
        #     "como_sofa": self.capacidad_personas,
        #     "como_cama": 2 if self.tamaño_cama in ["matrimonial", "queen", "king"] else 1
        # }
        # return capacidades
    
    def obtener_capacidad_total(self) -> dict:
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2 if self.tamaño_cama in ["matrimonial", "queen", "king"] else 1
        }
        return capacidades
        
    
    #  Implementar método para verificar compatibilidad de modo
    # def puede_usar_como_cama(self) -> bool:
    #     """Verifica si actualmente puede usarse como cama."""
    #     return self._modo_actual == "cama"
    def puede_usar_como_cama(self) -> bool: 
        """Verifica si actualmente puede usarse como cama."""
        return self._modo_actual == "cama"
    
    # def puede_usar_como_sofa(self) -> bool:
    #     """Verifica si actualmente puede usarse como sofá."""
    #     return self._modo_actual == "sofa"
    def puede_usar_como_sofa(self) -> bool:
        """Verifica si actualmente puede usarse como sofá."""
        return self._modo_actual == "sofa"
    
    def __str__(self) -> str:
        return f"Sofá-cama '{self.nombre}' en modo {self.modo_actual}"
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        # Implementar representación personalizada
        # return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
        

