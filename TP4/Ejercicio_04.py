def entero_a_romano(numero: int) -> str:
    """Función para convertir un número entero en números romanos

    Pre: Recibe un número entero entre 0 y 3999

    Post: Devuelve un String con la representación en números romanos
    """
    assert isinstance(numero, int), "La entrada debe ser un número entero"
    assert 0 <= numero <= 3999, "El número debe estar entre 0 y 3999"

    valores_romanos = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    romano = ""
    for valor in sorted(
        valores_romanos.keys(), reverse=True
    ):  # Recorremos los valores de mayor a menor, por eso reverse=True
        while numero >= valor:  # Mientras el número sea mayor o igual al valor actual
            romano += valores_romanos[
                valor
            ]  # Añadimos el símbolo romano correspondiente
            numero -= valor  # Restamos el valor al número

    return romano


def main():
    numero = int(input("Ingrese un número entero entre 0 y 3999: "))
    romano = entero_a_romano(numero)
    print(f"El número {numero} en números romanos es: {romano}")

    print(f"\n¿En qué cambiaría la función si el rango de valores fuese diferente?")
    print(
        f"Si el rango de valores fuese diferente, habría que ajustar el diccionario de valores_romanos. \nPor ejemplo, si se quisiera incluir números mayores a 3999, se necesitarían símbolos adicionales."
    )


if __name__ == "__main__":
    main()
