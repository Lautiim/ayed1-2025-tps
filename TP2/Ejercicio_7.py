def intercalar_listas(lista1: list, lista2: list) -> None:
    """Funcion para intercalar los elementos de una lista (lista2) dentro de otra (lista1) en posiciones impares.

    Pre: Recibe dos listas de enteros, donde lista1 tiene al menos el doble de elementos que lista2.
    
    Post: Modifica la lista1 insertando los elementos de lista2 en las posiciones impares.
    """

    for i in range(len(lista2)):
        # Inserta el elemento de lista2 en la posición impar correspondiente de lista1
        lista1[i*2+1:i*2+1] = lista2[i:i+1]

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    lista_principal = [8, 1, 3]
    lista_a_intercalar = [5, 9, 7]
    print("Lista original:", lista_principal)
    print("Lista a intercalar:", lista_a_intercalar)
    intercalar_listas(lista_principal, lista_a_intercalar)
    print("Lista intercalada:", lista_principal)

if __name__ == "__main__":
    main()