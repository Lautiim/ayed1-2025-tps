def es_fecha_valida(fecha: tuple) -> bool:
    """
    Funcion para verificar si una fecha es válida.

    Pre:
        fecha: tupla (día, mes, año)

    Post:
        True si la fecha es válida, False en caso contrario
    """
    # Valida dia/mes/año considerando meses de 30/31 y febrero bisiesto
    dia, mes, anio = fecha
    meses_con_31_dias = {1, 3, 5, 7, 8, 10, 12}
    meses_con_30_dias = {4, 6, 9, 11}

    # Chequeos básicos de rango
    if anio < 1 or mes < 1 or mes > 12 or dia < 1:
        return False

    if mes in meses_con_31_dias:
        return dia <= 31
    elif mes in meses_con_30_dias:
        return dia <= 30
    elif mes == 2:
        # Febrero: depende si el año es bisiesto
        if es_anio_bisiesto(anio):
            return dia <= 29
        else:
            return dia <= 28
    return False


def es_anio_bisiesto(anio: int) -> bool:
    """
    Funcion para verificar si un año es bisiesto.

    Pre:
        anio: año a verificar

    Post:
        True si el año es bisiesto, False en caso contrario
    """
    # Regla clásica: múltiplo de 4 y no de 100, salvo que sea múltiplo de 400
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def sumar_dias_a_fecha(fecha: tuple, dias_a_sumar: int) -> tuple:
    """
    Funcion para sumar N días a una fecha.
    Pre:
        fecha: tupla (día, mes, año)
        dias_a_sumar: número de días a sumar
    Post:
        nueva fecha como tupla (día, mes, año)
    """
    # Sumo de a un día, ajustando mes y año cuando haga falta
    dia, mes, anio = fecha

    for _ in range(dias_a_sumar):
        dia += 1
        if not es_fecha_valida((dia, mes, anio)):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

    return (dia, mes, anio)


def es_horario_valido(horario: tuple) -> bool:
    """
    Funcion para verificar si un horario es válido.

    Pre:
        horario: tupla (hora, minuto, segundo)

    Post:
        True si el horario es válido, False en caso contrario
    """
    # Chequea rangos válidos en formato 24hs
    hora, minuto, segundo = horario
    return 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60


def diferencia_entre_horarios(horario1: tuple, horario2: tuple) -> tuple:
    """
    Funcion para calcular la diferencia entre dos horarios.

    Pre:
        horario1: tupla (hora, minuto, segundo)
        horario2: tupla (hora, minuto, segundo)

    Post:
        diferencia como tupla (hora, minuto, segundo)
    """
    h1, m1, s1 = horario1
    h2, m2, s2 = horario2

    # Paso todo a segundos para operar fácil
    total_segundos1 = h1 * 3600 + m1 * 60 + s1
    total_segundos2 = h2 * 3600 + m2 * 60 + s2

    # Si el segundo horario es "más temprano", asumimos que pasó al día siguiente
    if total_segundos1 > total_segundos2:
        total_segundos2 += 24 * 3600

    diferencia_segundos = total_segundos2 - total_segundos1

    # Descompongo de nuevo a h:m:s
    horas = diferencia_segundos // 3600
    diferencia_segundos %= 3600
    minutos = diferencia_segundos // 60
    segundos = diferencia_segundos % 60

    return (horas, minutos, segundos)


def main():
    # Pruebitas simples para chequear que todo ande
    # Ingresar fecha por teclado
    input_fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
    dia, mes, anio = map(int, input_fecha.split("/"))
    fecha = (dia, mes, anio)

    print(f"Fecha {fecha} válida: {es_fecha_valida(fecha)}")
    nueva_fecha = sumar_dias_a_fecha(fecha, 3)
    print(f"Suma de 3 días a {fecha}: {nueva_fecha}")

    # Ingresar horario por teclado
    input_horario1 = input("Ingrese el primer horario (hh:mm:ss): ")
    hora, minuto, segundo = map(int, input_horario1.split(":"))
    horario1 = (hora, minuto, segundo)

    # Ingresar segundo horario por teclado
    input_horario2 = input("Ingrese el segundo horario (hh:mm:ss): ")
    hora, minuto, segundo = map(int, input_horario2.split(":"))
    horario2 = (hora, minuto, segundo)

    print(f"Horario {horario1} válido: {es_horario_valido(horario1)}")
    diferencia = diferencia_entre_horarios(horario1, horario2)
    print(f"Diferencia entre {horario1} y {horario2}: {diferencia}")


if __name__ == "__main__":
    main()
