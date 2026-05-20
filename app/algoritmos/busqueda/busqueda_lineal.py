def busqueda_lineal(array, objetivo):
    comparaciones = 0

    for i, valor in enumerate(array):
        comparaciones += 1
        if valor == objetivo:
            return {
                "found": True,
                "index": i,
                "comparisons": comparaciones,
                "complexity": "O(n)"
            }

    return {
        "found": False,
        "index": -1,
        "comparisons": comparaciones,
        "complexity": "O(n)"
    }