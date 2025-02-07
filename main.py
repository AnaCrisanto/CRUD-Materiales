"""
Este módulo contiene la configuración principal de la API
para el sistema de préstamos de materiales.
"""

from fastapi import FastAPI
from routes.usuarios import usuario
from routes.materiales import material
from routes.prestamos import prestamo

app = FastAPI(
    title="PRESTAMOS S.A. de C.V.",
    description="API de prueba para almacenar registros de préstamo de material educativo"
)

app.include_router(usuario)
app.include_router(material)
app.include_router(prestamo)
