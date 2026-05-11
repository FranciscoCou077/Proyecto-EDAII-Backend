def counting_sort_por_digito(arr: list[int], exp: int) -> list[int]:
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        digito = (arr[i] // exp) % 10
        conteo[digito] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        digito = (arr[i] // exp) % 10
        salida[conteo[digito] - 1] = arr[i]
        conteo[digito] -= 1

    return salida


def radix_sort(arr: list[int]) -> dict:
    if not arr:
        return {"sorted_array": [], "steps": [], "comparisons": 0,
                "complexity": {"best": "O(nk)", "average": "O(nk)",
                               "worst": "O(nk)", "space": "O(n+k)"}}

    arr = arr.copy()
    steps = [{"array": arr.copy(), "descripcion": "Array inicial"}]
    comparisons = 0

    maximo = max(arr)
    exp = 1
    paso = 1

    while maximo // exp > 0:
        arr = counting_sort_por_digito(arr, exp)
        comparisons += len(arr)

        nombre_digito = {1: "unidades", 10: "decenas", 100: "centenas"}.get(
            exp, f"10^{paso-1}"
        )

        steps.append({
            "array": arr.copy(),
            "exp": exp,
            "descripcion": f"Ordenado por {nombre_digito}"
        })

        exp *= 10
        paso += 1

    return {
        "sorted_array": arr,
        "steps": steps,
        "comparisons": comparisons,
        "complexity": {
            "best": "O(nk)",
            "average": "O(nk)",
            "worst": "O(nk)",
            "space": "O(n+k)"
        }
    }