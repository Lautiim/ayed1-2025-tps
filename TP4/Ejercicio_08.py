def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """Función que devuelve una subcadena con los últimos N caracteres de una cadena dada

    Pre: Recibe una cadena de caracteres y un entero N que indica la cantidad de caracteres a extraer

    Post: Devuelve la subcadena con los últimos N caracteres
    """
    assert isinstance(cadena, str), "La entrada debe ser una cadena de caracteres"
    assert isinstance(n, int) and n >= 0, "N debe ser un entero no negativo"

    longitud_cadena = len(cadena)  # Obtenemos la longitud de la cadena original

    if n > longitud_cadena:
        # Si N es mayor que la longitud de la cadena, devolvemos la cadena completa
        return cadena
    else:
        # Devolvemos los últimos N caracteres usando slicing
        return cadena[longitud_cadena - n :]


def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    n = int(input("Ingrese el valor de N (entero no negativo): "))
    resultado = ultimos_n_caracteres(cadena, n)
    print(f"Los últimos {n} caracteres son: '{resultado}'")


if __name__ == "__main__":
    main()
