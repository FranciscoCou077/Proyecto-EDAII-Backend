# API Endpoints — Backend EDA II

Base URL (local): http://localhost:8000
Base URL (producción): pendiente de despliegue

---

## Ordenamiento

### POST /api/sorting/counting-sort
Ordena un arreglo usando Counting Sort.

Body:
{
  "array": [5, 3, 8, 1, 2]
}

Respuesta:
{
  "sorted_array": [1, 2, 3, 5, 8],
  "steps": [...],
  "comparisons": 5,
  "complexity": {
    "best": "O(n+k)",
    "average": "O(n+k)",
    "worst": "O(n+k)",
    "space": "O(k)"
  }
}

---

### POST /api/sorting/radix-sort
Ordena un arreglo usando Radix Sort.

Body:
{
  "array": [170, 45, 75, 90, 802]
}

---

### POST /api/sorting/merge-sort
Ordena un arreglo usando Merge Sort.

Body:
{
  "array": [5, 3, 8, 1, 2]
}

---

### POST /api/sorting/bubble-sort
Ordena un arreglo usando Bubble Sort.

Body:
{
  "arreglo": [5, 3, 8, 1, 2]
}

---

### POST /api/sorting/heap-sort
Ordena un arreglo usando Heap Sort.

Body:
{
  "arreglo": [5, 3, 8, 1, 2]
}

---

### POST /api/sorting/quick-sort
Ordena un arreglo usando Quick Sort.

Body:
{
  "arreglo": [5, 3, 8, 1, 2]
}

---

### GET /api/sorting/compare
Corre todos los algoritmos con el mismo arreglo y devuelve comparativa de rendimiento.

Query param:
?array=5,3,8,1,9,2,7,4,6

---

## Grafos

### POST /api/graphs/represent
Devuelve matriz de adyacencia y lista de adyacencia.

Body:
{
  "edges": [[0,1],[1,2],[2,3]],
  "n": 4,
  "inicio": 0
}

---

### POST /api/graphs/bfs
Recorrido BFS (Búsqueda por expansión).

Body:
{
  "edges": [[0,1],[1,2],[2,3]],
  "n": 4,
  "inicio": 0
}

---

### POST /api/graphs/dfs
Recorrido DFS (Búsqueda por profundidad).

Body:
{
  "edges": [[0,1],[1,2],[2,3]],
  "n": 4,
  "inicio": 0
}

---

## Estado actual de integración

Módulo                           | Estado
---------------------------------|------------------
Ordenamiento (bubble, heap, quick)| Listo - pendiente PR de Ernesto
Ordenamiento (counting, radix, merge)| Integrado en dev
Grafos (BFS, DFS, representación)| Integrado en dev
Algoritmos paralelos             | Integrado en dev
Búsqueda (lineal, binaria, hash) | Integrado en dev
Árboles (binario, notaciones)    | Listo - pendiente mover carpeta
Archivos + Base de datos         | Listo - pendiente resolver conflicto

---

## Formato estándar de respuesta

Todos los endpoints devuelven esta estructura:

{
  "result": "...",
  "steps": [],
  "complexity": {
    "best": "O(...)",
    "average": "O(...)",
    "worst": "O(...)",
    "space": "O(...)"
  }
}

---

## Notas para Frontend y Chatbot

- Todos los endpoints aceptan y devuelven JSON
- CORS habilitado para cualquier origen
- Documentación interactiva disponible en /docs
- El campo steps contiene el estado del arreglo en cada paso para animaciones