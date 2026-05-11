def merge_sort(arr: list[int], steps: list = None, comparisons: list = None) -> list[int]:
    if steps is None:
        steps = []
    if comparisons is None:
        comparisons = [0]

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid], steps, comparisons)
    derecha   = merge_sort(arr[mid:], steps, comparisons)

    return _merge(izquierda, derecha, steps, comparisons)


def _merge(izquierda: list, derecha: list, steps: list, comparisons: list) -> list:
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        comparisons[0] += 1
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    steps.append({
        "array": resultado.copy(),
        "izquierda": izquierda,
        "derecha": derecha,
        "descripcion": f"Merge de {izquierda} y {derecha}"
    })

    return resultado


def merge_sort_completo(arr: list[int]) -> dict:
    if not arr:
        return {"sorted_array": [], "steps": [], "comparisons": 0,
                "complexity": {"best": "O(n log n)", "average": "O(n log n)",
                               "worst": "O(n log n)", "space": "O(n)"}}

    arr = arr.copy()
    steps = [{"array": arr.copy(), "descripcion": "Array inicial"}]
    comparisons = [0]

    sorted_arr = merge_sort(arr, steps, comparisons)

    return {
        "sorted_array": sorted_arr,
        "steps": steps,
        "comparisons": comparisons[0],
        "complexity": {
            "best": "O(n log n)",
            "average": "O(n log n)",
            "worst": "O(n log n)",
            "space": "O(n)"
        }
    }