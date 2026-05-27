from fastapi import APIRouter
from pydantic import BaseModel

from app.algoritmos.busqueda.busqueda_lineal import busqueda_lineal
from app.algoritmos.busqueda.busqueda_binaria import busqueda_binaria
from app.algoritmos.busqueda.hash import busqueda_hash

router = APIRouter()

class SearchInput(BaseModel):
    array: list[int]
    target: int


@router.post("/linear")
def ejecutar_busqueda_lineal(data: SearchInput):
    return busqueda_lineal(data.array, data.target)


@router.post("/binary")
def ejecutar_busqueda_binaria(data: SearchInput):
    return busqueda_binaria(data.array, data.target)


@router.post("/hash")
def ejecutar_busqueda_hash(data: SearchInput):
    return busqueda_hash(data.array, data.target)