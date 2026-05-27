# Investigacion de Algoritmos de Grafos (DFS y BFS)

## 1. Introduccion a Grafos. 
Un **grafo** es una estructura de datos compuesta por **nodos (vértices)** y **aristas (bordes)** que representan conexiones entre dichos nodos.  
Los grafos pueden ser **dirigidos** (las aristas tienen dirección) o **no dirigidos**, y pueden contener **pesos** en las aristas para representar costos o distancias.  
Son fundamentales en informática para modelar redes, caminos, relaciones y estructuras jerárquicas.

## 2. Busqueda en Profundidad (DFS - Depth-First Search)

### ¿Cómo funciona?
- **Concepto:** Explora lo más profundo posible en cada rama antes de retroceder (*backtracking*).  
- **Estructura de Datos Utilizada:** Una **Pila (Stack)**, ya sea de forma explícita o implícita mediante recursividad.

### Complejidad Algorítmica
- **Tiempo:** \(O(V + E)\), donde \(V\) es el número de vértices y \(E\) el número de aristas.  
- **Espacio:** \(O(V)\), debido al almacenamiento de la pila de llamadas o nodos visitados.

### Casos de Uso Comunes
- Detección de ciclos en grafos.  
- Ordenamiento topológico.  
- Resolver laberintos (verificar si existe un camino).

## 3. Búsqueda en Anchura (BFS - Breadth-First Search)

### ¿Cómo funciona?
- **Concepto:** Explora los vecinos de un nodo **nivel por nivel**: primero los vecinos directos, luego los vecinos de los vecinos, y así sucesivamente.  
- **Estructura de Datos Utilizada:** Una **Cola (Queue)** siguiendo el principio FIFO (*First In, First Out*).

### Complejidad Algorítmica
- **Tiempo:** \(O(V + E)\).  
- **Espacio:** \(O(V)\), aunque puede requerir más memoria en grafos muy anchos.

### Casos de Uso Comunes
- Encontrar el **camino más corto** en grafos no ponderados.  
- Algoritmos de ruteo en redes.  
- Sistemas de recomendación (amigos en común de primer nivel, segundo nivel, etc.).

## 4. Tabla Comparativa: DFS vs BFS

| Característica       | DFS (Depth-First Search) | BFS (Breadth-First Search) |
|-----------------------|---------------------------|-----------------------------|
| **Estructura**        | Pila (Stack / Recursión) | Cola (Queue)                |
| **Enfoque**           | Explora hacia lo profundo | Explora por niveles         |
| **Camino más corto**  | No garantiza              | Sí garantiza (sin pesos)    |
| **Memoria**           | Menor en grafos anchos    | Mayor (almacena nodos por nivel) |
