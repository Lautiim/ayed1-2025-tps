def esta_ordenada_ascendente(lista_elementos: list) -> bool:
    """Funcion que devuelve True si la lista esta ordenada en forma ascendente,
    False en caso contrario (si no esta ordenada).

    Pre: Recibe una lista de elementos comparables.

    Post: Devuelve un booleano, True si la lista esta ordenada en forma ascendente, False de lo contrario.
    """
    # Validamos que la lista no este vacia
    assert len(lista_elementos) > 0, "La lista no puede estar vacia"
    # Validamos que la lista no sea una lista de tuplas
    assert not all(isinstance(i, tuple) for i in lista_elementos), "La lista no puede ser una lista de tuplas"
    # Validamos que la lista no sea una lista de listas
    assert not all(isinstance(i, list) for i in lista_elementos), "La lista no puede ser una lista de listas"
    # Validamos que la lista no sea una lista de diccionarios
    assert not all(isinstance(i, dict) for i in lista_elementos), "La lista no puede ser una lista de diccionarios"

    # Recorremos la lista y comparamos cada elemento con el siguiente
    for i in range(len(lista_elementos) - 1): # Recorremos hasta el penultimo elemento, porque comparamos con el elemento siguiente
        if lista_elementos[i] > lista_elementos[i + 1]: # Si el elemento actual es mayor que el siguiente
            return False
    return True

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")

    # Valores para probar la funcion
    numeros_ordenados = [2, 5, 8, 12]
    letras_desordenadas = ["A", "B", "C", "A"]
    numeros_con_repetidos = [3, 3, 7, 10]
    lista_vacia = []
    lista_un_elemento = [42]

    print(f"{numeros_ordenados} -> {esta_ordenada_ascendente(numeros_ordenados)}")
    print(f"{letras_desordenadas} -> {esta_ordenada_ascendente(letras_desordenadas)}")
    print(f"{numeros_con_repetidos} -> {esta_ordenada_ascendente(numeros_con_repetidos)}")
    print(f"{lista_vacia} -> {esta_ordenada_ascendente(lista_vacia)}")
    print(f"{lista_un_elemento} -> {esta_ordenada_ascendente(lista_un_elemento)}")

if __name__ == "__main__":
    main()