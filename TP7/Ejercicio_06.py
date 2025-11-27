# Me trabe con esta funcion asi que pedi ayuda a Copilot para solucionarla
# Tenia desbordamiento de pila en A(3,7)
cache = {}  # Almacenamiento para memoizacion, la memoria de resultados previos


def ackermann(m: int, n: int) -> int:
    """
    Funcion de Ackermann con memoizacion.

    Pre: m >= 0, n >= 0.

    Post: retorna A(m, n).
    """
    # Revisar cache
    if (m, n) in cache:  # Si ya lo calcule antes
        return cache[(m, n)]  # Retorno el valor guardado

    if m == 0:
        resultado = n + 1
    elif n == 0:
        resultado = ackermann(m - 1, 1)
    else:
        resultado = ackermann(m - 1, ackermann(m, n - 1))

    # Guardar en cache
    cache[(m, n)] = resultado  # Almacenar el resultado calculado
    return resultado


def imprimir_tabla_ackermann():
    """
    Imprime una tabla con valores de Ackermann para m entre 0 y 3, n entre 0 y 7.

    Pre: ninguna.

    Post: muestra la tabla en consola.
    """
    print("Tabla de la función de Ackermann A(m, n)")
    print("\n    ", end="")

    # Encabezado de columnas (n)
    for n in range(8):
        print(f"n={n:2}", end="  ")
    print()
    print("    " + "-" * 48)

    # Filas (m)
    for m in range(4):
        print(f"m={m} |", end="")
        for n in range(8):
            valor = ackermann(m, n)
            print(f"{valor:4}", end="  ")
        print()


def main():
    imprimir_tabla_ackermann()


if __name__ == "__main__":
    main()
