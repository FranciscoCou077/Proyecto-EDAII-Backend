from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from multiprocessing import Pool
import time
import math

router = APIRouter()


# ── Lógica de paralelismo ─────────────────────────────────────────────────────

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True


def encontrar_primos_secuencial(limite: int) -> list[int]:
    return [n for n in range(2, limite + 1) if es_primo(n)]


def encontrar_primos_paralelo(limite: int, num_procesos: int = 4) -> list[int]:
    if limite < 2:
        return []
    numeros = list(range(2, limite + 1))
    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(es_primo, numeros)
    return [n for n, primo in zip(numeros, resultados) if primo]


def procesar_rango(inicio: int, fin: int, funcion: str) -> float:
    if funcion == "suma":
        return sum(range(inicio, fin + 1))
    elif funcion == "producto":
        resultado = 1
        for i in range(inicio, fin + 1):
            resultado *= i
        return resultado
    elif funcion == "suma_cuadrados":
        return sum(i * i for i in range(inicio, fin + 1))
    else:
        raise ValueError("funcion debe ser: 'suma', 'producto' o 'suma_cuadrados'")


def calcular_paralelo(n: int, funcion: str, num_procesos: int = 4) -> float:
    if n < 1:
        return 0
    tamano = n // num_procesos
    rangos = []
    inicio = 1
    for i in range(num_procesos):
        fin = inicio + tamano - 1
        if i == num_procesos - 1:
            fin = n
        if inicio <= n:
            rangos.append((inicio, fin, funcion))
        inicio = fin + 1
    with Pool(processes=num_procesos) as pool:
        resultados = pool.starmap(procesar_rango, rangos)
    if funcion == "producto":
        total = 1
        for r in resultados:
            total *= r
        return total
    return sum(resultados)


def comparar_rendimiento(n: int, num_procesos: int = 4) -> dict:
    inicio = time.time()
    primos_sec = encontrar_primos_secuencial(n)
    tiempo_secuencial = time.time() - inicio

    inicio = time.time()
    primos_par = encontrar_primos_paralelo(n, num_procesos)
    tiempo_paralelo = time.time() - inicio

    speedup = tiempo_secuencial / tiempo_paralelo if tiempo_paralelo > 0 else 0

    return {
        "tiempo_secuencial": round(tiempo_secuencial, 4),
        "tiempo_paralelo": round(tiempo_paralelo, 4),
        "speedup": round(speedup, 2),
        "num_primos": len(primos_par),
    }


# ── Datos teóricos ────────────────────────────────────────────────────────────

NIVELES_PARALELISMO = [
    {
        "nivel": "Nivel de bit",
        "descripcion": "Procesamiento simultáneo de múltiples bits en una sola operación. Permite realizar operaciones sobre palabras de datos más anchas.",
        "ejemplo": "Procesador de 64 bits realiza operaciones en 64 bits a la vez en lugar de 8."
    },
    {
        "nivel": "Nivel de instrucción",
        "descripcion": "El procesador ejecuta múltiples instrucciones simultáneamente mediante técnicas como pipelining, ejecución superescalar y out-of-order execution.",
        "ejemplo": "Pipeline de 5 etapas: fetch, decode, execute, memory, writeback ejecutándose en paralelo."
    },
    {
        "nivel": "Nivel de datos (SIMD)",
        "descripcion": "La misma instrucción se aplica simultáneamente a múltiples datos. Ideal para operaciones vectoriales y matriciales.",
        "ejemplo": "Sumar dos arreglos de 8 enteros en una sola instrucción SSE/AVX."
    },
    {
        "nivel": "Nivel de tarea",
        "descripcion": "Diferentes tareas o hilos independientes se ejecutan en paralelo en múltiples núcleos o procesadores.",
        "ejemplo": "Servidor web manejando múltiples peticiones HTTP simultáneamente con hilos."
    },
]

MODELOS_PRAM = [
    {
        "variante": "EREW",
        "significado": "Exclusive Read Exclusive Write",
        "descripcion": "El modelo más restrictivo. En cada paso, cada celda de memoria puede ser leída y escrita por a lo sumo un procesador. Evita todos los conflictos de acceso.",
        "ejemplo_uso": "Algoritmos de búsqueda paralela donde cada procesador trabaja en su propia partición."
    },
    {
        "variante": "CREW",
        "significado": "Concurrent Read Exclusive Write",
        "descripcion": "Múltiples procesadores pueden leer la misma celda simultáneamente, pero solo uno puede escribir en un instante dado. Modelo más común en la práctica.",
        "ejemplo_uso": "Broadcast de datos: todos los procesadores leen el pivote en QuickSort paralelo."
    },
    {
        "variante": "CRCW",
        "significado": "Concurrent Read Concurrent Write",
        "descripcion": "Permite lecturas y escrituras concurrentes. Cuando múltiples procesadores escriben en la misma celda se aplica una regla de resolución: prioridad, valor común o arbitrario.",
        "ejemplo_uso": "Encontrar el máximo de un arreglo en O(1) tiempo con n² procesadores."
    },
]

METRICAS = {
    "speedup": {
        "formula": "S(p) = T(1) / T(p)",
        "descripcion": "Aceleración obtenida usando p procesadores respecto a la ejecución secuencial.",
        "speedup_ideal": "S(p) = p (lineal)"
    },
    "eficiencia": {
        "formula": "E(p) = S(p) / p = T(1) / (p · T(p))",
        "descripcion": "Fracción del tiempo que cada procesador está siendo utilizado útilmente.",
        "rango": "0 < E(p) ≤ 1"
    },
    "ley_de_amdahl": {
        "formula": "S(p) = 1 / (f + (1-f)/p)",
        "descripcion": "Límite teórico del speedup. Si el 10% es secuencial, el speedup máximo es 10x sin importar cuántos procesadores se usen.",
    },
    "trabajo_costo": {
        "formula": "W = p · T(p)",
        "descripcion": "Trabajo total realizado. Un algoritmo es óptimo en costo si W = O(T_secuencial)."
    }
}


