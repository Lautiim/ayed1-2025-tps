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

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """ Verifica si una fecha es valida

        Pre: Recibe tres numeros enteros que representan una fecha (dia, mes, año).

        Post: Devuelve True si la fecha es valida, False en caso contrario.

    """
    
    # Se verifica que los numeros sean enteros
    assert(isinstance(dia, int)), "Los numeros deben ser enteros"
    assert(isinstance(mes, int)), "Los numeros deben ser enteros"
    assert(isinstance(anio, int)), "Los numeros deben ser enteros"

    if (mes >= 1 and mes <= 12): # Se comprueba que el mes sea valido (1-12)
        match mes: # Se comprueba el mes
            case 1 | 3 | 5 | 7 | 8 | 10 | 12: # Meses con 31 dias
                if (dia >= 1 and dia <= 31):
                    return True
                else:
                    return False
            case 4 | 6 | 9 | 11: # Meses con 30 dias
                if (dia >= 1 and dia <= 30):
                    return True
                else:
                    return False
            case 2:
                if (es_bisiesto(anio) == True): # Febrero tiene 29 dias si es bisiesto
                    if (dia >= 1 and dia <= 29):
                        return True
                    else:
                        return False
                else: # Febrero tiene 28 dias si no es bisiesto
                    if (dia >= 1 and dia <= 28):
                        return True
                    else:
                        return False
    else:
        return False

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")

    # Se solicita una fecha al usuario para validar la funcion.
    print("Ingrese una fecha para validar: ")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))

    print(f"\nFecha a validar: {dia}/{mes}/{anio}")
    
    if validar_fecha(dia, mes, anio) == True:
        print("La fecha es valida :D.")
    else:
        print("La fecha no es valida :(.")

if __name__ == "__main__":
    main()