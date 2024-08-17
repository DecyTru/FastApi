from sqlalchemy.orm import Session
from parking.Models import Usuario, Vehiculo, Tarifa
from parking.Schemas import UsuarioCreate, VehiculoCreate

# Funciones CRUD para Usuario
def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario( username=usuario.username, password=usuario.password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario_by_credentials(db: Session, username: str, password: str):
    return db.query(Usuario).filter(Usuario.username == username, Usuario.password == password).first()

# Funciones CRUD para Vehiculo
def create_vehiculo(db: Session, vehiculo: VehiculoCreate):
    db_vehiculo = Vehiculo(placa=vehiculo.placa, marca=vehiculo.marca, modelo=vehiculo.modelo, usuario_id=vehiculo.usuario_id)
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def get_vehiculo(db: Session, placa: str):
    return db.query(Vehiculo).filter(Vehiculo.placa == placa).first()

def delete_vehiculo(db: Session, placa: str):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.placa == placa).first()
    if db_vehiculo:
        db.delete(db_vehiculo)
        db.commit()
    return db_vehiculo

# Funciones CRUD para Tarifa
def get_tarifas(db: Session):
    return db.query(Tarifa).all()
