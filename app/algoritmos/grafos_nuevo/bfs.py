from collections import deque

def bfs(grafo, inicio):
    visitados = []
    cola = deque([inicio])
    vistos = set([inicio])

    while cola:
        nodo = cola.popleft()
        visitados.append(nodo)

        for vecino in grafo[nodo]:
            if vecino not in vistos:
                vistos.add(vecino)
                cola.append(vecino)
    return visitados