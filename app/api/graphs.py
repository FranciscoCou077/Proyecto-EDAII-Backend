from fastapi import APIRouter 
from app.algoritmos._3_grafos import bfs, dfs, representacion

router = APIRouter()

@router.post("/api/graphs/represent")
def representar_grafo(edges: list[tuple[int, int]], n: int):
    matriz = representacion.matriz_adyacencia(edges, n)
    lista = representacion.lista_adyacencia(edges, n)
    return {"matriz": matriz, "lista": lista}

@router.post("/api/graphs/bfs")
def ejecutar_bfs(edges: list[tuple[int, int]], n: int, inicio: int):
    grafo = representacion.lista_adyacencia(edges, n)
    recorrido = dfs.dfs(grafo, inicio)
    return {"recorrido": recorrido}
