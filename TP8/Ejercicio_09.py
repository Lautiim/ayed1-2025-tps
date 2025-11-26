def main():
    # Pedimos el numero
    try:
        n = int(input("Ingresá un número entero: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return
    
    # Generamos la tabla de multiplicar por comprension
    tabla = {i: n * i for i in range(1, 13)}
    
    # Mostramos con formato simple
    print(f"\nTabla de multiplicar del {n}:")
    print("-" * 30)
    for i, resultado in tabla.items():
        print(f"{n} x {i:2} = {resultado}")


if __name__ == "__main__":
    main()
