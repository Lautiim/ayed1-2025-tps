def sumar_cadenas_numeros(cadena1: str, cadena2: str) -> float:
    """Suma dos números reales representados como cadenas de caracteres.

    Pre: Recibe dos cadenas de caracteres que deberían contener números reales.

    Post: Devuelve la suma de los dos números como un número real.
    Si alguna de las cadenas no contiene un número válido, devuelve -1.
    """
    assert isinstance(
        cadena1, str
    ), "La primera entrada debe ser una cadena de caracteres."
    assert isinstance(
        cadena2, str
    ), "La segunda entrada debe ser una cadena de caracteres."

    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        return numero1 + numero2
    except ValueError:
        return -1.0  # Devolvemos -1 si hay un error de conversión


def main():
    cadena1 = input("Ingrese el primer número real: ")
    cadena2 = input("Ingrese el segundo número real: ")
    resultado = sumar_cadenas_numeros(cadena1, cadena2)
    if resultado == -1.0:
        print("Error: Una o ambas cadenas no contienen un número válido.")
    else:
        print(f"La suma de los números es: {resultado}")


if __name__ == "__main__":
    main()
