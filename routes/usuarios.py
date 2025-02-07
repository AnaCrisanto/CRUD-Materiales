"""Este módulo contiene las rutas relacionadas con los usuarios
y las operaciones CRUD asociadas a ellos en la API."""

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.usuarios
import config.db
import schemas.usuarios
import models.usuarios

usuario = APIRouter()

models.usuarios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """
    Crea una sesión de base de datos para ser utilizada en las operaciones.
    """
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usuario.get("/usuarios/", response_model=List[schemas.usuarios.Usuario], tags=["Usuarios"])
async def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de usuarios con paginación.
    """
    db_usuarios = crud.usuarios.obtener_usuarios(db=db, skip=skip, limit=limit)
    return db_usuarios

@usuario.post("/usuario/", response_model=schemas.usuarios.Usuario, tags=["Usuarios"])
async def create_usuario(usuario_data: schemas.usuarios.UsuarioCreate,
                         db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario.
    """
    try:
        db_usuario = crud.usuarios.crear_usuario(db=db, usuario=usuario_data)
        return db_usuario
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@usuario.get("/usuario/{usuario_id}", response_model=schemas.usuarios.Usuario, tags=["Usuarios"])
async def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un usuario específico por su ID.
    """
    db_usuario = crud.usuarios.obtener_usuario(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@usuario.put("/usuario/{usuario_id}", response_model
             =schemas.usuarios.Usuario, tags=["Usuarios"])
async def update_usuario(usuario_id: int, usuario_data:
    schemas.usuarios.UsuarioUpdate, db: Session = Depends(get_db)):
    """
    Actualiza un usuario existente.
    """
    db_usuario = crud.usuarios.actualizar_usuario(db=db,
                                                  usuario_id
                                                  =usuario_id,
                                                  usuario=
                                                  usuario_data)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@usuario.delete("/usuario/{usuario_id}", response_model=schemas.usuarios.Usuario, tags=["Usuarios"])
async def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario por su ID.
    """
    db_usuario = crud.usuarios.eliminar_usuario(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario
