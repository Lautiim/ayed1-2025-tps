def eliminar_elementos_lista(lista_numeros: list[int], lista_a_eliminar: list[int]) -> None:
    """Funcion para eliminar de la lista original todos los elementos que se indiquen en la lista de eliminacion.

    Pre: Recibe 2 listas de enteros, la primera es la lista original y la segunda es la lista de eliminacion.

    Post: Remueve todos los elementos de la lista original que se encuentran en la lista de eliminacion.
    """
    # Validamos que las entradas sean listas
    assert isinstance(lista_numeros, list) and isinstance(lista_a_eliminar, list), "Ambos parámetros deben ser listas"
    # Validamos que las listas contengan solo enteros
    assert all(isinstance(x, int) for x in lista_numeros), "La lista_numeros debe contener solo enteros"
    assert all(isinstance(x, int) for x in lista_a_eliminar), "La lista_a_eliminar debe contener solo enteros"
    
    # Recorremos la lista con los valores a eliminar y eliminamos cada elemento de la lista original
    for elemento in lista_a_eliminar:
        while elemento in lista_numeros: # Mientras el elemento este en la lista, lo eliminamos
            lista_numeros.remove(elemento)

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    lista_original = [12, 25, 37, 25, 44, 37, 50, 25] # Lista de ejemplo
    valores_para_eliminar = [25, 37, 99] # Lista con los valores a eliminar

    print("Lista original:", lista_original)
    print("Valores a eliminar:", valores_para_eliminar)

    eliminar_elementos_lista(lista_original, valores_para_eliminar)

    print("\nLista resultado:", lista_original)

if __name__ == "__main__":
    main()