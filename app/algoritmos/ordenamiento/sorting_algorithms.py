"""
Algoritmos de Ordenamiento con Pasos Intermedios
Proyecto EDA II - Backend
Autor: Flamenco Villaseñor Ernesto
Rama: feature/sorting-part1
"""

# ==============================================================
# BUBBLE SORT
# ==============================================================

def bubble_sort(arr: list) -> dict:
    """
    Ordena una lista usando Bubble Sort.
    Retorna el arreglo ordenado y todos los pasos intermedios.
    """
    arr = arr.copy()  # No modificamos el original
    pasos = []
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Guardamos una copia del estado actual como paso
                pasos.append({
                    "paso": len(pasos) + 1,
                    "arreglo": arr.copy(),
                    "comparando": [j, j + 1]
                })

    return {
        "algoritmo": "Bubble Sort",
        "resultado": arr,
        "total_pasos": len(pasos),
        "pasos": pasos
    }


# ==============================================================
# HEAP SORT
# ==============================================================

def _heapify(arr: list, n: int, i: int, pasos: list):
    """Función auxiliar para construir el heap."""
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq

    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        pasos.append({
            "paso": len(pasos) + 1,
            "arreglo": arr.copy(),
            "intercambio": [i, mayor]
        })
        _heapify(arr, n, mayor, pasos)


def heap_sort(arr: list) -> dict:
    """
    Ordena una lista usando Heap Sort.
    Retorna el arreglo ordenado y todos los pasos intermedios.
    """
    arr = arr.copy()
    pasos = []
    n = len(arr)

    # Construir el max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i, pasos)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        pasos.append({
            "paso": len(pasos) + 1,
            "arreglo": arr.copy(),
            "intercambio": [0, i]
        })
        _heapify(arr, i, 0, pasos)

    return {
        "algoritmo": "Heap Sort",
        "resultado": arr,
        "total_pasos": len(pasos),
        "pasos": pasos
    }


# ==============================================================
# QUICK SORT
# ==============================================================

def _partition(arr: list, bajo: int, alto: int, pasos: list) -> int:
    """Función auxiliar: divide el arreglo alrededor del pivote."""
    pivote = arr[alto]
    i = bajo - 1

    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            pasos.append({
                "paso": len(pasos) + 1,
                "arreglo": arr.copy(),
                "pivote": alto,
                "intercambio": [i, j]
            })

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    pasos.append({
        "paso": len(pasos) + 1,
        "arreglo": arr.copy(),
        "pivote_colocado": i + 1
    })
    return i + 1


def _quick_sort_recursivo(arr: list, bajo: int, alto: int, pasos: list):
    """Función recursiva interna de Quick Sort."""
    if bajo < alto:
        pi = _partition(arr, bajo, alto, pasos)
        _quick_sort_recursivo(arr, bajo, pi - 1, pasos)
        _quick_sort_recursivo(arr, pi + 1, alto, pasos)


def quick_sort(arr: list) -> dict:
    """
    Ordena una lista usando Quick Sort.
    Retorna el arreglo ordenado y todos los pasos intermedios.
    """
    arr = arr.copy()
    pasos = []
    _quick_sort_recursivo(arr, 0, len(arr) - 1, pasos)

    return {
        "algoritmo": "Quick Sort",
        "resultado": arr,
        "total_pasos": len(pasos),
        "pasos": pasos
    }
