# Proyecto-EDAII-Backend
# Core Algorítmico y Backend API | Estructura de Datos y Algoritmos II

Bienvenido al repositorio central del equipo de Backend. Este proyecto constituye el núcleo lógico de una solución de software integral desarrollada para el proyecto final de la asignatura de Estructura de Datos y Algoritmos II (UNAM, Facultad de Ingeniería).

## Finalidad del Software (El Proyecto Global)

El objetivo final de este proyecto integrador es construir una plataforma educativa e interactiva que permita la ejecución, visualización y consulta de todos los algoritmos estudiados durante el curso (ordenamiento, búsqueda, grafos, árboles, manejo de archivos y paralelismo). 

Para lograr un producto a nivel de producción, el desarrollo de todo el grupo se ha fragmentado en una arquitectura de microservicios o módulos independientes:
1.  **Backend (Este repositorio):** Motor de cálculo y procesamiento.
2.  **Agente de IA / Chatbot:** Interfaz de procesamiento de lenguaje natural para consultas teóricas y analíticas sobre los algoritmos.
3.  **Interfaz Gráfica de Usuario (GUI):** Entorno visual interactivo para el usuario final.

El software resultante permitirá al profesor (o a cualquier usuario) cargar archivos de prueba personalizados, consultar el funcionamiento de estructuras de datos mediante el chatbot, y observar el comportamiento de los algoritmos con entradas de datos reales a través de la interfaz gráfica.

## Propósito del Backend

Este repositorio tiene una responsabilidad única y crítica: **procesar la información sin bloqueos y servirla de manera estandarizada.** El Backend no imprime datos en consola ni genera ventanas; su propósito es exponer una API estructurada (desarrollada en Python) que reciba las peticiones de la Interfaz Gráfica y del Agente de IA, ejecute el algoritmo correspondiente con la máxima eficiencia posible, gestione la lectura de los archivos de prueba del profesor, y devuelva los resultados estructurados (ej. en formato JSON). Esta separación de responsabilidades asegura que el sistema sea escalable y tolerante a fallos.

## Metodología de Trabajo y Rigor Técnico

Para garantizar la integridad del código y fomentar un entorno de trabajo colaborativo profesional entre los desarrolladores, este repositorio se rige por un esquema estricto de control de versiones basado en **Git Flow**:

* **Protección de la Rama Principal:** Está estrictamente prohibido realizar `push` directo a la rama `main`. La rama `main` refleja únicamente código estable, probado y funcional.
* **Desarrollo Basado en Ramas (Branching):** Cada nuevo algoritmo, corrección de errores (bugfix) o refactorización debe desarrollarse en una rama aislada (ej. `feature/dijkstra-grafos`, `fix/lectura-archivos`).
* **Integración mediante Pull Requests (PR):** Para integrar código a la rama principal, el desarrollador debe abrir un Pull Request. 
* **Revisión por Pares (Code Review):** Ningún PR puede ser fusionado (*merged*) sin la revisión y aprobación explícita de al menos un compañero del equipo de backend. Esto asegura la calidad del código, el cumplimiento de la convención de nombres y la correcta documentación interna.
* **Estructura Homologada:** Todo el código se organiza siguiendo fielmente la estructura del temario oficial, asegurando que cualquier miembro del grupo pueda localizar rápidamente las implementaciones.

## Equipo de Desarrollo Backend

La arquitectura, programación de algoritmos y mantenimiento de esta API está a cargo de:

* **Francisco José Coutiño Morales** - Lead Backend Developer ([GitHub](https://github.com/FranciscoCou077))
* **Ernesto Flamenco Villaseñor** - Backend Developer ([GitHub](https://github.com/))
* *[Nombre del Desarrollador 4]* - Backend Developer ([GitHub](https://github.com/))
* *[Nombre del Desarrollador 4]* - Backend Developer ([GitHub](https://github.com/))
* *[Nombre del Desarrollador 5]* - Backend Developer ([GitHub](https://github.com/))
* *[Nombre del Desarrollador 6]* - Backend Developer ([GitHub](https://github.com/))

---
*Desarrollado con rigor, lógica y código limpio.*
