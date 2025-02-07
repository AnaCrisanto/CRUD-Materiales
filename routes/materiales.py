"""Este módulo contiene las rutas relacionadas con los materiales
y las operaciones CRUD asociadas a ellos en la API."""

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.materiales
import models.materiales
import config.db
import schemas.materiales

material = APIRouter()

# Crea todas las tablas en la base de datos, si no existen
models.materiales.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """
    Crea una sesión de base de datos para ser utilizada en las operaciones.
    """
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material.get("/materials", response_model=List[schemas.materiales.Material], tags=["Materiales"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de materiales con paginación.
    """
    return crud.materiales.get_materials(db=db, skip=skip, limit=limit)

@material.get("/materials/{material_id}", response_model
              =schemas.materiales.Material, tags=["Materiales"])
async def read_material(material_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un material específico por su ID.
    """
    db_material = crud.materiales.get_material(db=db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.post("/materials", response_model
               =schemas.materiales.Material, tags=["Materiales"])
async def create_material(material_data: schemas.materiales.MaterialCreate, db: Session
                          = Depends(get_db)):
    """
    Crea un nuevo material en el sistema.
    """
    return crud.materiales.create_material(db=db, material=material_data)

@material.put("/materials/{material_id}", response_model
              =schemas.materiales.Material, tags
              =["Materiales"])
async def update_material(material_id: int, material_data:
    schemas.materiales.MaterialUpdate, db: Session
                          = Depends(get_db)):
    """
    Actualiza un material existente.
    """
    db_material = crud.materiales.update_material(db=db, material_id
                                                  =material_id, material=material_data)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.delete("/materials/{material_id}", response_model
                 =schemas.materiales.Material, tags=["Materiales"])
async def delete_material(material_id: int, db: Session = Depends(get_db)):
    """
    Elimina un material por su ID.
    """
    db_material = crud.materiales.delete_material(db=db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
