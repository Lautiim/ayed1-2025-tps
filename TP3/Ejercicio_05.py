"""
Desarrollar  un  programa  que  permita  realizar  reservas  en  una  sala  de  cine  de  N 
filas con M butacas  por  cada fila. Desarrollar   las  siguientes  funciones  y utilizarlas 
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas 
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y 
se volverá a invocar luego de la misma con los estados actualizados.
reservar:  Deberá  recibir  una  matriz  y  la  butaca  seleccionada,  y  actualizará  la 
sala en caso de estar disponible dicha butaca. La función devolverá True/False 
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores 
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y  retornará cuántas buta-
cas desocupadas hay en la sala.
butacas_contiguas:  Buscará  la  secuencia  más  larga  de  butacas  libres  conti-
guas en una misma fila y devolverá las coordenadas de inicio de la misma.
"""
import random

def mostrar_butacas(sala: list[list[bool]]) -> None:
    """Muestra por pantalla el estado de cada una de las butacas del cine.

    Pre: Recibe una matriz de booleanos.

    Post: Muestra por pantalla el estado de cada una de las butacas del cine.
    """
    assert len(sala) > 0, "La sala no debe estar vacía."

    print("Estado de las butacas (L: Libre, R: Reservada):")
    for i, fila in enumerate(sala):
        fila_estado = ""
        for j, butaca in enumerate(fila):
            if butaca:
                fila_estado += "R "  # Butaca ocupada
            else:
                fila_estado += "L "  # Butaca libre
        print(f"Fila {i + 1}: {fila_estado.strip()}")

def reservar(sala: list[list[bool]], fila: int, columna: int) -> bool:
    """Funcion para eservar una butaca específica.

    Pre: Recibe la matriz de la sala, la fila y la columna.

    Post: Devuelve True si se pudo reservar
    """
    num_filas = len(sala)
    num_columnas = len(sala[0])

    # Validamos que las coordenadas estén dentro de la sala
    if not (0 <= fila < num_filas and 0 <= columna < num_columnas):
        assert("Error: Butaca fuera de los límites de la sala.")
        return False

    # Verificar si la butaca está libre
    if not sala[fila][columna]: # Si no estaba reservada
        sala[fila][columna] = True  # Reservar
        return True
    else:
        # Si ya estaba reservada
        return False

def cargar_sala(sala: list[list[bool]]) -> None:
    """Fuencion cargar con valores aleatorios (True/False) la matriz.

    Pre: Recibe la matriz de la sala.

    Post: La matriz es modificada con valores aleatorios.
    """
    assert len(sala) > 0, "La sala no debe estar vacía."
    
    num_filas = len(sala)
    num_columnas = len(sala[0])

    for i in range(num_filas):
        for j in range(num_columnas):
            # Asigna True (Reservado) o False (Libre) aleatoriamente
            sala[i][j] = random.choice([True, False])

def butacas_libres(sala: list[list[bool]]) -> int:
    """Funcion para consultar cuantas butacas desocupadas (False) hay en la sala.

    Pre: Recibe la matriz de la sala.

    Post: Devuelve la cantidad de butacas libres (False).
    """
    assert len(sala) > 0, "La sala no debe estar vacía."
    
    butacas_libres = 0
    
    for fila in sala: # Recorremos las filas de la sala
        for butaca in fila: # Recorremos las butacas de una fila
            if not butaca:  # Si la butaca esta libre
                butacas_libres += 1

    return butacas_libres

def butacas_contiguas(sala: list[list[bool]]) -> tuple[int, int] | None:
    """Funcion para buscar la secuencia más larga de butacas libres.

    Pre: Recibe la matriz de la sala.

    Post: Devuelve una tupla (fila, columna), las coordenadas de la racha más larga. Devuelve None si no hay ninguna butaca libre.
    """
    assert len(sala) > 0, "La sala no debe estar vacía."

    max_longitud = 0
    mejor_inicio = None  # (fila, columna)

    num_filas = len(sala)
    num_columnas = len(sala[0])

    for i in range(num_filas):
        longitud_actual = 0
        inicio_actual = 0

        for j in range(num_columnas):
            if not sala[i][j]:  # Si está libr
                if longitud_actual == 0:
                    inicio_actual = j  # Marcar el inicio de esta racha
                longitud_actual += 1
            else:  # Si está ocupada
                # Se rompió la racha, comparamos si fue la mejor hasta ahora
                if longitud_actual > max_longitud:
                    max_longitud = longitud_actual
                    mejor_inicio = (i, inicio_actual)
                longitud_actual = 0  # Reiniciar racha

        # En caso de que la fila termine con una racha de asientos libres
        if longitud_actual > max_longitud:
            max_longitud = longitud_actual
            mejor_inicio = (i, inicio_actual)

    return mejor_inicio

def main():
    sala = []  # Sala de cine
    filas = 5  # Número de filas
    columnas = 7  # Número de columnas

    # Inicializamos la sala con todas las butacas libre
    for i in range(filas):
        fila = [False for x in range(columnas)]
        sala.append(fila)

    # Cargamos la sala con reservas aleatorias
    cargar_sala(sala)

    # Mostramos el estado inicial de la sala
    mostrar_butacas(sala)

    libres = butacas_libres(sala)
    print(f"\nTotal de butacas libres: {libres}")

    mejor_racha = butacas_contiguas(sala)
    if mejor_racha:
        # Sumamos 1 para mostrar bien al usuario
        print(f"Mejor racha de asientos contiguos inicia en: Fila {mejor_racha[0] + 1}, Butaca {mejor_racha[1] + 1}")
    else:
        print("No hay butacas libres en la sala.")

    # Proceso de reserva
    print("\n--- Realizar una Reserva ---")
    try:
        # Pedimos al usuario (índices 1-based)
        fila_usuario = int(input(f"Ingrese la fila (1-{filas}): "))
        col_usuario = int(input(f"Ingrese la butaca (1-{columnas}): "))

        # Convertimos a índices 0-based para la función reservar
        fila_idx = fila_usuario - 1
        col_idx = col_usuario - 1

        if reservar(sala, fila_idx, col_idx):
            print(f"¡Reserva exitosa en Fila {fila_usuario}, Butaca {col_usuario}!")
        else:
            print(f"No se pudo reservar. La butaca Fila {fila_usuario}, Butaca {col_usuario} ya está ocupada o es inválida.")

    except ValueError:
        print("Error: Entrada inválida. Debe ingresar números.")

    # Se volverá a invocar [mostrar_butacas] luego de la misma
    mostrar_butacas(sala)
    print(f"\nTotal de butacas libres ahora: {butacas_libres(sala)}")

if __name__ == "__main__":
    main()