"""
Schemas de Entrada y Salida para los Endpoints de Sorting
Proyecto EDA II - Backend
Autor: Flamenco Villaseñor Ernesto
"""

from pydantic import BaseModel, Field
from typing import List, Optional


# ==============================================================
# SCHEMAS DE ENTRADA (lo que recibe la API)
# ==============================================================

class SortingInput(BaseModel):
    """
    Schema de entrada común para todos los algoritmos de ordenamiento.
    El cliente manda un arreglo de números enteros.
    """
    arreglo: List[int] = Field(
        ...,
        description="Lista de números enteros a ordenar",
        example=[64, 34, 25, 12, 22, 11, 90]
    )

    class Config:
        json_schema_extra = {
            "example": {
                "arreglo": [64, 34, 25, 12, 22, 11, 90]
            }
        }


# ==============================================================
# SCHEMAS DE SALIDA (lo que devuelve la API)
# ==============================================================

class Paso(BaseModel):
    """Representa un paso intermedio durante el ordenamiento."""
    paso: int = Field(..., description="Número de paso")
    arreglo: List[int] = Field(..., description="Estado del arreglo en este paso")
    comparando: Optional[List[int]] = Field(None, description="Índices que se están comparando (Bubble Sort)")
    intercambio: Optional[List[int]] = Field(None, description="Índices que se intercambiaron (Heap/Quick Sort)")
    pivote: Optional[int] = Field(None, description="Índice del pivote actual (Quick Sort)")
    pivote_colocado: Optional[int] = Field(None, description="Índice donde quedó el pivote (Quick Sort)")


class SortingOutput(BaseModel):
    """
    Schema de salida común para todos los algoritmos de ordenamiento.
    Devuelve el resultado final y todos los pasos intermedios.
    """
    algoritmo: str = Field(..., description="Nombre del algoritmo usado")
    resultado: List[int] = Field(..., description="Arreglo completamente ordenado")
    total_pasos: int = Field(..., description="Número total de pasos realizados")
    pasos: List[Paso] = Field(..., description="Lista de todos los pasos intermedios")

    class Config:
        json_schema_extra = {
            "example": {
                "algoritmo": "Bubble Sort",
                "resultado": [11, 12, 22, 25, 34, 64, 90],
                "total_pasos": 6,
                "pasos": [
                    {
                        "paso": 1,
                        "arreglo": [34, 64, 25, 12, 22, 11, 90],
                        "comparando": [0, 1]
                    }
                ]
            }
        }
