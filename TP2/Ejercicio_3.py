def generar_lista_cuadrados() -> list[int]:
    """Funcion para generar una lista con los cuadrados de los números entre 1 y un valor indicado dado por el usuario.

    Pre: Ninguna precondicion.

    Post: Devuelve una lista de enteros con los cuadrados desde 1 hasta el numero ingresado.
    """
    final = int(input("\nIngrese el valor hasta el cual desea calcular los cuadrados: "))
    while final < 1:
        print("El valor debe ser un entero positivo mayor a 0.")
        final = int(input("Ingrese el valor hasta el cual desea calcular los cuadrados: "))
    
    lista_cuadrados = [] # Lista para almacenar los cuadrados

    # Recoremos los valores desde 1 hasta el valor ingresado.
    for valor in range(1, final + 1):
        cuadrado = valor ** 2 # Calculamos el cuadrado
        lista_cuadrados.append(cuadrado) # Y lo agregamos a la lista
    return lista_cuadrados

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    lista_de_cuadrados = generar_lista_cuadrados()
    
    print("\nLos ultimos 10 valores de la lista de cuadrados son:")
    print(lista_de_cuadrados[-10:])

if __name__ == "__main__":
    main()