from tabulate import tabulate


def main():
    # Pedimos el numero
    try:
        n = int(input("Ingresá un número entero: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return
    
    # Generamos la tabla de multiplicar por comprension
    tabla = {i: n * i for i in range(1, 13)}
    
    # Preparamos los datos para tabulate
    datos = [[f"{n} x {i}", resultado] for i, resultado in tabla.items()]
    
    # Mostramos con formato de tabla
    print(f"\nTabla de multiplicar del {n}:")
    print(tabulate(datos, headers=["Operación", "Resultado"], tablefmt="grid"))


if __name__ == "__main__":
    main()
