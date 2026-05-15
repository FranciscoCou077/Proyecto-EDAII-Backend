from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import graphs, sorting, searching
from app.database import engine
from app.models import Base
from app.algoritmos.ordenamiento.sorting_router import router as sorting_part1_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Backend - Estructura de Datos y Algoritmos II",
    description="Motor algorítmico para evaluación, consulta y ejecución de algoritmos.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "estado": "En línea",
        "mensaje": "Bienvenido al motor Backend de EDA II",
        "equipo": "Backend"
    }

app.include_router(sorting.router, prefix="/api/sorting", tags=["Ordenamiento"])
app.include_router(graphs.router,  prefix="/api/graphs",  tags=["Grafos"])
app.include_router(searching.router, prefix="/api/searching", tags=["Busqueda"])
app.include_router(sorting_part1_router, prefix="/api/sorting", tags=["Ordenamiento"])
app.include_router(graphs.router, prefix="/api/graphs", tags=["Grafos"])

