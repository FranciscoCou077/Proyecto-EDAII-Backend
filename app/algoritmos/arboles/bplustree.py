# Árbol B+ de orden 3
# Diferencia clave con B: los datos reales solo están en las hojas,
# y las hojas están enlazadas entre sí.

class NodoBPlus:
    def __init__(self):
        self.claves = []
        self.hijos = []       # solo para nodos internos
        self.siguiente = None # solo para nodos hoja (lista enlazada)
        self.es_hoja = True

class ArbolBPlus:
    def __init__(self, orden=3):
        self.orden = orden
        self.max_claves = orden - 1
        self.raiz = NodoBPlus()

    # ---------- BUSCAR ----------
    def buscar(self, clave):
        hoja = self._ir_a_hoja(self.raiz, clave)
        return clave in hoja.claves

    def _ir_a_hoja(self, nodo, clave):
        if nodo.es_hoja:
            return nodo

        i = 0
        while i < len(nodo.claves) and clave >= nodo.claves[i]:
            i += 1

        return self._ir_a_hoja(nodo.hijos[i], clave)

    # ---------- INSERTAR ----------
    def insertar(self, clave):
        resultado = self._insertar_recursivo(self.raiz, clave)

        # Si la raíz se dividió, crear nueva raíz
        if resultado is not None:
            clave_subida, nodo_derecho = resultado
            nueva_raiz = NodoBPlus()
            nueva_raiz.es_hoja = False
            nueva_raiz.claves = [clave_subida]
            nueva_raiz.hijos = [self.raiz, nodo_derecho]
            self.raiz = nueva_raiz

    def _insertar_recursivo(self, nodo, clave):
        if nodo.es_hoja:
            # Insertar en hoja manteniendo orden
            self._insertar_en_lista(nodo.claves, clave)

            if len(nodo.claves) > self.max_claves:
                return self._dividir_hoja(nodo)
            return None
        else:
            # Bajar al hijo correcto
            i = 0
            while i < len(nodo.claves) and clave >= nodo.claves[i]:
                i += 1

            resultado = self._insertar_recursivo(nodo.hijos[i], clave)

            if resultado is not None:
                clave_subida, nodo_derecho = resultado
                nodo.claves.insert(i, clave_subida)
                nodo.hijos.insert(i + 1, nodo_derecho)

                if len(nodo.claves) > self.max_claves:
                    return self._dividir_interno(nodo)

            return None

    def _insertar_en_lista(self, lista, valor):
        lista.append(valor)
        lista.sort()

    def _dividir_hoja(self, hoja):
        mitad = len(hoja.claves) // 2
        nueva_hoja = NodoBPlus()
        nueva_hoja.es_hoja = True

        nueva_hoja.claves = hoja.claves[mitad:]
        hoja.claves = hoja.claves[:mitad]

        # Enlazar las hojas
        nueva_hoja.siguiente = hoja.siguiente
        hoja.siguiente = nueva_hoja

        # La primera clave de la nueva hoja sube al padre
        return (nueva_hoja.claves[0], nueva_hoja)

    def _dividir_interno(self, nodo):
        mitad = len(nodo.claves) // 2
        clave_subida = nodo.claves[mitad]

        nuevo_nodo = NodoBPlus()
        nuevo_nodo.es_hoja = False
        nuevo_nodo.claves = nodo.claves[mitad + 1:]
        nuevo_nodo.hijos = nodo.hijos[mitad + 1:]

        nodo.claves = nodo.claves[:mitad]
        nodo.hijos = nodo.hijos[:mitad + 1]

        return (clave_subida, nuevo_nodo)

    # ---------- RECORRIDO DE HOJAS (característico del B+) ----------
    def recorrido_hojas(self):
        """Recorre todas las hojas enlazadas y devuelve todos los valores."""
        # Ir hasta la hoja más a la izquierda
        nodo = self.raiz
        while not nodo.es_hoja:
            nodo = nodo.hijos[0]

        valores = []
        while nodo is not None:
            valores.extend(nodo.claves)
            nodo = nodo.siguiente

        return valores