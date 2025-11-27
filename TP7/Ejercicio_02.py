def binario_a_decimal(binario: int) -> int:
    """
    Funcion para convertir un numero binario a decimal.

    Pre: "binario" es un entero que representa un numero binario.

    Post: retorna el valor decimal equivalente.
    """
    if binario == 0:  # Caso base
        return 0

    # Caso recursivo: último dígito + resto * 2
    ultimo_digito = binario % 10
    resto = binario // 10
    return ultimo_digito + 2 * binario_a_decimal(resto)


def main():
    try:
        binario = int(input("Ingresá un número binario: "))
        decimal = binario_a_decimal(binario)
        print(f"El número binario {binario} en decimal es: {decimal}")
    except ValueError:
        print("Entrada inválida. Por favor ingresá un número binario válido.")


if __name__ == "__main__":
    main()
