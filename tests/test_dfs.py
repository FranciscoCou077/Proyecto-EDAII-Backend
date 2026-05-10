import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.algoritmos.grafos.dfs import dfs

def test_dfs_recorrido_completo():
    grafo = {0: [1, 2], 1: [3], 2: [], 3: []}
    resultado = dfs(grafo, 0)
    assert 0 in resultado
    assert len(resultado) == 4

def test_dfs_nodo_inicio_primero():
    grafo = {0: [1], 1: [2], 2: []}
    resultado = dfs(grafo, 0)
    assert resultado[0] == 0

def test_dfs_grafo_un_nodo():
    grafo = {0: []}
    resultado = dfs(grafo, 0)
    assert resultado == [0]