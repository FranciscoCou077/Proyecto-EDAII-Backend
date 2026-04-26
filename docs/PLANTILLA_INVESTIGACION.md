# 📄 Documento de Investigación: [Nombre del Algoritmo]

## 1. Información General
* **Tema / Unidad:** [Ej. 3. Algoritmos de Grafos]
* **Algoritmo:** [Nombre exacto del algoritmo]
* **Subgrupo de Investigación:** [Nombres de los integrantes]
* **Fecha de Revisión:** [DD/MM/AAAA]

---

## 2. Descripción Teórica y Funcionamiento
*(Esta sección provee la base de conocimiento para el Agente de IA).*
* **Definición:** Concepto formal y utilidad del algoritmo.
* **Mecánica paso a paso:** Descripción lógica del flujo de datos.
* **Ventajas y Desventajas:** Análisis comparativo de eficiencia y limitaciones.

## 3. Análisis de Complejidad Matemático (Big-O)
* **Complejidad Temporal (Peor caso):** $O(\cdot)$
* **Complejidad Temporal (Caso promedio):** $O(\cdot)$
* **Complejidad Espacial (Memoria):** $O(\cdot)$

## 4. Estrategia de Implementación (Backend - Python)
* **Estructuras de Datos base:** (Ej. Listas de adyacencia, pilas, colas de prioridad).
* **Firma de la Función Principal (Propuesta):** ```python
  def ejecutar_algoritmo(input_data: dict) -> dict:
      """
      Descripción breve de la implementación.
      """
      pass
  ```
* **Librerías externas permitidas:** (Idealmente ninguna para la lógica pura, pero especificar si se requiere alguna como `numpy` para cálculos específicos).

## 5. Casos de Prueba Críticos (Edge Cases)
*(Sección diseñada para anticipar los archivos de prueba (.txt/.csv) del profesor).*
* **Caso trivial:** (Ej. Una lista con un solo elemento o un grafo con un solo nodo).
* **Caso de fallo:** (Ej. Archivo de entrada vacío, formato de datos incorrecto, grafos disconexos cuando se busca un camino).
* **Caso de estrés:** (Ej. Procesamiento de un conjunto de datos masivo para evaluar el límite de tiempo de ejecución).

## 6. Integración y Estructura de Datos (API)
*(Crucial para la comunicación con la Interfaz Gráfica y el Chatbot).*
* **Formato de Entrada esperado (JSON):** ¿Qué datos necesita recibir el backend desde la Interfaz Gráfica?
  ```json
  {
    "algoritmo": "nombre",
    "parametros": {
      "dato_1": [],
      "opcion": "valor"
    }
  }
  ```
* **Formato de Salida esperado (JSON):** ¿Qué estructura devolverá el backend para que la GUI pueda renderizar/animar el resultado sin errores?
  ```json
  {
    "resultado": [],
    "tiempo_ejecucion": "0.00s",
    "pasos": []
  }
  ```

## 7. Referencias Bibliográficas
*(Citar libros del temario oficial u otras fuentes confiables).*
* **Básica:** AHO, Alfred. *Data Structures and Algorithms*. New Jersey: Addison-Wesley, 1983.
* **Complementaria:** CORMEN, Thomas. *Introduction to Algorithms*.
* **Otras fuentes:** [Insertar libros o artículos científicos consultados].
