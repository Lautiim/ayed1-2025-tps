def main():
    # Generamos el diccionario con comprension
    cuadrados = {n: n**2 for n in range(1, 21)}
    
    # Imprimimos el diccionario
    print("Diccionario de números y sus cuadrados:")
    print(cuadrados)
    
    # Opcionalmente, mostramos en formato mas legible
    print("\nLlaves y sus valores:")
    for clave, valor in cuadrados.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
