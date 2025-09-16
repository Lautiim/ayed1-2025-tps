def diadelasemana(dia, mes, año):
    if mes < 3:
        mes = mes + 10
        año = año - 1  # Corregi el guion ya que era un guion largo no una resta
    else:
        mes = mes - 2  # Corregi el guion ya que era un guion largo no una resta
    siglo = año // 100
    año2 = año % 100
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

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

def dias_en_mes(mes: int, año: int) -> int:
    """ Funcion para saber la cantidad de dias que tiene un mes en un año.

    Pre: Recibe dos enteros positivos, que representan: mes y año.

    Post: Devuelve un entero positivo, que representa la cantidad de dias del mes en el año dado.
    """
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: # Meses con 31 dias
            return 31
        case 4 | 6 | 9 | 11: # Meses con 30 dias
            return 30
        case 2: # Febrero, es especial porque depende si es bisiesto o no
            if es_bisiesto(año): # Si es bisiesto, tiene 29 dias
                return 29
            else: # Caso contrario, tiene 28 dias
                return 28

def imprimir_calendario(mes: int, año: int):
    """ Funcion para imprimir el calendario de un mes y año dado.

    Pre: Recibe dos enteros positivos, que representan: mes y año.

    Post: Imprime el calendario del mes y año dados.
    """
    print(f"\n   Calendario {mes}/{año}") # Mostramos el mes y año
    print("-----------------------")
    print("Do Lu Ma Mi Ju Vi Sa") # Mostramos los dias de la semana

    inicio = diadelasemana(1, mes, año) # Obtenemos el dia de la semana del primer dia del mes
    dias = dias_en_mes(mes, año) # Obtenemos la cantidad de dias del mes
    print("   " * inicio, end="") # Imprimimos los espacios hasta el primer dia del mes

    for dia in range(1, dias + 1): # Recorremos los dias del mes
        print(f"{dia:2}", end=" ") # Imprimimos el dia con un espacio
        inicio += 1 # Se incrementa el contador de dias para saber cuando hacer el salto de linea
        if inicio % 7 == 0: # Si el contador es multiplo de 7, hacemos un salto de linea
            print()

    print("\n")

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    

    # Pedimos al usuario que ingrese una fecha
    dia = int(input("Ingrese el dia (1-31): "))
    mes = int(input("Ingrese el mes (1-12): "))
    año = int(input("Ingrese el año: "))

    imprimir_calendario(mes, año) # Llamamos a la funcion para imprimir el calendario del mes y año ingresado
    
    dia_semana = diadelasemana(dia, mes, año) # Llamamos a la funcion para obtener el dia de la semana
    print(f"El {dia}/{mes}/{año} es {dias_semana[dia_semana]}") # Mostramos por pantalla el dia de la semana.

dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"] # Lista para mapear el resultado de diadelasemana a un nombre de día

if __name__ == "__main__":
    main()