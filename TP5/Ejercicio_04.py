def imprimir_numeros_hasta_100000() -> None:
    """Funcion que imprime los números enteros del 1 al 100000, solicitando confirmación para detenerse al recibir Ctrl-C.

    Pre: No recibe parámetros.

    Post: Imprime los números del 1 al 100000 en la consola. Si el usuario presiona Ctrl-C,
    se le solicita confirmación para detener la ejecución del programa.
    """
    try:  # Capturamos la interrupción del teclado (Ctrl-C)
        for numero in range(1, 100001):
            print(numero)
    except (
        KeyboardInterrupt
    ):  # Si se presiona Ctrl-C, se solicita confirmación para detener la ejecución
        confirmar = (
            input("\n¿Desea realmente detener la ejecución? (s/n): ").strip().lower()
        )
        if confirmar == "s":
            print("Ejecución detenida por el usuario :D.")
        else:
            imprimir_numeros_hasta_100000()  # Reinicia la impresión si no se confirma


def main():
    imprimir_numeros_hasta_100000()


if __name__ == "__main__":
    main()
