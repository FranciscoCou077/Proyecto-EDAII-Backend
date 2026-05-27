def prioridad(operador):

    if operador == "+" or operador == "-":
        return 1

    if operador == "*" or operador == "/":
        return 2

    if operador == "^":
        return 3

    return 0


def infija_a_sufija(expresion: str, reverse_asociativity: bool = False) -> str:

    pila = []
    salida = []

    partes = expresion.split()

    for parte in partes:

        if parte.isalnum():
            salida.append(parte)

        elif parte == "(":
            pila.append(parte)

        elif parte == ")":

            while len(pila) > 0 and pila[-1] != "(":
                salida.append(pila.pop())

            if len(pila) > 0:
                pila.pop()

        else:

            pop_equal = (parte != "^") if not reverse_asociativity else (parte == "^")

            while len(pila) > 0 and pila[-1] != "(" and (
                prioridad(pila[-1]) > prioridad(parte)
                or (prioridad(pila[-1]) == prioridad(parte) and pop_equal)
            ):
                salida.append(pila.pop())

            pila.append(parte)

    while len(pila) > 0:
        salida.append(pila.pop())

    return " ".join(salida)


def infija_a_prefija(expresion: str) -> str:

    partes = expresion.split()
    partes.reverse()

    nueva = []

    for parte in partes:

        if parte == "(":
            nueva.append(")")

        elif parte == ")":
            nueva.append("(")

        else:
            nueva.append(parte)

    invertida = " ".join(nueva)

    sufija = infija_a_sufija(invertida, reverse_asociativity=True)

    resultado = sufija.split()
    resultado.reverse()

    return " ".join(resultado)