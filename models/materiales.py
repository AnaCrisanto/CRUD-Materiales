"""Este módulo contiene las clases y enumeraciones para el modelo de Material."""

import enum
from sqlalchemy import Column, Integer, String, Enum
from config.db import Base

class TipoMaterial(str, enum.Enum):
    """Enum que representa los tipos de material disponibles."""
    CANON = "Cañon"
    COMPUTADORA = "Computadora"
    EXTENSION = "Extension"

class Estatus(str, enum.Enum):
    """Enum que representa el estatus del material disponible."""
    DISPONIBLE = "Disponible"
    PRESTADO = "Prestado"
    EN_MANTENIMIENTO = "En Mantenimiento"

    @classmethod
    def example_method(cls):
        """Método de ejemplo que no realiza ninguna acción."""

    @classmethod
    def obtener_estatus_lista(cls):
        """Devuelve una lista de todos los estatus disponibles."""
        return list(cls)

class Material(Base):
    """Columnas de la tabla material."""
    __tablename__ = "tbb_Material"

    id = Column(Integer, primary_key=True, autoincrement=True)
    TipoMaterial = Column(Enum(TipoMaterial))
    Marca = Column(String(60))
    Modelo = Column(String(100))
    Estado = Column(Enum(Estatus))

    def __repr__(self):
        return (
            f"Material(id={self.id}, "
            f"TipoMaterial={self.TipoMaterial}, "
            f"Marca={self.Marca}, "
            f"Modelo={self.Modelo}, "
            f"Estado={self.Estado})"
        )

    def es_material_disponible(self):
        """Verifica si el material está disponible."""
        return self.Estado == Estatus.DISPONIBLE

def __repr__(self):
    return (
        f"Material(id={self.id}, "
        f"TipoMaterial={self.TipoMaterial}, "
        f"Marca={self.Marca}, "
        f"Modelo={self.Modelo}, "
        f"Estado={self.Estado})"
    )
