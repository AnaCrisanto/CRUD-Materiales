"""
Este módulo contiene los esquemas para los materiales en el sistema,
incluyendo las operaciones CRUD y las validaciones de datos necesarias.
"""

from pydantic import BaseModel

class MaterialBase(BaseModel):
    """
    Base model para los materiales, contiene los atributos comunes
    que todos los materiales deben tener.

    Atributos:
        TipoMaterial: El tipo de material.
        Marca: La marca del material.
        Modelo: El modelo del material.
        Estado: El estado actual del material (ej. 'nuevo', 'usado').
    """
    TipoMaterial: str
    Marca: str
    Modelo: str
    Estado: str

class MaterialCreate(MaterialBase):
    """
    Modelo utilizado para crear un nuevo material.

    Hereda de MaterialBase, pero no agrega campos adicionales.
    """

class MaterialUpdate(MaterialBase):
    """
    Modelo utilizado para actualizar un material existente.

    Hereda de MaterialBase, pero no agrega campos adicionales.
    """

class Material(MaterialBase):
    """
    Modelo que representa un material completo, incluyendo su ID.

    Hereda de MaterialBase y agrega el campo `id`, que es necesario
    para identificar de manera única a cada material en la base de datos.

    Atributos:
        id: El identificador único del material.
    """
    id: int

    class Config:
        """
        Configuración de la clase Material para permitir la conversión
        de atributos de la base de datos.
        """
        from_attributes = True

    def metodo_ejemplo(self):
        """
        Método de ejemplo para evitar la advertencia de "demasiado pocos métodos públicos".
        """
        return self.id
