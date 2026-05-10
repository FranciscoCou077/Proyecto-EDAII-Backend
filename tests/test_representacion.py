import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.algoritmos.grafos.representacion import matriz_adyacencia, lista_adyacencia

def test_matriz_adyacencia_size():
    edges = [[0, 1], [1, 2]]
    matriz = matriz_adyacencia(edges, 3)
    assert len(matriz) == 3
    assert len(matriz[0]) == 3

def test_matriz_adyacencia_valores():
    edges = [[0, 1]]
    matriz = matriz_adyacencia(edges, 2)
    assert matriz[0][1] == 1
    assert matriz[1][0] == 1  # no dirigido

def test_lista_adyacencia_keys():
    edges = [[0, 1], [1, 2]]
    lista = lista_adyacencia(edges, 3)
    assert 0 in lista
    assert 1 in lista
    assert 2 in lista

def test_lista_adyacencia_vecinos():
    edges = [[0, 1]]
    lista = lista_adyacencia(edges, 2)
    assert 1 in lista[0]
    assert 0 in lista[1]  