def normalizar_lista_numeros(lista_numeros: list[int]) -> list[float]:
    """Funcion que normaliza una lista de numeros enteros a una lista de flotantes entre 0 y 1, donde la suma de todos los elementos es 1.0.

    Pre: Recibe una lista de enteros, no vacia.

    Post: Devuelve una lista de flotantes normalizada.
    """
    # Validamos que la lista no este vacia
    assert len(lista_numeros) > 0, "La lista no puede estar vacía"
    # Validamos que la lista contenga solo enteros
    assert all(isinstance(x, int) for x in lista_numeros), "La lista debe contener solo enteros"
    
    # Sumamos todos los elementos de la lista
    suma_elementos = sum(lista_numeros)
    lista_normalizada = [] # Lista donde se guarda la lista normalizada

    # Si la suma es 0, todos los elementos seran 0.0 para evitar division por cero je
    if suma_elementos == 0:
        lista_normalizada = [0.0 for _ in lista_numeros]
    else: # Si no, normalizamos cada elemento dividiendolo por la suma total
        for numero in lista_numeros:
            proporcion = numero / suma_elementos # Calculamos la proporcion del numero respecto a la suma total
            lista_normalizada.append(proporcion)

    return lista_normalizada

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    ejemplos = [
        [1, 1, 2],
        [5, 15, 10],
        [3, 3, 3, 3],
        [0, 0, 0]
    ]
    for ejemplo in ejemplos:
        print(f"Lista original: {ejemplo} ----- Lista normalizada: {normalizar_lista_numeros(ejemplo)}")

if __name__ == "__main__":
    main()