"""#Este módulo contiene funciones CRUD para la entidad 'Material'."""
from sqlalchemy.orm import Session
import models.materiales
import schemas.materiales

def get_material(db: Session, material_id: int):
    """Obtiene un material específico desde la base de datos por su ID."""
    return db.query(models.materiales.Material).filter(models.materiales.Material.id
                                                       == material_id).first()

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista de materiales desde la base de datos."""
    return db.query(models.materiales.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.materiales.MaterialCreate):
    """Crea un nuevo material en la base de datos."""
    db_material = models.materiales.Material(
        TipoMaterial=material.TipoMaterial,
        Marca=material.Marca,
        Modelo=material.Modelo,
        Estado=material.Estado
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, material_id: int, material: schemas.materiales.MaterialUpdate):
    """Actualiza los datos de un material existente en la base de datos."""
    db_material = db.query(models.materiales.Material).filter(models.materiales.Material.id
                                                              == material_id).first()
    if db_material:
        for var, value in vars(material).items():
            if value is not None:
                setattr(db_material, var, value)
        db.commit()
        db.refresh(db_material)
    return db_material
def delete_material(db: Session, material_id: int):
    """Elimina un material por su ID."""
    db_material = db.query(models.materiales.Material).filter(models.materiales.Material.id
                                                              == material_id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
