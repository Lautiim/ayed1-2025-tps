def suma_naturales(n: int) -> int:
    """
    Funcion para calcular la suma de los primeros N números naturales recursivamente.

    Pre: n es un entero positivo.

    Post: retorna la suma 1 + 2 + ... + n.
    """
    if n <= 0:  # Caso base
        return 0

    return n + suma_naturales(n - 1)  # Caso recursivo


def main():
    try:
        n = int(input("Ingresá N (cantidad de números naturales a sumar): "))
        if n < 0:
            print("Por favor ingresá un número positivo.")
        else:
            resultado = suma_naturales(n)
            print(f"La suma de los primeros {n} números naturales es: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor ingresá un número entero.")


if __name__ == "__main__":
    main()
