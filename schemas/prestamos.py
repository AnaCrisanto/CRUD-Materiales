"""
Este módulo contiene los esquemas necesarios para el manejo de los préstamos
en el sistema, incluyendo las operaciones CRUD y las validaciones de datos.
"""

from datetime import datetime
from pydantic import BaseModel

class PrestamoBase(BaseModel):
    """
    Esquema base para los préstamos, contiene los atributos comunes
    que todos los préstamos deben tener.

    Atributos:
        id_usuario: El ID del usuario que realiza el préstamo.
        id_material: El ID del material prestado.
        fecha_prestamo: La fecha en que se realiza el préstamo.
        fecha_devolucion: La fecha de devolución del material.
        estatus: El estado actual del préstamo (ej. 'activo', 'devuelto').
    """
    id_usuario: str
    id_material: str
    fecha_prestamo: datetime
    fecha_devolucion: datetime
    estatus: str

class PrestamoCreate(PrestamoBase):
    """
    Esquema utilizado para crear un nuevo préstamo.

    Hereda de PrestamoBase, pero no agrega campos adicionales.
    """

class PrestamoUpdate(PrestamoBase):
    """
    Esquema utilizado para actualizar un préstamo existente.

    Hereda de PrestamoBase, pero no agrega campos adicionales.
    """

class Prestamo(PrestamoBase):
    """
    Esquema que representa un préstamo completo, incluyendo su ID.

    Hereda de PrestamoBase y agrega el campo `id_prestamo`, necesario
    para identificar de manera única a cada préstamo en la base de datos.

    Atributos:
        id_prestamo: El identificador único del préstamo.
    """
    id_prestamo: int

    class Config:
        """
        Configuración de la clase Prestamo para permitir la conversión
        de atributos de la base de datos.
        """
        from_attributes = True

    def metodo_ejemplo(self):
        """
        Método de ejemplo para evitar la advertencia de "demasiados pocos métodos públicos".
        """
        return self.id_prestamo
