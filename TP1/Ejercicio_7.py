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


def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    
    # Se solicita una fecha al usuario para validar la funcion.
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    print(f"\nFecha ingresada: {dia}/{mes}/{anio}")
    dia_siguiente = diasiguiente(dia, mes, anio)
    print(f"El dia siguiente es: {dia_siguiente[0]}/{dia_siguiente[1]}/{dia_siguiente[2]}")

if __name__ == "__main__":
    main()
