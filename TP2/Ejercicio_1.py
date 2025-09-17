import random
from typing import List # Importamos List para definir listas con tipos especificos

def crear_lista_aleatoria() -> List[int]:
    """Funcion para cargar una lista de números aleatorios de 4 cifras. La cantidad de elementos también es aleatoria de dos numeros, entre 10 y 99.

    Pre: Sin precondiciones.

    Post: Retorna una lista de enteros con valores de entre 1000 y 9999.
    """
    cantidad_elementos = random.randint(10, 99) # Definimos la cantidad de elementos aleatoriamente 
    resultado = [] # Lista donde se almacenan los numeros aleatorios
    
    for _ in range(cantidad_elementos): # Recorremos la cantidad de elementos
        resultado.append(random.randint(1000, 9999))

    return resultado

def calcular_producto(lista: List[int]) -> int:
    """Funcion que devuelve el producto de todos los elementos de la lista.

    Pre: Lista de enteros, no puede estar vacia.

    Post: Retorna un entero, que es el producto de todos los elementos de la lista.
    """
    # validamos que la lista no este vacia
    assert len(lista) > 0, "La lista no puede estar vacia"

    producto = 1

    for elem in lista:
        producto *= elem
    
    return producto

def quitar_todos(lista: List[int], elemento: int) -> List[int]:
    """Funcion que elimina todas las apariciones de un elemento en la lista.

    Pre: Una lista de enteros y un entero que eliminar

    Post: Retorna la lista ingresada sin las apariciones del elemento.
    """
    # Validamos que la lista no este vacia
    assert len(lista) > 0, "La lista no puede estar vacia"
    # Validamos que el elemento a eliminar sea un entero
    assert isinstance(elemento, int), "El elemento a eliminar debe ser un entero"
    # Validamos que el elemento a eliminar este en la lista
    assert elemento in lista, "El elemento a eliminar no se encuentra en la lista"

    # Recorremos la lista y eliminamos todas las apariciones del elemento
    i = 0 # Indice para recorrer la lista
    while i < len(lista): # Mientras el indice sea menor que la longitud de la lista
        if lista[i] == elemento: # Si el elemento en la posicion i es igual al elemento a eliminar
            lista.pop(i) # Eliminamos el elemento en la posicion i
        else:
            i += 1
    return lista

def es_capicua(lista: List[int]) -> bool:
    """Funcion para verificar si el contenido de una lista es capicúa.
    Capicúa: Se lee igual de izquierda a derecha que de derecha a izquierda.

    Pre: Recibe una lista de enteros, no vacia.

    Post: Devuelve un booleano, True si la lista es capicúa, False en caso contrario.
    """
    # Validamos que la lista no este vacia
    assert len(lista) > 0, "La lista no puede estar vacia"

    # Recorremos la lista desde ambos extremos hacia el centro
    izquierda, derecha = 0, len(lista) - 1

    # Mientras los indices no se crucen
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]: # Si los elementos en las posiciones no coinciden, no es capicua
            return False
        
        izquierda += 1
        derecha -= 1
    return True

def menu() -> None:
    """Funcion para mostrar el menu de opciones."""
    print("Seleccione una opción:")
    print("1. Calcular producto de la lista")
    print("2. Quitar todas las apariciones de un elemento")
    print("3. Verificar si la lista es capicúa")
    print("4. Salir")

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")

    # Creacion de la lista aleatoria
    numeros = crear_lista_aleatoria()
    print("Lista generada:")
    print(numeros)

    while True:
        menu()
        opcion = input("Ingrese una opción (1-4): ")

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida. Intente nuevamente.\n")

        if opcion == "1":
            resultado_producto = calcular_producto(numeros)
            print(f"\nProducto de todos los números: {resultado_producto}\n")
        elif opcion == "2":
            valor_str = input("\nIngrese un número a quitar de la lista: ")
            if not valor_str.isdigit():
                print("Entrada inválida. Debe ingresar un número entero.")
                break
            valor = int(valor_str)
            nueva_lista = quitar_todos(numeros[:], valor)
            print("Lista despues de quitar el valor:")
            print(nueva_lista)
        elif opcion == "3":
            if es_capicua(numeros):
                print("\nLa lista es capicúa.\n")
            else:
                print("\nLa lista no es capicúa.\n")
        elif opcion == "4":
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()