def es_bisiesto(anio: int) -> bool:
    """ Verifica si un año es bisiesto 
    
        Pre: Recibe un numero entero.

        Post: Devuelve True si el año es bisiesto, False en caso contrario.

    """

    # Un año es bisiesto si es divisible por 4 y no es divisible por 100 pero si lo es si es divisible por 400.
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else: # En caso de no cumplir estas condiciones es porque no es bisiesto.
        return False

def diasiguiente(dia: int, mes: int, anio: int) -> str:
    """Devuelve el dia siguiente a la fecha ingresada.

    Pre: Recibre tres enteros positivos, que representan: dia, mes y año.

    Post: Devuelve tres enteros positivos, que representan: dia, mes y año del dia siguiente.
    """
    bisiesto = es_bisiesto(anio) # Llamamos a la funcion para saber si el año es bisiesto, esto se utilizara a futuro

    # Verificamos que los valores de dia ingresados sean positivos
    if dia < 1 or mes < 1 or anio < 1:
        raise ValueError("El dia, mes y año deben ser enteros positivos.")
    # Verificamos que el mes sea valido
    if mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12.")
    # Verificamos que el mes sea valido segun el mes
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12 : # Meses con 31 dias
            if dia > 31:
                raise ValueError("El dia debe estar entre 1 y 31 para el mes ingresado.")
        case 4 | 6 | 9 | 11: # Meses con 30 dias
            if dia > 30:
                raise ValueError("El dia debe estar entre 1 y 30 para el mes ingresado.")
        case 2: # Febrero, es especial porque depende si es bisiesto o no
            if bisiesto: # Si es bisiesto, tiene 29 dias
                if dia > 29:
                    raise ValueError("El dia debe estar entre 1 y 29 para el mes de febrero en un año bisiesto.")
            else: # Caso contrario, tiene 28 dias
                if dia > 28: 
                    raise ValueError("El dia debe estar entre 1 y 28 para el mes de febrero en un año no bisiesto.")
        case _:
            raise ValueError("Mes inválido")

    # Calculamos el dia siguiente en base al mes y si es bisiesto o no
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10: # Meses con 31 dias
            if dia < 31:
                dia += 1
            else: # En caso de ser 31, sumamos 1 y pasamos al siguiente mes
                dia = 1
                mes += 1
        case 4 | 6 | 9 | 11: # Meses con 30 dias
            if dia < 30:
                dia += 1
            else: # En caso de ser 30, sumamos 1 y pasamos al siguiente mes
                dia = 1
                mes += 1
        case 2: # Febrero, es especial porque depende si es bisiesto o no
            if bisiesto: # Si es bisiesto
                if dia < 29:
                    dia += 1
                else: # En caso de ser 29, sumamos 1 y pasamos a marzo
                    dia = 1
                    mes += 1
            else: # Si no bisiesto
                if dia < 28:
                    dia += 1
                else: # En caso de ser 28, sumamos 1 y pasamos a marzo
                    dia = 1
                    mes += 1
        case 12: # Diciembre
            if dia < 31:
                dia += 1
            else: # En caso de ser 31, sumamos 1 y pasamos a enero del proximo año
                dia = 1
                mes = 1
                anio += 1
    
    return dia, mes, anio


def sumar_dias(dia, mes, anio, dias_a_sumar):
    """Suma la cantidad de dias indicados, a una fecha dada. Limitandose a utilizar la funcion diasiguiente().
    
    Pre: Recibe 4 enteros positivos, que representan: dia, mes, año y la cantidad de dias a sumar.

    Post: Devuelve tres enteros positivos, que representan: dia, mes y año de la nueva fecha.
    
    """
    for _ in range(dias_a_sumar): # Recorremos la cantidad de dias a sumar
        dia, mes, anio = diasiguiente(dia, mes, anio) # Obtenemos el dia siguiente
    return dia, mes, anio # Al finalizar, devolvemos la nueva fecha


def dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2):
    """Calcula la cantidad de días entre dos fechas. Limitandose a utilizar la función diasiguiente().

    Pre: Recibe 6 enteros positivos, que representan: dia1, mes1, anio1 y dia2, mes2, anio2.

    Post: Devuelve un entero positivo, que representa la cantidad de días entre las dos fechas.

    """

    # Validamos que la segunda fecha es posterior a la primera
    if (anio2 + mes2, dia2) < (anio1 + mes1, dia1):
        raise ValueError("La segunda fecha debe ser posterior a la primera.")

    contador = 0 # Se utiliza para contar la cantidad de dias entre las dos fechas
    
    fecha_actual = (dia1, mes1, anio1)
    fecha_final = (dia2, mes2, anio2)
    
    while fecha_actual != fecha_final: # Mientras la fecha actual no sea igual a la fecha final
        fecha_actual = diasiguiente(*fecha_actual) # Obtenemos el dia siguiente
        contador += 1
    return contador


def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    
    # Valores para pruebas
    dia_inicio = 28
    mes_inicio = 2
    anio_inicio = 2020 
    dia_final = 5
    mes_final = 3
    anio_final = 2020
    dias_a_sumar = 10

    # Probamos la función diasiguiente():
    siguiente_dia = diasiguiente(dia_inicio, mes_inicio, anio_inicio)
    print(f"El día siguiente a {dia_inicio}/{mes_inicio}/{anio_inicio} es: {siguiente_dia[0]}/{siguiente_dia[1]}/{siguiente_dia[2]}")

    # Probamos la función dias_entre_fechas():
    dias = dias_entre_fechas(dia_inicio, mes_inicio, anio_inicio, dia_final, mes_final, anio_final)
    print(f"Días entre {dia_inicio}/{mes_inicio}/{anio_inicio} y {dia_final}/{mes_final}/{anio_final}: {dias}")

    # Probamos la función sumar_dias():
    nueva_fecha = sumar_dias(dia_inicio, mes_inicio, anio_inicio, dias_a_sumar)
    print(f"Fecha después de sumar {dias_a_sumar} días a {dia_inicio}/{mes_inicio}/{anio_inicio}: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")

if __name__ == "__main__":
    main()
