def cargar_enteros_matriz(filas: int, columnas: int) -> list[list[int]]:
    """Funcion para cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.

    Pre: Recibe la cantidad de filas y columnas de la matriz.
    
    Post: Devuelve una matriz con los enteros cargados por el usuario.
    """
    assert filas > 0 and columnas > 0, "La cantidad de filas y columnas debe ser mayor a cero."
    assert isinstance(filas, int) and isinstance(columnas, int), "Las filas y columnas deben ser enteros."

    matriz = [] # Generamos una lista vacia
    for i in range(filas): # Recorremos la cantidad de filas
        fila = [] # Generamos una lista vacia para la fila
        for x in range(columnas): # Recorremos la cantidad de columnas
            valor = int(input(f"Ingrese el valor para la posición [{i}][{x}]: ")) # Pedimos el valor al usuario
            fila.append(valor) # Agregamos el valor a la fila
        matriz.append(fila) # Agregamos la fila a la matriz
    return matriz

def asc_filas_matriz(matriz: list[list[int]]) -> None:
    """Funcion para ordenar de forma ascendente cada fila de una matriz.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve una matriz con las filas ordenadas de forma ascendente.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros. :3"

    matriz_ordenada = [] # Generamos una lista vacia

    for fila in matriz: # Recorremos cada fila de la matriz
        matriz_ordenada.append(sorted(fila)) # Agregamos la fila ordenada a la matriz ordenada

    return matriz_ordenada

def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    """Funcion para intercambiar dos filas, cuyos números se reciben como parámetro.

    Pre: Recibe una matriz de enteros y dos índices de filas válidos.

    Post: Modifica la matriz intercambiando las filas indicadas.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."
    assert 0 <= fila1 < len(matriz), "El índice de fila1 está fuera de rango."
    assert 0 <= fila2 < len(matriz), "El índice de fila2 está fuera de rango."

    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1] # Intercambiamos las filas

def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> None:
    """Funcion para intercambiar dos columnas, cuyos números se reciben como parámetro.

    Pre: Recibe una matriz de enteros y dos índices de columnas válidos.

    Post: Modifica la matriz intercambiando las columnas indicadas.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."
    assert 0 <= col1 < len(matriz[0]), "El índice de col1 está fuera de rango."
    assert 0 <= col2 < len(matriz[0]), "El índice de col2 está fuera de rango."

    for fila in matriz: # Recorremos cada fila de la matriz
        fila[col1], fila[col2] = fila[col2], fila[col1] # Intercambiamos los elementos de las columnas

def trasponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """Funcion para trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)

    Pre: Recibe una matriz de enteros.

    Post: Devuelve la matriz traspuesta.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."

    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_traspuesta = [] # Generamos una lista vacia

    for j in range(columnas): # Recorremos las columnas
        nueva_fila = [] # Generamos una lista vacia para la nueva fila
        for i in range(filas): # Recorremos las filas
            nueva_fila.append(matriz[i][j]) # Agregamos el elemento a la nueva fila
        matriz_traspuesta.append(nueva_fila) # Agregamos la nueva fila a la matriz traspuesta

    return matriz_traspuesta

def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """Funcion para calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro

    Pre: Recibe una matriz de enteros y un índice de fila válido.

    Post: Devuelve el promedio de los elementos de la fila.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."
    assert 0 <= fila < len(matriz), "El índice de fila está fuera de rango."

    return sum(matriz[fila]) / len(matriz[fila]) # El promedio es la suma de los elementos dividido la cantidad de elementos

def promedio_impares_columna(matriz: list[list[int]], columna: int) -> float:
    """Funcion para calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve el promedio de los elementos impares en las columnas de índice impar.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."
    assert 0 <= columna < len(matriz[0]), "El índice de columna está fuera de rango."

    cantidad_impares = 0
    cantidad_elementos = 0

    for i in range(len(matriz)): # Recorremos las filas
        if matriz[i][columna] % 2 != 0: # Si el elemento es impar
            cantidad_impares += 1 # Incrementamos la cantidad de impares
        if matriz[i][columna] is not None: # Si el elemento no es None
            cantidad_elementos += 1 # Incrementamos la cantidad de elementos

    if cantidad_elementos == 0:
        return 0.0 # Contemplamos división por cero si no hay elementos

    return cantidad_impares / cantidad_elementos # El promedio es la suma de los impares dividido la cantidad de elementos

