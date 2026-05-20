def busqueda_hash(array, objetivo):
    tabla_hash = {}
    colisiones = 0

    for i, valor in enumerate(array):
        if valor in tabla_hash:
            colisiones += 1
        tabla_hash[valor] = i

    encontrado = objetivo in tabla_hash

    return {
        "found": encontrado,
        "index": tabla_hash.get(objetivo, -1),
        "collisions": colisiones,
        "complexity": "O(1)"
    }