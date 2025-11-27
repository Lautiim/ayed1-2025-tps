def contar_digitos(n: int) -> int:
    """
    Funcion para contar la cantidad de dígitos de un número entero sin usar strings.

    Pre: n es un número entero.

    Post: devuelve la cantidad de dígitos.
    """
    n = abs(n)  # Valor absoluto = evitar signo negativo

    if n < 10:  # Caso base: un solo dígito
        return 1

    return 1 + contar_digitos(n // 10)  # Caso recursivo


def main():
    try:
        numero = int(input("Ingresá un número entero: "))
        print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")
    except ValueError:
        print("Entrada inválida. Por favor ingresá un número entero.")


if __name__ == "__main__":
    main()
