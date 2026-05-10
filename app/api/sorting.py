from fastapi import APIRouter
from pydantic import BaseModel
import time

from app.algoritmos.ordenamiento.counting_sort import counting_sort
from app.algoritmos.ordenamiento.radix_sort    import radix_sort
from app.algoritmos.ordenamiento.merge_sort     import merge_sort_completo

router = APIRouter()

class ArrayInput(BaseModel):
    array: list[int]

# -------------------------------------------------------
@router.post("/counting-sort")
def ejecutar_counting_sort(data: ArrayInput):
    return counting_sort(data.array)

# -------------------------------------------------------
@router.post("/radix-sort")
def ejecutar_radix_sort(data: ArrayInput):
    return radix_sort(data.array)

# -------------------------------------------------------
@router.post("/merge-sort")
def ejecutar_merge_sort(data: ArrayInput):
    return merge_sort_completo(data.array)

# -------------------------------------------------------
@router.get("/compare")
def comparar_algoritmos(array: str = "5,3,8,1,9,2,7,4,6"):
    """
    Corre todos los algoritmos con el mismo arreglo y
    devuelve comparativa de tiempo y complejidad.
    """
    arr = [int(x) for x in array.split(",")]

    resultados = {}
    algoritmos = {
        "counting_sort": counting_sort,
        "radix_sort":    radix_sort,
        "merge_sort":    merge_sort_completo,
    }

    for nombre, func in algoritmos.items():
        inicio = time.perf_counter()
        resultado = func(arr)
        fin = time.perf_counter()

        resultados[nombre] = {
            "sorted_array": resultado["sorted_array"],
            "comparisons":  resultado["comparisons"],
            "time_ms":      round((fin - inicio) * 1000, 4),
            "complexity":   resultado["complexity"]
        }

    return {
        "array_original": arr,
        "resultados": resultados
    }