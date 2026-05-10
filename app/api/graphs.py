from fastapi import APIRouter
from pydantic import BaseModel
from app.algoritmos.grafos import bfs, dfs, representacion

router = APIRouter()

class GrafoInput(BaseModel):
    edges: list[list[int]]
    n: int
    inicio: int = 0

@router.post("/represent")
def representar_grafo(data: GrafoInput):
    matriz = representacion.matriz_adyacencia(data.edges, data.n)
    lista  = representacion.lista_adyacencia(data.edges, data.n)
    return {
        "matriz": matriz,
        "lista": lista,
        "complexity": {
            "matriz": "O(V²) espacio",
            "lista":  "O(V+E) espacio"
        }
    }

@router.post("/bfs")
def ejecutar_bfs(data: GrafoInput):
    grafo     = representacion.lista_adyacencia(data.edges, data.n)
    recorrido = bfs.bfs(grafo, data.inicio)
    return {
        "recorrido": recorrido,
        "nodo_inicio": data.inicio,
        "complexity": {
            "time":  "O(V + E)",
            "space": "O(V)"
        }
    }

@router.post("/dfs")
def ejecutar_dfs(data: GrafoInput):
    grafo     = representacion.lista_adyacencia(data.edges, data.n)
    recorrido = dfs.dfs(grafo, data.inicio)
    return {
        "recorrido": recorrido,
        "nodo_inicio": data.inicio,
        "complexity": {
            "time":  "O(V + E)",
            "space": "O(V)"
        }
    }