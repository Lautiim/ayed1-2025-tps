"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re-
presenta el día de la semana y cada fila a una de sus fábricas. Ejemplo:
(Lunes) (Martes) (Miércoles) (Jueves) (Viernes) (Sábado)
0 1 2 3 4 5
(Fábrica 1) 0 23 150 20 120 25 150
(Fábrica 2) 1 40 75 80 0 80 35
( . . . ) . . . . . . . . . . . . . . . . . .
(Fábrica 
n) 3 80 80 80 80 80 80
 Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una 
semana,  considerando  que  la  capacidad  máxima  de  fabricación  es  de  150 
unidades  por  día  y  puede  suceder  que  en  ciertos  días  no  se  fabrique  nin-
guna. 
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fábrica.
"""
import random

def generar_matriz_bicicletas(fabricas: int, dias: int) -> list[list[int]]:
    """Genera una matriz con datos aleatorios para N fábricas durante una semana.
    
    Pre: Recibe dos enteros positivos, fabricas y dias.

    Post: Devuelve una matriz donde cada fila representa una fábrica y cada columna un día,
    con valores aleatorios desde 0 hasta 150.
    """
    assert fabricas > 0 and dias > 0, "El número de fábricas y días debe ser positivo."
    assert fabricas.is_integer() and dias.is_integer(), "El número de fábricas y días debe ser un entero."
    
    matriz = [] # Generamos la matriz vacía

    for i in range(fabricas): # Recorremos cada fábrica
        fila = [random.randint(0, 150) for x in range(dias)] # Generamos una fila con datos aleatorios por dia, por comprensión
        matriz.append(fila) # Agregamos la fila a la matriz
    
    return matriz

def consultar_total_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """Calcula la cantidad total de bicicletas fabricadas por cada fábrica.
    
    Pre: Recibe una matriz de enteros.

    Post: Devuelve una lista con el total de bicicletas por fábrica.
    """
    assert len(matriz) > 0, "La matriz no debe estar vacía."

    totales = [] # Generamos la lista vacía para los totales
    for fila in matriz: # Recorremos cada fila de la matriz
        totales.append(sum(fila)) # Calculamos el total de la fila y lo agregamos a la lista de totales
    return totales

def fabrica_mas_productiva(matriz: list[list[int]]) -> tuple[int, int, int]:
    """Determina la fábrica más productiva en un solo día.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve una tupla con el índice de la fábrica, el día y la cantidad producida.
    """
    assert len(matriz) > 0, "La matriz no debe estar vacía."

    max_fabrica = -1 # Índice de la fábrica más productiva  
    max_dia = -1 # Índice del día más productivo
    max_produccion = -1 # Cantidad máxima producida en un solo día

    for i, fila in enumerate(matriz): # Recorremos cada fila de la matriz
        for j, produccion in enumerate(fila): # Recorremos cada día de la fábrica
            if produccion > max_produccion: # Si la producción es mayor a la máxima registrada
                max_produccion = produccion # Actualizamos la máxima producción
                max_fabrica = i # Actualizamos la fábrica
                max_dia = j # Actualizamos el día

    return (max_fabrica, max_dia, max_produccion)

def dia_mas_productivo(matriz: list[list[int]]) -> tuple[int, int]:
    """Determina el día más productivo considerando todas las fábricas combinadas.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve una tupla con el índice del día y la cantidad total producida.
    """
    assert len(matriz) > 0, "La matriz no debe estar vacía."

    dias = len(matriz[0]) # Número de días
    max_dia = -1 # Índice del día más productivo
    max_produccion = -1 # Cantidad máxima producida en un día

    for j in range(dias): # Recorremos cada día
        produccion_dia = sum(matriz[i][j] for i in range(len(matriz))) # Sumamos la producción de todas las fábricas en ese día
        if produccion_dia > max_produccion: # Si la producción del día es mayor a la máxima registrada
            max_produccion = produccion_dia # Actualizamos la máxima producción
            max_dia = j # Actualizamos el día

    return (max_dia, max_produccion)

def menor_cantidad_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """Crea una lista por comprensión con la menor cantidad fabricada por cada fábrica.

    Pre: Recibe una matriz de enteros.

    Post: Devuelve una lista con la menor cantidad por fábrica.
    """
    assert len(matriz) > 0, "La matriz no debe estar vacía."

    menores = [min(fila) for fila in matriz] # Lista por comprensión para obtener el mínimo de cada fila
    return menores

def main():
    # Generacion de la matriz
    fabricas = 5
    dias = 7
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    matriz = generar_matriz_bicicletas(fabricas, dias)

    # Mostrar la matriz
    print("Matriz de producción de bicicletas (Fábricas x Días):")
    for i, fila in enumerate(matriz):
        print(f"Fábrica {i + 1}: {fila}")

    # Consultar total por fábrica 
    totales = consultar_total_por_fabrica(matriz)
    for i, total in enumerate(totales):
        print(f"Total Fábrica {i + 1}: {total}")

    # Fabrica más productiva en un solo día
    fabrica, dia, produccion = fabrica_mas_productiva(matriz)
    print(f"Fábrica más productiva en un solo día: Fábrica {fabrica + 1}, {dias_semana[dia]}, Producción {produccion}")

    # Día más productivo considerando todas las fábricas
    dia, produccion = dia_mas_productivo(matriz)
    print(f"Día más productivo considerando todas las fábricas: {dias_semana[dia]}, Producción {produccion}")

    # Menor cantidad por fábrica
    menores = menor_cantidad_por_fabrica(matriz)
    for i, menor in enumerate(menores):
        print(f"Menor cantidad Fábrica {i + 1}: {menor}")

if __name__ == "__main__":
    main()