def matriz_adyacencia(edges, n):
    matriz = [[0] * n for _ in range(n)]
    for u, v in edges:
        matriz[u][v] = 1
        matriz[v][u] = 1  # Para grafos no dirigidos
    return matriz
def lista_adyacencia(edges, n):
    lista = {i: [] for i in range(n)}
    for u, v in edges:
        lista[u].append(v)
        lista[v].append(u)  # Para grafos no dirigidos
    return lista

