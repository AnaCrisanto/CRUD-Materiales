"""#Este módulo contiene funciones CRUD para la entidad 'Prestamos'."""
from sqlalchemy.orm import Session
import models.prestamos
import schemas.prestamos

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    """Ver los préstamo en la base de datos."""
    return db.query(models.prestamos.Prestamo).offset(skip).limit(limit).all()

def get_prestamo(db: Session, id_prestamo: int):
    """Ver un nuevo préstamo por id en la base de datos."""
    return db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id_prestamo
                                                      == id_prestamo).first()

def create_prestamo(db: Session, prestamo: schemas.prestamos.PrestamoCreate):
    """Crea un nuevo préstamo en la base de datos."""
    db_prestamo = models.prestamos.Prestamo(
        id_usuario=prestamo.id_usuario,
        id_material=prestamo.id_material,
        fecha_prestamo=prestamo.fecha_prestamo,
        fecha_devolucion=prestamo.fecha_devolucion,
        estatus=prestamo.estatus
    )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, id_prestamo: int, prestamo: schemas.prestamos.PrestamoUpdate):
    """Actualiza un préstamo en la base de datos."""
    db_prestamo = db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id_prestamo
                                                             == id_prestamo).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            if value is not None:
                setattr(db_prestamo, var, value)
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id_prestamo: int):
    """Eliminar un préstamo en la base de datos."""
    db_prestamo = db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id_prestamo
                                                             == id_prestamo).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
