import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.algoritmos.grafos.bfs import bfs

def test_bfs_recorrido_completo():
    grafo = {0: [1, 2], 1: [3], 2: [], 3: []}
    resultado = bfs(grafo, 0)
    assert resultado == [0, 1, 2, 3]

def test_bfs_nodo_inicio_diferente():
    grafo = {0: [1], 1: [2], 2: []}
    resultado = bfs(grafo, 1)
    assert resultado[0] == 1

def test_bfs_grafo_un_nodo():
    grafo = {0: []}
    resultado = bfs(grafo, 0)
    assert resultado == [0]