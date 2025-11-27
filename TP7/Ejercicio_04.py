def producto_por_sumas(a: int, b: int) -> int:
    """
    Funcion que calcula el producto de dos numeros mediante sumas sucesivas recurs0ivamente.

    Pre: a y b son numeros enteros.

    Post: retorna a * b.
    """
    # Caso base: si b es 0, el producto es 0
    if b == 0:
        return 0

    # Para numeros negativos numeros negativos
    if b < 0:
        return -producto_por_sumas(a, -b)  # Maneja b negativo

    # Caso recursivo: a + producto(a, b-1)
    return a + producto_por_sumas(a, b - 1)


def main():
    try:
        a = int(input("Ingresá el primer número: "))
        b = int(input("Ingresá el segundo número: "))
        resultado = producto_por_sumas(a, b)
        print(f"El producto de {a} × {b} = {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor ingresá números enteros.")


if __name__ == "__main__":
    main()
