from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import List

from app.algoritmos.arboles.binary_tree import ArbolBinario
from app.algoritmos.arboles.btree import ArbolB
from app.algoritmos.arboles.bplustree import ArbolBPlus
from app.algoritmos.arboles.notation import infija_a_sufija, infija_a_prefija

router = APIRouter(prefix="/api/trees", tags=["Trees"])


# ─────────────────────────────────────────────
# MODELOS DE ENTRADA
# ─────────────────────────────────────────────

class BinaryTreeRequest(BaseModel):
    valores: List[int]
    operacion: str  # insertar, buscar, preorden, inorden, postorden, nivel_orden
    buscar_valor: int | None = None


class BTreeRequest(BaseModel):
    valores: List[int]
    operacion: str  # insertar, buscar
    tipo: str       # b o b+
    buscar_valor: int | None = None


class NotationRequest(BaseModel):
    expresion: str
    tipo: str  # sufija o prefija


# ─────────────────────────────────────────────
# POST /api/trees/binary
# ─────────────────────────────────────────────

@router.post("/binary")
def operar_arbol_binario(request: BinaryTreeRequest):
    arbol = ArbolBinario()

    for v in request.valores:
        arbol.insertar(v)

    op = request.operacion.lower()

    if op == "insertar":
        return {
            "mensaje": "Valores insertados correctamente",
            "inorden": arbol.inorden()
        }

    if op == "buscar":
        if request.buscar_valor is None:
            raise HTTPException(status_code=400, detail="Falta buscar_valor")

        return {
            "valor": request.buscar_valor,
            "encontrado": arbol.buscar(request.buscar_valor)
        }

    if op == "preorden":
        return {"recorrido": arbol.preorden()}

    if op == "inorden":
        return {"recorrido": arbol.inorden()}

    if op == "postorden":
        return {"recorrido": arbol.postorden()}

    if op == "nivel_orden":
        return {"recorrido": arbol.nivel_orden()}

    raise HTTPException(status_code=400, detail="Operación no válida")


# ─────────────────────────────────────────────
# POST /api/trees/btree
# ─────────────────────────────────────────────

@router.post("/btree")
def operar_btree(request: BTreeRequest):

    if request.tipo.lower() == "b":
        arbol = ArbolB(orden=3)
    elif request.tipo.lower() == "b+":
        arbol = ArbolBPlus(orden=3)
    else:
        raise HTTPException(status_code=400, detail="tipo debe ser 'b' o 'b+'")

    for v in request.valores:
        arbol.insertar(v)

    op = request.operacion.lower()

    if op == "insertar":
        if request.tipo.lower() == "b":
            return {
                "mensaje": "Valores insertados en Árbol B",
                "estructura": arbol.recorrido_por_niveles()
            }
        else:
            return {
                "mensaje": "Valores insertados en Árbol B+",
                "hojas": arbol.recorrido_hojas()
            }

    if op == "buscar":
        if request.buscar_valor is None:
            raise HTTPException(status_code=400, detail="Falta buscar_valor")

        return {
            "valor": request.buscar_valor,
            "encontrado": arbol.buscar(request.buscar_valor)
        }

    raise HTTPException(status_code=400, detail="Operación no válida")


# ─────────────────────────────────────────────
# POST /api/trees/notation
# ─────────────────────────────────────────────

@router.post("/notation")
def convertir_notacion(request: NotationRequest):

    if request.tipo.lower() == "sufija":
        return {
            "original": request.expresion,
            "resultado": infija_a_sufija(request.expresion)
        }

    if request.tipo.lower() == "prefija":
        return {
            "original": request.expresion,
            "resultado": infija_a_prefija(request.expresion)
        }

    raise HTTPException(status_code=400, detail="tipo debe ser 'sufija' o 'prefija'")