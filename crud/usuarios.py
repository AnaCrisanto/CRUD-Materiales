"""#Este módulo contiene funciones CRUD para la entidad 'Usuarios'."""
from sqlalchemy.orm import Session
import models.usuarios
import schemas.usuarios

def obtener_usuarios(db: Session, skip: int = 0, limit: int = 10):
    """Ver los usuarios en la base de datos."""
    return db.query(models.usuarios.Usuario).offset(skip).limit(limit).all()

def obtener_usuario_por_nombre(db: Session, nombre: str):
    """Ver los usuarios por nombre en la base de datos."""
    return db.query(models.usuarios.Usuario).filter(models.usuarios.Usuario.
                                                    nombreUsuario
                                                    == nombre).first()

def obtener_usuario(db: Session, usuario_id: int):
    """Ver los usuarios en la base de datos."""
    return db.query(models.usuarios.Usuario).filter(models.usuarios.Usuario.
                                                    id == usuario_id).first()

def crear_usuario(db: Session, usuario: schemas.usuarios.UsuarioCreate):
    """Crear los usuarios en la base de datos."""
    db_usuario = obtener_usuario_por_nombre(db, usuario.nombreUsuario)
    if db_usuario:
        raise ValueError("El nombre de usuario ya está registrado.")
    db_usuario_correo = db.query(models.usuarios.Usuario).filter(models.
                                                                 usuarios.
                                                                 Usuario.
                                                                 correoElectronico
                                                                 ==
                                                                 usuario.
                                                                 correoElectronico).first()
    if db_usuario_correo:
        raise ValueError("El correo electrónico ya está registrado.")

    # Crear el nuevo usuario
    db_usuario = models.usuarios.Usuario(
        nombre=usuario.nombre,
        primerApellido=usuario.primerApellido,
        segundoApellido=usuario.segundoApellido,
        tipoUsuario=usuario.tipoUsuario,
        nombreUsuario=usuario.nombreUsuario,
        correoElectronico=usuario.correoElectronico,
        contrasena=usuario.contrasena,
        numeroTelefono=usuario.numeroTelefono,
        estatus=usuario.estatus,
        fechaRegistro=usuario.fechaRegistro,
        fechaActualizacion=usuario.fechaActualizacion
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def actualizar_usuario(db: Session, usuario_id: int, usuario:
    schemas.usuarios.UsuarioUpdate):
    """Actualizar los usuarios en la base de datos."""
    db_usuario = db.query(models.usuarios.Usuario).filter(models.usuarios.Usuario.
                                                          id == usuario_id).first()

    if db_usuario:
        for var, value in vars(usuario).items():
            if value is not None:
                setattr(db_usuario, var, value)
        db.commit()
        db.refresh(db_usuario)

    return db_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    """Eliminar los usuarios en la base de datos."""
    db_usuario = db.query(models.usuarios.Usuario).filter(models.
                                                          usuarios.Usuario.
                                                          id ==
                                                          usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
