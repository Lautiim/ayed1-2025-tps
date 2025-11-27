def resto_por_restas(dividendo: int, divisor: int) -> int:
    """
    Funcion que calcula el resto de la division usando restas sucesivas recursivamente.

    Pre: dividendo >= 0, divisor > 0.

    Post: retorna dividendo % divisor.
    """
    # Caso base: si dividendo es menor que divisor, ese es el resto
    if dividendo < divisor:
        return dividendo

    # Caso recursivo: restamos divisor y continuamos
    return resto_por_restas(dividendo - divisor, divisor)


def main():
    try:
        dividendo = int(input("Ingresá el dividendo: "))
        divisor = int(input("Ingresá el divisor: "))

        if divisor <= 0:
            print("El divisor debe ser mayor que 0.")
        elif dividendo < 0:
            print("El dividendo debe ser no negativo.")
        else:
            resultado = resto_por_restas(dividendo, divisor)
            print(f"El resto de {dividendo} ÷ {divisor} = {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor ingresá números enteros.")


if __name__ == "__main__":
    main()
