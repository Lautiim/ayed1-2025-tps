def es_capicua(cadena: str) -> bool:
    """Funcion para saber si una cadena es capicua, sin utilizar cadenas auxiliares ni rebanadas

    Pre: Recibe una cadena de caracteres

    Post: Devuelve True si la cadena es capicua, False en caso contrario
    """
    assert isinstance(cadena, str), "La entrada debe ser una cadena de caracteres"
    cadena = cadena.strip().lower()  # Normalizamos la cadena

    i = 0  # índice inicial
    j = len(cadena) - 1  # índice final
    while i < j:
        if cadena[i] != cadena[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    cadena = input("Ingrese una cadena: ")

    if es_capicua(cadena):
        print("La cadena es capicúa.")
    else:
        print("La cadena no es capicúa.")


if __name__ == "__main__":
    main()


def main():
    pass