def es_simetrica_principal(matriz: list[list[int]]) -> bool:
    """Funcion para determinar si la matriz es simétrica con respecto a su diagonal principal.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve True si la matriz es simétrica, False en caso contrario.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        return False # Una matriz no cuadrada no puede ser simétrica

    for i in range(filas):
        for j in range(i + 1, columnas):
            if matriz[i][j] != matriz[j][i]:
                return False # Si encontramos un par de elementos que no son iguales, no es simétrica

    return True # Si no encontramos diferencias, es simétrica

def es_simetrica_secundaria(matriz: list[list[int]]) -> bool:
    """Funcion para determinar si la matriz es simétrica con respecto a su diagonal secundaria.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve True si la matriz es simétrica, False en caso contrario.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        return False # Una matriz no cuadrada no puede ser simétrica

    for i in range(filas):
        for j in range(columnas - i - 1):
            if matriz[i][j] != matriz[filas - j - 1][columnas - i - 1]:
                return False # Si encontramos un par de elementos que no son iguales, no es simétrica

    return True # Si no encontramos diferencias, es simétrica

def columnas_capicua(matriz: list[list[int]]) -> list[int]:
    """Funcion para determinar qué columnas de la matriz son palíndromos (capicúas), 
    devolviendo una lista con los números de las mismas

    Pre: Recibe una matriz de enteros.

    Post: Devuelve una lista con los índices de las columnas que son capicúa.
    """
    assert len(matriz) > 0 and len(matriz[0]) > 0, "La matriz no debe estar vacía."
    assert all(isinstance(fila, list) for fila in matriz), "La matriz debe ser una lista de listas."
    assert all(all(isinstance(elem, int) for elem in fila) for fila in matriz), "Todos los elementos de la matriz deben ser enteros."

    columnas_capicuas = [] # Generamos una lista vacia
    num_columnas = len(matriz[0])

    for j in range(num_columnas): # Recorremos las columnas
        columna = [matriz[i][j] for i in range(len(matriz))] # Obtenemos la columna
        # Verificamos si la columna es capicúa, comparándola con su reverso
        # [::-1] significa invertir la lista
        if columna == columna[::-1]: 
            columnas_capicuas.append(j) # Agregamos el índice de la columna capicúa

    return columnas_capicuas

def menu():
    """Funcion para mostrar el menú de opciones al usuario."""
    print("Seleccione una opción:")
    print("1. Cargar matriz")
    print("2. Ordenar filas de la matriz")
    print("3. Intercambiar filas")
    print("4. Intercambiar columnas")
    print("5. Trasponer matriz")
    print("6. Calcular promedio de una fila")
    print("7. Calcular porcentaje de impares en una columna")
    print("8. Verificar simetría respecto a diagonal principal")
    print("9. Verificar simetría respecto a diagonal secundaria")
    print("10. Listar columnas capicúa")
    print("11. Salir")

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    matriz = []

    while True:
        menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            filas = int(input("Ingrese la cantidad de filas: "))
            columnas = int(input("Ingrese la cantidad de columnas: "))
            matriz = cargar_enteros_matriz(filas, columnas)
            print("Matriz cargada:", matriz)
        elif opcion == '2':
            matriz = asc_filas_matriz(matriz)
            print("Matriz con filas ordenadas:", matriz)
        elif opcion == '3':
            fila1 = int(input("Ingrese el índice de la primera fila a intercambiar: "))
            fila2 = int(input("Ingrese el índice de la segunda fila a intercambiar: "))
            intercambiar_filas(matriz, fila1, fila2)
            print("Matriz después de intercambiar filas:", matriz)
        elif opcion == '4':
            col1 = int(input("Ingrese el índice de la primera columna a intercambiar: "))
            col2 = int(input("Ingrese el índice de la segunda columna a intercambiar: "))
            intercambiar_columnas(matriz, col1, col2)
            print("Matriz después de intercambiar columnas:", matriz)
        elif opcion == '5':
            matriz = trasponer_matriz(matriz)
            print("Matriz traspuesta:", matriz)
        elif opcion == '6':
            fila = int(input("Ingrese el índice de la fila para calcular el promedio: "))
            promedio = promedio_fila(matriz, fila)
            print(f"El promedio de la fila {fila} es: {promedio}")
        elif opcion == '7':
            columna = int(input("Ingrese el índice de la columna para calcular el porcentaje de impares: "))
            porcentaje = promedio_impares_columna(matriz, columna)
            print(f"El porcentaje de elementos impares en la columna {columna} es: {porcentaje:.2%}")
        elif opcion == '8':
            if es_simetrica_principal(matriz):
                print("La matriz es simétrica respecto a su diagonal principal.")
            else:
                print("La matriz no es simétrica respecto a su diagonal principal.")
        elif opcion == '9':
            if es_simetrica_secundaria(matriz):
                print("La matriz es simétrica respecto a su diagonal secundaria.")
            else:
                print("La matriz no es simétrica respecto a su diagonal secundaria.")
        elif opcion == '10':
            columnas_capicuas_list = columnas_capicua(matriz)
            print("Las columnas capicúa son:", columnas_capicuas_list)

if __name__ == "__main__":
    main()