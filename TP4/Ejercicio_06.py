"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando  la  posición  y  la  cantidad  de  caracteres  deseada.  Devolver  la  subcadena
como  valor  de  retorno.  Escribir  también  un  programa  para  verificar  el  comporta-
miento  de  la  misma.  Ejemplo,  dada  la  cadena  "El  número  de  teléfono  es  4356-
7890"  extraer  la  subcadena  que  comienza  en  la  posición  25  y  tiene  9  caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""


def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """Función para extraer una subcadena utilizando rebanadas

    Pre: Recibe una cadena de caracteres, la posición inicial y la cantidad de caracteres a extraer

    Post: Devuelve la subcadena extraída
    """
    assert isinstance(cadena, str), "La entrada debe ser una cadena de caracteres"
    assert (
        isinstance(posicion, int) and posicion >= 0
    ), "La posición debe ser un entero no negativo"
    assert (
        isinstance(cantidad, int) and cantidad >= 0
    ), "La cantidad debe ser un entero no negativo"

    return cadena[
        posicion : posicion + cantidad
    ]  # Utilizamos rebanadas para extraer la subcadena, desde la posición hasta la posición + cantidad


def extraer_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """Función para extraer una subcadena sin utilizar rebanadas

    Pre: Recibe una cadena de caracteres, la posición inicial y la cantidad de caracteres a extraer

    Post: Devuelve la subcadena extraída
    """
    assert isinstance(cadena, str), "La entrada debe ser una cadena de caracteres"
    assert (
        isinstance(posicion, int) and posicion >= 0
    ), "La posición debe ser un entero no negativo"
    assert (
        isinstance(cantidad, int) and cantidad >= 0
    ), "La cantidad debe ser un entero no negativo"

    subcadena = ""  # Inicializamos la subcadena vacía
    longitud_cadena = len(cadena)  # Obtenemos la longitud de la cadena original

    for i in range(
        cantidad
    ):  # Recorremos desde 0 hasta cantidad - 1, repetimos por la cantidad de caracteres a extraer
        indice_actual = (
            posicion + i
        )  # Calculamos el índice actual sumando la posición inicial y la iteración
        if (
            indice_actual < longitud_cadena
        ):  # Si el índice actual es menor que la longitud de la cadena
            subcadena += cadena[
                indice_actual
            ]  # Añadimos el carácter correspondiente a la subcadena
        else:
            break  # Si se supera la longitud de la cadena, se detiene el bucle

    return subcadena


def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion = int(input("Ingrese la posición inicial (entero no negativo): "))
    cantidad = int(
        input("Ingrese la cantidad de caracteres a extraer (entero no negativo): ")
    )

    subcadena_rebanadas = extraer_subcadena_rebanadas(cadena, posicion, cantidad)
    print(f"Subcadena extraída utilizando rebanadas: '{subcadena_rebanadas}'")

    subcadena_sin_rebanadas = extraer_subcadena_sin_rebanadas(
        cadena, posicion, cantidad
    )
    print(f"Subcadena extraída sin utilizar rebanadas: '{subcadena_sin_rebanadas}'")


if __name__ == "__main__":
    main()
