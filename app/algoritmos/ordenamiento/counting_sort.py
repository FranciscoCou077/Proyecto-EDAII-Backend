def counting_sort(arr: list[int]) -> dict:
    if not arr:
        return {"sorted_array": [], "steps": [], "comparisons": 0,
                "complexity": {"best": "O(n+k)", "average": "O(n+k)",
                               "worst": "O(n+k)", "space": "O(k)"}}

    arr = arr.copy()
    steps = [{"array": arr.copy(), "descripcion": "Array inicial"}]
    comparisons = 0

    maximo = max(arr)
    minimo = min(arr)
    rango = maximo - minimo + 1

    # Paso 1 — Contar ocurrencias
    conteo = [0] * rango
    for num in arr:
        conteo[num - minimo] += 1
        comparisons += 1

    steps.append({
        "array": arr.copy(),
        "conteo": conteo.copy(),
        "descripcion": f"Conteo de ocurrencias (rango {minimo} a {maximo})"
    })

    # Paso 2 — Acumular conteos
    for i in range(1, rango):
        conteo[i] += conteo[i - 1]

    steps.append({
        "array": arr.copy(),
        "conteo": conteo.copy(),
        "descripcion": "Conteo acumulado"
    })

    # Paso 3 — Construir array de salida
    salida = [0] * len(arr)
    for num in reversed(arr):
        salida[conteo[num - minimo] - 1] = num
        conteo[num - minimo] -= 1

    steps.append({
        "array": salida.copy(),
        "descripcion": "Array ordenado final"
    })

    return {
        "sorted_array": salida,
        "steps": steps,
        "comparisons": comparisons,
        "complexity": {
            "best": "O(n+k)",
            "average": "O(n+k)",
            "worst": "O(n+k)",
            "space": "O(k)"
        }
    }