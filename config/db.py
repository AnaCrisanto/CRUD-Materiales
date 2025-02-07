# config/db.py
"""
Este archivo contiene la configuración de la base de datos utilizando SQLAlchemy.
Incluye la configuración de la URL de la base de datos, el motor de conexión,
la creación de sesiones y la base de datos declarativa.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("La URL de la base de datos no está definida en las variables de entorno.")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
