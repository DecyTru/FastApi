from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from parking import Crud, Schemas
from parking.Database import get_db

router = APIRouter()

@router.post("/Registro/", response_model=Schemas.UsuarioResponseFull)
def create_usuario(usuario: Schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return Crud.create_usuario(db, usuario)

@router.get("/InicioSession/", response_model=Schemas.UsuarioResponseFull)
def read_usuario(username: str, password: str, db: Session = Depends(get_db)):
    db_usuario = Crud.get_usuario_by_credentials(db, username, password)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@router.post("/CrearVehiculos/", response_model=Schemas.VehiculoResponse)
def create_vehiculo(vehiculo: Schemas.VehiculoCreate, db: Session = Depends(get_db)):
    return Crud.create_vehiculo(db, vehiculo)

@router.get("/MostrarVehiculos/{placa}", response_model=Schemas.VehiculoResponse)
def read_vehiculo(placa: str, db: Session = Depends(get_db)):
    db_vehiculo = Crud.get_vehiculo(db, placa)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo not found")
    return db_vehiculo

@router.delete("/BorrarVehiculos/{placa}", response_model=Schemas.VehiculoResponse)
def delete_vehiculo(placa: str, db: Session = Depends(get_db)):
    db_vehiculo = Crud.delete_vehiculo(db, placa)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo not found")
    return db_vehiculo

@router.get("/tarifas/", response_model=list[Schemas.TarifaResponse])
def read_tarifas(db: Session = Depends(get_db)):
    return Crud.get_tarifas(db)
