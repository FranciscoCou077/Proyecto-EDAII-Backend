from fastapi import FastAPI

# Inicializamos la aplicación de FastAPI
app = FastAPI(
    title="API Backend - Estructura de Datos y Algoritmos II",
    description="Motor algorítmico para evaluación, consulta y ejecución de algoritmos.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """
    Endpoint raíz para comprobar que el servidor está funcionando correctamente.
    """
    return {
        "estado": "En línea",
        "mensaje": "Bienvenido al motor Backend de EDA II",
        "equipo": "Backend"
    }