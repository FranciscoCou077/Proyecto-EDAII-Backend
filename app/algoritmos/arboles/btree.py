# Árbol B de orden 3 (máximo 2 claves por nodo, máximo 3 hijos)

class NodoBTree:
    def __init__(self):
        self.claves = []
        self.hijos = []
        self.es_hoja = True

class ArbolB:
    def __init__(self, orden=3):
        self.orden = orden          # número máximo de hijos
        self.max_claves = orden - 1 # máximo de claves por nodo
        self.raiz = NodoBTree()

    # ---------- BUSCAR ----------
    def buscar(self, clave, nodo=None):
        if nodo is None:
            nodo = self.raiz

        # Recorremos las claves del nodo para ver si está
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and clave == nodo.claves[i]:
            return True  # encontrado

        if nodo.es_hoja:
            return False  # no existe

        return self.buscar(clave, nodo.hijos[i])

    # ---------- INSERTAR ----------
    def insertar(self, clave):
        raiz = self.raiz

        # Si la raíz está llena, hay que dividirla
        if len(raiz.claves) == self.max_claves:
            nueva_raiz = NodoBTree()
            nueva_raiz.es_hoja = False
            nueva_raiz.hijos.append(self.raiz)
            self._dividir_hijo(nueva_raiz, 0)
            self.raiz = nueva_raiz

        self._insertar_no_lleno(self.raiz, clave)

    def _insertar_no_lleno(self, nodo, clave):
        i = len(nodo.claves) - 1

        if nodo.es_hoja:
            # Insertar la clave en el lugar correcto
            nodo.claves.append(None)
            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = clave
        else:
            # Encontrar el hijo donde debe ir
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1

            # Si ese hijo está lleno, dividirlo primero
            if len(nodo.hijos[i].claves) == self.max_claves:
                self._dividir_hijo(nodo, i)
                if clave > nodo.claves[i]:
                    i += 1

            self._insertar_no_lleno(nodo.hijos[i], clave)

    def _dividir_hijo(self, padre, i):
        orden = self.orden
        nodo_lleno = padre.hijos[i]
        nuevo_nodo = NodoBTree()
        nuevo_nodo.es_hoja = nodo_lleno.es_hoja

        mitad = orden // 2  # índice de la clave que sube al padre

        # La clave del medio sube al padre
        padre.claves.insert(i, nodo_lleno.claves[mitad])

        # El nuevo nodo se queda con las claves de la derecha
        nuevo_nodo.claves = nodo_lleno.claves[mitad + 1:]
        nodo_lleno.claves = nodo_lleno.claves[:mitad]

        # Si no es hoja, también dividir los hijos
        if not nodo_lleno.es_hoja:
            nuevo_nodo.hijos = nodo_lleno.hijos[mitad + 1:]
            nodo_lleno.hijos = nodo_lleno.hijos[:mitad + 1]

        padre.hijos.insert(i + 1, nuevo_nodo)

    # ---------- RECORRIDO (para mostrar resultado) ----------
    def recorrido_por_niveles(self):
        """Devuelve una lista de listas con las claves por nivel."""
        if not self.raiz.claves:
            return []

        resultado = []
        cola = [self.raiz]

        while cola:
            nivel = []
            siguiente = []
            for nodo in cola:
                nivel.append(nodo.claves[:])
                for hijo in nodo.hijos:
                    siguiente.append(hijo)
            resultado.append(nivel)
            cola = siguiente

        return resultado