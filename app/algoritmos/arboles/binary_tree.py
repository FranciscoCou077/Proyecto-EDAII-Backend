class NodoArbol:

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:

    def __init__(self):
        self.raiz = None


    def insertar(self, valor):

        if self.raiz is None:
            self.raiz = NodoArbol(valor)
            return

        actual = self.raiz

        while True:

            if valor < actual.valor:

                if actual.izquierdo is None:
                    actual.izquierdo = NodoArbol(valor)
                    return

                actual = actual.izquierdo

            elif valor > actual.valor:

                if actual.derecho is None:
                    actual.derecho = NodoArbol(valor)
                    return

                actual = actual.derecho

            else:
                return


    def buscar(self, valor):

        actual = self.raiz

        while actual is not None:

            if valor == actual.valor:
                return True

            if valor < actual.valor:
                actual = actual.izquierdo

            else:
                actual = actual.derecho

        return False


    def eliminar(self, valor):

        self.raiz = self._eliminar(self.raiz, valor)


    def _eliminar(self, raiz, valor):

        if raiz is None:
            return raiz

        if valor < raiz.valor:
            raiz.izquierdo = self._eliminar(raiz.izquierdo, valor)

        elif valor > raiz.valor:
            raiz.derecho = self._eliminar(raiz.derecho, valor)

        else:

            if raiz.izquierdo is None:
                return raiz.derecho

            if raiz.derecho is None:
                return raiz.izquierdo

            menor = self._minimo(raiz.derecho)

            raiz.valor = menor.valor

            raiz.derecho = self._eliminar(raiz.derecho, menor.valor)

        return raiz


    def _minimo(self, raiz):

        actual = raiz

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual


    def preorden(self):
        return preorden(self.raiz)


    def inorden(self):
        return inorden(self.raiz)


    def postorden(self):
        return postorden(self.raiz)


    def nivel_orden(self):
        return nivel_orden(self.raiz)


def preorden(raiz: NodoArbol) -> list:
    """Recorrido preorden: raíz, izquierdo, derecho."""
    
    if raiz is None:
        return []

    res = []

    res.append(raiz.valor)
    res += preorden(raiz.izquierdo)
    res += preorden(raiz.derecho)

    return res


def inorden(raiz: NodoArbol) -> list:
    """Recorrido inorden: izquierdo, raíz, derecho."""
    
    if raiz is None:
        return []

    res = []

    res += inorden(raiz.izquierdo)
    res.append(raiz.valor)
    res += inorden(raiz.derecho)

    return res


def postorden(raiz: NodoArbol) -> list:
    """Recorrido postorden: izquierdo, derecho, raíz."""
    
    if raiz is None:
        return []

    res = []

    res += postorden(raiz.izquierdo)
    res += postorden(raiz.derecho)
    res.append(raiz.valor)

    return res


def nivel_orden(raiz: NodoArbol) -> list:
    """Recorrido por niveles (BFS en árbol)."""
    
    if raiz is None:
        return []

    res = []
    cola = [raiz]

    while len(cola) > 0:

        actual = cola.pop(0)

        res.append(actual.valor)

        if actual.izquierdo is not None:
            cola.append(actual.izquierdo)

        if actual.derecho is not None:
            cola.append(actual.derecho)

    return res