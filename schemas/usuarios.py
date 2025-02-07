"""
Este módulo contiene los esquemas para los usuarios en el sistema,
incluyendo las operaciones CRUD y las validaciones de datos necesarias.
"""

from datetime import datetime
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    """
    Esquema base para los usuarios, contiene los atributos comunes
    que todos los usuarios deben tener.
    """
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: str
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: str
    fechaRegistro: datetime
    fechaActualizacion: datetime


class UsuarioCreate(UsuarioBase):
    """
    Esquema utilizado para crear un nuevo usuario.
    """

class UsuarioUpdate(UsuarioBase):
    """
    Esquema utilizado para actualizar un usuario existente.
    """

class Usuario(UsuarioBase):
    """
    Esquema que representa un usuario completo, incluyendo su ID.
    """
    id: int

    class Config:
        """
        Configuración de la clase Usuario para permitir la conversión
        de atributos de la base de datos.
        """
        from_attributes = True
