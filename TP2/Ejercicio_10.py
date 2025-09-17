import random

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    # Solicitamos al usuario la cantasdd de numeros aleatorios a generar
    cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    # Generamos la cantidad indicada de numeros aleatorios entre 1 y 100
    lista_aleatoria = [random.randint(1, 100) for _ in range(cantidad_numeros)]
    # Filtramos los numeros impares utilizando filter y un lambda para la condicion de impar
    lista_impares = list(filter(lambda x: x % 2 != 0, lista_aleatoria))

    # Mostramos las listas por pantalla
    print("Lista de numeros aleatorios:")
    print(lista_aleatoria)
    print("Lista de nmeros impares:")
    print(lista_impares)

if __name__ == "__main__":
    main()