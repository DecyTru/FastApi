from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import Generator

# Cambia la URL de conexión a MySQL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost/ParkingLotDB"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear el localizador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base declarativa
Base = declarative_base()

# Función para obtener la base de datos
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
