"""Este módulo contiene las definiciones del modelo de usuario,
incluyendo los tipos y estatus asociados a un usuario en el sistema."""

import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base

class TipoUsuario(str, enum.Enum):
    """Enum que representa los diferentes tipos de usuario."""
    ALUMNO = "ALUMNO"
    PROFESOR = "PROFESOR"
    SECRETARIA = "SECRETARIA"
    LABORATORISTA = "LABORATORISTA"
    DIRECTIVO = "DIRECTIVO"
    ADMINISTRATIVO = "ADMINISTRATIVO"

class Estatus(str, enum.Enum):
    """Enum que representa los diferentes estatus de un usuario."""
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    BLOQUEADO = "BLOQUEADO"
    SUSPENDIDO = "SUSPENDIDO"

class Usuario(Base):
    """Representa los usuarios registrados en el sistema."""
    __tablename__ = "tbb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60))
    correoElectronico = Column(String(100))
    contrasena = Column(String(60))
    numeroTelefono = Column(String(20))
    estatus = Column(Enum(Estatus))
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)

    def __repr__(self):
        return (
            f"Usuario(id={self.id}, nombre={self.nombre}, "
            f"tipoUsuario={self.tipoUsuario}, estatus={self.estatus})"
        )

    # Método para asegurarse que el tipoUsuario siempre se guarda en mayúsculas
    @classmethod
    def validate_tipo_usuario(cls, tipo_usuario: str):
        """Asegura que tipoUsuario esté en mayúsculas."""
        return tipo_usuario.upper()
