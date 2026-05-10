def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = []
    visitados.append(inicio)
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
    return visitados