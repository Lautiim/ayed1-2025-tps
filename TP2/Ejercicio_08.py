def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    # Genaromos la lista de numeros impares entre 100 y 200, empezamos en 101 y vamos sumando de a 2
    lista_impares = [numero for numero in range(101, 200, 2)]
    print("Números impares entre 100 y 200:")

    print(f" {lista_impares}")
if __name__ == "__main__":
    main()