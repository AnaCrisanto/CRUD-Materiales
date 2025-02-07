"""Este módulo contiene las definiciones de la
tabla de préstamos y sus estatus en la base de datos."""

import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base

class EstatusPrestamo(str, enum.Enum):
    """Enum que representa los estatus de un préstamo."""
    ACTIVO = "Activo"
    DEVUELTO = "Devuelto"
    VENCIDO = "Vencido"

class Prestamo(Base):
    """Modelo que representa los préstamos de materiales en la base de datos."""
    __tablename__ = "tbb_prestamos"

    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(String(50))
    id_material = Column(String(50))
    fecha_prestamo = Column(DateTime)
    fecha_devolucion = Column(DateTime, nullable=True)
    estatus = Column(Enum(EstatusPrestamo))

    def esta_vencido(self):
        """Verifica si el préstamo ha vencido."""
        if self.fecha_devolucion and self.fecha_devolucion < datetime.now():
            self.estatus = EstatusPrestamo.VENCIDO
            return True
        return False

    def dias_restantes(self):
        """Devuelve los días restantes para la devolución del material."""
        if self.fecha_devolucion:
            delta = self.fecha_devolucion - datetime.now()
            return delta.days
        return None

    def actualizar_estatus(self):
        """Actualiza el estatus del préstamo basado en la fecha de devolución."""
        if self.esta_vencido():
            self.estatus = EstatusPrestamo.VENCIDO
        elif self.fecha_devolucion:
            self.estatus = EstatusPrestamo.DEVUELTO
        else:
            self.estatus = EstatusPrestamo.ACTIVO
