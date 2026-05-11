"""
Endpoints de la API para Algoritmos de Ordenamiento
Proyecto EDA II - Backend
Autor: Flamenco Villaseñor Ernesto

Endpoints expuestos:
    POST /api/sorting/bubble-sort
    POST /api/sorting/heap-sort
    POST /api/sorting/quick-sort
"""

from fastapi import APIRouter
from sorting_schemas import SortingInput, SortingOutput
from sorting_algorithms import bubble_sort, heap_sort, quick_sort

# Creamos el router (el "módulo" de rutas para sorting)
router = APIRouter(
    prefix="/api/sorting",
    tags=["Sorting Algorithms"]
)


# ==============================================================
# ENDPOINT: Bubble Sort
# ==============================================================

@router.post(
    "/bubble-sort",
    response_model=SortingOutput,
    summary="Ordenar con Bubble Sort",
    description="Recibe un arreglo de enteros y lo ordena usando Bubble Sort. Devuelve el resultado y todos los pasos intermedios."
)
def endpoint_bubble_sort(data: SortingInput):
    resultado = bubble_sort(data.arreglo)
    return resultado


# ==============================================================
# ENDPOINT: Heap Sort
# ==============================================================

@router.post(
    "/heap-sort",
    response_model=SortingOutput,
    summary="Ordenar con Heap Sort",
    description="Recibe un arreglo de enteros y lo ordena usando Heap Sort. Devuelve el resultado y todos los pasos intermedios."
)
def endpoint_heap_sort(data: SortingInput):
    resultado = heap_sort(data.arreglo)
    return resultado


# ==============================================================
# ENDPOINT: Quick Sort
# ==============================================================

@router.post(
    "/quick-sort",
    response_model=SortingOutput,
    summary="Ordenar con Quick Sort",
    description="Recibe un arreglo de enteros y lo ordena usando Quick Sort. Devuelve el resultado y todos los pasos intermedios."
    )
def endpoint_quick_sort(data: SortingInput):
    resultado = quick_sort(data.arreglo)
    return resultado
