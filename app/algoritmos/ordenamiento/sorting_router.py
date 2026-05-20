from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.algoritmos.ordenamiento.sorting_algorithms import (
    bubble_sort, heap_sort, quick_sort
)

router = APIRouter(tags=["Ordenamiento"])

class SortingInput(BaseModel):
    arreglo: List[int]

@router.post("/bubble-sort")
def endpoint_bubble_sort(data: SortingInput):
    return bubble_sort(data.arreglo)

@router.post("/heap-sort")
def endpoint_heap_sort(data: SortingInput):
    return heap_sort(data.arreglo)

@router.post("/quick-sort")
def endpoint_quick_sort(data: SortingInput):
    return quick_sort(data.arreglo)