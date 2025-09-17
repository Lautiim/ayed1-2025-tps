import random

def crear_lista_aleatoria(cant_elementos: int) -> list:
    """Funcion para crear una lista de N números aleatorios del 1 al 100.

    Pre: Recibe un entero positivo que indica la cantidad de elementos a generar.

    Post: Devuelve una lista con los números aleatorios generados.
    """
    # Validamos que eltipo de dato sea correcto
    assert isinstance(cant_elementos, int), "La cantidad de elementos debe ser un entero."
    # Validamos que la cantidad de elementos sea positiva
    assert cant_elementos > 0, "La cantidad de elementos debe ser un entero positivo."

    # Se genera la lista de números aleatorios
    return [random.randint(1, 100) for _ in range(cant_elementos)]

def contiene_repetidos(lista: list) -> bool:
    """Funcion para verificar si una lista contiene elementos repetidos.

    Pre: Recibe una lista de elementos, no puede estar vacia.

    Post: Devuelve True si la lista contiene elementos repetidos, False sino contrario.
    """
    # Validamos que el tipo de dato sea correcto
    assert isinstance(lista, list), "El parámetro debe ser una lista."
    # Validamos que la lista no este vacia
    assert len(lista) > 0, "La lista no puede estar vacía."

    # Recorremos la lista y verificamos si hay elementos repetidos
    for i in range(len(lista)):
        if lista[i] in lista[i+1:]:
            return True
        else:
            return False

def elementos_unicos(lista: list) -> list:
    """Funcion para obtener una lista con los elementos unicos de una lista dada.
    
    Pre: Obtiene una lista de elementos, no puede estar vacia.

    Post: Devuelve una lista con los elementos unicos de la lista original.
    """
    # Validamos que el tipo de dato sea correcto
    assert isinstance(lista, list), "El parámetro debe ser una lista."
    # Validamos que la lista no este vacia
    assert len(lista) > 0, "La lista no puede estar vacía."

    return list(set(lista))

def main():
    """Funcion principal del programa"""
    print("--------- Bienvenido ---------")
    largo_lista = 10

    lista_aleatoria = crear_lista_aleatoria(largo_lista)
    print("Lista generada:", lista_aleatoria)
    
    if contiene_repetidos(lista_aleatoria):
        print("\nLa lista contiene elementos repetidos.")
    else:
        print("\nLa lista no contiene elementos repetidos.")

    lista_unicos = elementos_unicos(lista_aleatoria)
    print("Lista de elementos únicos:", lista_unicos)

if __name__ == "__main__":
    main()