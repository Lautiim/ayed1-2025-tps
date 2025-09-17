def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    valido = False
    while not valido:
        entrada_A = int(input("Ingrese el valor de A: "))
        entrada_B = int(input("Ingrese el valor de B: "))
        if isinstance(entrada_A, int) and isinstance(entrada_B, int):
            A = entrada_A
            B = entrada_B
            if A <= B:
                valido = True
            else:
                print("El valor de A debe ser menor o igual que B. Intente nuevamente.")
        else:
            print("Por favor, ingrese numeros enteros.")

    # Generamos la lista de múltiplos de 7 que no son múltiplos de 5 entre A y B
    multiplos_de_7_no_de_5 = [numero for numero in range(A, B + 1) if numero % 7 == 0 and numero % 5 != 0]
    
    print(f"\nMúltiplos de 7 que no son múltiplos de 5 entre {A} y {B}:")
    print(multiplos_de_7_no_de_5)

if __name__ == "__main__":
    main()