# ── Schemas ───────────────────────────────────────────────────────────────────

class PrimosRequest(BaseModel):
    limite: int = Field(..., ge=2, le=500_000, description="Límite superior para buscar primos")
    num_procesos: int = Field(default=4, ge=1, le=8, description="Número de procesos paralelos")
    modo: str = Field(default="paralelo", description="'paralelo' o 'secuencial'")

class PrimosResponse(BaseModel):
    limite: int
    num_procesos: int
    modo: str
    cantidad_primos: int
    primeros_10: list[int]
    ultimos_10: list[int]
    tiempo_segundos: float

class CalculoRequest(BaseModel):
    n: int = Field(..., ge=1, le=100_000, description="Valor máximo del rango [1, n]")
    funcion: str = Field(..., description="'suma', 'producto' o 'suma_cuadrados'")
    num_procesos: int = Field(default=4, ge=1, le=8)

class CalculoResponse(BaseModel):
    n: int
    funcion: str
    num_procesos: int
    resultado: float
    tiempo_segundos: float

class RendimientoResponse(BaseModel):
    limite: int
    num_procesos: int
    tiempo_secuencial: float
    tiempo_paralelo: float
    speedup: float
    num_primos: int
    eficiencia: float


# ── Endpoints ─────────────────────────────────────────────────────────────────

@router.get(
    "/info",
    summary="Teoría de algoritmos paralelos",
    description="Retorna información teórica completa: niveles de paralelismo, modelos PRAM y métricas."
)
def get_parallel_info():
    n = 8
    procesadores = n // 2
    pasos = math.ceil(math.log2(n))
    speedup_pram = round((n - 1) / pasos, 2)

    return {
        "introduccion": (
            "Los algoritmos paralelos permiten resolver problemas dividiendo el trabajo "
            "entre múltiples procesadores que operan simultáneamente. El modelo PRAM "
            "(Parallel Random Access Machine) es el modelo teórico estándar para analizarlos, "
            "asumiendo memoria compartida y acceso en tiempo constante."
        ),
        "niveles_de_paralelismo": NIVELES_PARALELISMO,
        "modelos_pram": MODELOS_PRAM,
        "metricas": METRICAS,
        "ejemplo_pram_simulado": {
            "operacion": "Suma de arreglo (reducción en árbol) — CREW PRAM",
            "n_elementos": n,
            "procesadores": procesadores,
            "pasos_paralelos": pasos,
            "complejidad_secuencial": f"O(n) = O({n})",
            "complejidad_paralela": f"O(log n) = O({pasos})",
            "speedup": speedup_pram,
            "eficiencia": round(speedup_pram / procesadores, 2),
        }
    }


@router.post(
    "/primos",
    response_model=PrimosResponse,
    summary="Búsqueda de primos paralela o secuencial",
    description="Encuentra todos los números primos hasta el límite usando multiprocessing real."
)
def buscar_primos(request: PrimosRequest):
    try:
        inicio = time.time()
        if request.modo == "secuencial":
            primos = encontrar_primos_secuencial(request.limite)
        else:
            primos = encontrar_primos_paralelo(request.limite, request.num_procesos)
        tiempo = round(time.time() - inicio, 4)

        return PrimosResponse(
            limite=request.limite,
            num_procesos=request.num_procesos,
            modo=request.modo,
            cantidad_primos=len(primos),
            primeros_10=primos[:10],
            ultimos_10=primos[-10:],
            tiempo_segundos=tiempo,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/calcular",
    response_model=CalculoResponse,
    summary="Cálculo paralelo sobre rango [1, n]",
    description="Ejecuta suma, producto o suma de cuadrados en paralelo dividiendo el rango entre procesos."
)
def calcular(request: CalculoRequest):
    if request.funcion not in ("suma", "producto", "suma_cuadrados"):
        raise HTTPException(status_code=400, detail="funcion debe ser: 'suma', 'producto' o 'suma_cuadrados'")
    try:
        inicio = time.time()
        resultado = calcular_paralelo(request.n, request.funcion, request.num_procesos)
        tiempo = round(time.time() - inicio, 4)

        return CalculoResponse(
            n=request.n,
            funcion=request.funcion,
            num_procesos=request.num_procesos,
            resultado=resultado,
            tiempo_segundos=tiempo,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/rendimiento",
    response_model=RendimientoResponse,
    summary="Comparación secuencial vs paralelo",
    description="Ejecuta búsqueda de primos en ambos modos y compara tiempos reales de ejecución."
)
def rendimiento(limite: int = 50_000, num_procesos: int = 4):
    if limite < 2 or limite > 500_000:
        raise HTTPException(status_code=400, detail="limite debe estar entre 2 y 500000")
    if num_procesos < 1 or num_procesos > 8:
        raise HTTPException(status_code=400, detail="num_procesos debe estar entre 1 y 8")
    try:
        resultado = comparar_rendimiento(limite, num_procesos)
        eficiencia = round(resultado["speedup"] / num_procesos, 2)

        return RendimientoResponse(
            limite=limite,
            num_procesos=num_procesos,
            tiempo_secuencial=resultado["tiempo_secuencial"],
            tiempo_paralelo=resultado["tiempo_paralelo"],
            speedup=resultado["speedup"],
            num_primos=resultado["num_primos"],
            eficiencia=eficiencia,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))