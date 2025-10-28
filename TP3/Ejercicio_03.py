import random

def rellenar_matriz(filas: int, columnas: int) -> list[list[int]]:
    """Función para rellenar una matriz de N x N con números enteros al azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla
    
    Pre: Recibe dos enteros positivos filas y columnas.

    Post: Devuelve una matriz de N x N con números enteros al azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
    """    
    assert filas > 0 and columnas > 0, "Las dimensiones de la matriz deben ser enteros positivos."
    assert filas.is_integer() and columnas.is_integer(), "Las dimensiones de la matriz deben ser enteros."
    assert filas == columnas, "La matriz debe ser cuadrada."

    # Calculamos el total de elementos y creamos una la lista de números disponibles
    # Por ejemplo, si n=3, total_elementos es 9, y la lista es [0, 1, ..., 8]
    total_elementos = filas ** 2
    numeros_disponibles = list(range(total_elementos))
    
    # Mezclamos la lista de números aleatoriamente
    random.shuffle(numeros_disponibles)
    
    # Creamos la matriz y la rellenamos
    matriz = []
    for i in range(filas):
        # Creamos una nueva fila vacía
        fila = []
        for j in range(columnas):
            numero = numeros_disponibles.pop() # Sacamos un número de la lista mezclada
            fila.append(numero)
        
        # Agregamos la fila completa a la matriz
        matriz.append(fila)
        
    return matriz

def main():
    matriz = rellenar_matriz(4, 4)
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()