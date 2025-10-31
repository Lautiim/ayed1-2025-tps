def cargar_lista_enteros() -> list[int]:
    """Función para cargar una lista con números enteros ingresados por el usuario hasta ingresar -1.

    Pre: No recibe parámetros.

    Post: Devuelve una lista de números enteros ingresados por el usuario, excluyendo el -1.
    """
    lista_enteros = []
    while True:
        try:
            numero = int(
                input("Ingrese un número entero (-1 para finalizar): ").strip()
            )
            if numero == -1:  # Condición para finalizar la carga
                break
            lista_enteros.append(numero)
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
    return lista_enteros


def buscar_elementos_en_lista(lista: list[int]) -> None:
    """Función que permite al usuario buscar elementos en la lista y muestra su posición.

    Pre: Recibe una lista de números enteros.

    Post: Permite al usuario ingresar números para buscar en la lista e imprime su posición.
    Si el número no está en la lista, imprime un mensaje de error. El proceso se aborta
    después de tres errores.
    """
    assert isinstance(lista, list), "El parámetro debe ser una lista."
    assert lista, "La lista está vacía."

    errores = 0
    while errores < 3:
        try:
            numero_buscar = int(
                input("Ingrese un número para buscar en la lista: ").strip()
            )
            posicion = lista.index(numero_buscar)
            print(f"El número {numero_buscar} se encuentra en la posición {posicion}.")
        except ValueError:
            errores += 1
            print(
                f"Error: El número {numero_buscar} no se encuentra en la lista. Intentos restantes: {3 - errores}"
            )
    if errores == 3:
        print("Se han alcanzado el máximo de intentos. Finalizando la búsqueda.")


def main():
    lista_enteros = cargar_lista_enteros()
    buscar_elementos_en_lista(lista_enteros)


if __name__ == "__main__":
    main()
