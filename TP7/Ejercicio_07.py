def mcd(x: int, y: int) -> int:
    """
    Calcula el MCD de dos numeros usando recursividad.

    Pre: x >= 0, y >= 0.

    Post: retorna MCD(x, y).
    """
    assert x >= 0 and y >= 0, "Los números deben ser no negativos."

    # MCD(X, X) = X
    if x == y:
        return x

    # MCD(X, Y) = MCD(Y, X) - aseguramos que x > y
    if x < y:
        return mcd(y, x)

    # Si X > Y => MCD(X, Y) = MCD(X-Y, Y)
    return mcd(x - y, y)


def mcd_lista(numeros: list[int]) -> int:
    """
    Calcula el MCD de todos los elementos de una lista recursivamente.

    Pre: numeros es una lista de enteros no negativos.

    Post: retorna MCD de todos los elementos.
    """
    # Caso base: lista vacia
    if len(numeros) == 0:
        return 0

    # Caso base: un solo elemento
    if len(numeros) == 1:
        return numeros[0]

    # Caso recursivo: MCD(X,Y,Z) = MCD(MCD(X,Y),Z)
    # Tomamos primer elemento y calculamos MCD con el resto
    return mcd(numeros[0], mcd_lista(numeros[1:]))


def main():
    print("=== Calcular MCD de dos números ===")
    try:
        x = int(input("Ingresá el primer número: "))
        y = int(input("Ingresá el segundo número: "))

        if x < 0 or y < 0:
            print("Los números deben ser no negativos.")
        else:
            resultado = mcd(x, y)
            print(f"MCD({x}, {y}) = {resultado}")
    except ValueError:
        print("Entrada inválida.")

    print("\n=== Calcular MCD de una lista ===")
    try:
        entrada = input("Ingresá números separados por espacios: ")
        numeros = [int(n) for n in entrada.split()]

        if any(n < 0 for n in numeros):
            print("Todos los números deben ser no negativos.")
        elif len(numeros) == 0:
            print("Debés ingresar al menos un número.")
        else:
            resultado = mcd_lista(numeros)
            print(f"MCD de {numeros} = {resultado}")
    except ValueError:
        print("Entrada inválida.")


if __name__ == "__main__":
    main()
