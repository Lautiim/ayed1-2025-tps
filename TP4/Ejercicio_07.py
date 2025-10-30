"""Escribir  una  función  para  eliminar  una  subcadena  de  una  cadena  de  caracteres,  a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""


def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """Función para eliminar una subcadena utilizando rebanadas

    Pre: Recibe una cadena de caracteres, la posición inicial y la cantidad de caracteres a eliminar

    Post: Devuelve la cadena resultante despues de eliminar la subcadena
    """
    assert isinstance(cadena, str), "La entrada debe ser una cadena de caracteres"
    assert (
        isinstance(posicion, int) and posicion >= 0
    ), "La posición debe ser un entero no negativo"
    assert (
        isinstance(cantidad, int) and cantidad >= 0
    ), "La cantidad debe ser un entero no negativo"

    # Usamos rebanadas para construir la nueva cadena sin la subcadena
    return cadena[:posicion] + cadena[posicion + cantidad :]


def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """Función para eliminar una subcadena sin utilizar rebanadas

    Pre: Recibe una cadena de caracteres, la posición inicial y la cantidad de caracteres a eliminar

    Post: Devuelve la cadena resultante tras eliminar la subcadena
    """
    assert isinstance(cadena, str), "La entrada debe ser una cadena de caracteres"
    assert (
        isinstance(posicion, int) and posicion >= 0
    ), "La posición debe ser un entero no negativo"
    assert (
        isinstance(cantidad, int) and cantidad >= 0
    ), "La cantidad debe ser un entero no negativo"

    resultado = ""  # Inicializamos el resultado vacío
    longitud_cadena = len(cadena)  # Obtenemos la longitud de la cadena original

    for i in range(longitud_cadena):  # Recorremos cada índice de la cadena original
        if i < posicion or i >= posicion + cantidad:
            # Si el índice está fuera del rango de la subcadena a eliminar
            resultado += cadena[i]  # Añadimos el carácter a la cadena resultante

    return resultado


def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    posicion = int(input("Ingrese la posición inicial (entero no negativo): "))
    cantidad = int(
        input("Ingrese la cantidad de caracteres a eliminar (entero no negativo): ")
    )

    resultado_rebanadas = eliminar_subcadena_rebanadas(cadena, posicion, cantidad)
    print(f"Cadena resultante utilizando rebanadas: {resultado_rebanadas}")

    resultado_sin_rebanadas = eliminar_subcadena_sin_rebanadas(
        cadena, posicion, cantidad
    )
    print(f"Cadena resultante sin utilizar rebanadas: {resultado_sin_rebanadas}")


if __name__ == "__main__":
    main()
