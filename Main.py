from fastapi import FastAPI
from parking.Routes import router as parking_router
from parking.Database import Base, engine

app = FastAPI()

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir el enrutador de parking
app.include_router(parking_router, prefix="/api/v1", tags=["Parking"])

# Ruta raíz que devuelve un mensaje de bienvenida
@app.get("/", tags=["Root"])
def read_root():
    return {"mensaje": "¡Bienvenido a la API de Gestión de Parqueo! Consulta la documentación en /docs para ver los endpoints disponibles."}
