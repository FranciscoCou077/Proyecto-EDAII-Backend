def busqueda_binaria(array, objetivo):
    izquierda = 0
    derecha = len(array) - 1
    comparaciones = 0

    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2

        if array[medio] == objetivo:
            return {
                "found": True,
                "index": medio,
                "comparisons": comparaciones,
                "complexity": "O(log n)"
            }

        elif array[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return {
        "found": False,
        "index": -1,
        "comparisons": comparaciones,
        "complexity": "O(log n)"
    }