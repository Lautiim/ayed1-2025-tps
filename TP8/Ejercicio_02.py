ANIO_CORTE = 30  # Punto de corte para años de 2 dígitos


def es_anio_bisiesto(anio: int) -> bool:
    """
    Funcion que verifica si un año es bisiesto.

    Pre:
        anio: año a verificar

    Post:
        True si el año es bisiesto, False en caso contrario
    """
    # Regla clásica: múltiplo de 4 y no de 100, salvo que sea múltiplo de 400
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def es_fecha_valida(fecha: tuple) -> bool:
    """
    Funcion que verifica si una fecha es válida.

    Pre:
        fecha: tupla (día, mes, año) con año en 4 dígitos

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


def normalizar_anio(anio: int, anio_corte: int = ANIO_CORTE) -> int:
    """
    Funcion que convierte un año de 2 dígitos a 4 dígitos según un corte.

    Pre:
        anio: año en 2 o 4 dígitos
        anio_corte: umbral en 0..99; <= corte -> 2000s, > corte -> 1900s

    Post:
        año en 4 dígitos
    """
    # Si ya viene con 4 dígitos, lo dejamos como está
    if anio >= 100:
        return anio

    # Regla del corte pedida: <= corte -> 2000, > corte -> 1900
    if 0 <= anio <= anio_corte:
        return 2000 + anio
    else:
        return 1900 + anio


def fecha_en_extendido(fecha: tuple, anio_corte: int = ANIO_CORTE) -> str:
    """
    Funcion que devuelve la fecha en formato extendido.

    Pre:
        fecha: tupla (día, mes, año) con año en 2 o 4 dígitos
        anio_corte: entero en 0..99 para interpretar años de 2 dígitos

    Post:
        cadena con formato: "D de Mes de AAAA"
    """
    # Nombres de meses capitalizados
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    dia, mes, anio = fecha

    # Normalizo el año según la regla del corte
    anio_norm = normalizar_anio(anio, anio_corte)

    # Valido la fecha resultante (por las dudas)
    if not es_fecha_valida((dia, mes, anio_norm)):
        return "Fecha inválida"

    nombre_mes = meses.get(mes, "Mes inválido")
    if nombre_mes == "Mes inválido":
        return "Fecha inválida"

    return f"{dia} de {nombre_mes} de {anio_norm}"


def main():
    """
    Programa principal para ingresar una fecha, transformarla y mostrarla.

    Pre:
        Ninguna.

    Post:
        Muestra la fecha en formato extendido (o error si no es válida)
    """
    print("FORMATO EXTENDIDO DE FECHAS")
    print(f"Año de corte configurado: {ANIO_CORTE}")

    # Ingreso: dd/mm/aa o dd/mm/aaaa
    texto = input("Ingrese una fecha (dd/mm/aa o dd/mm/aaaa): ").strip()
    try:
        d_str, m_str, a_str = texto.split("/")
        dia = int(d_str)
        mes = int(m_str)
        anio = int(a_str)
    except Exception:
        print("Entrada inválida. Formato esperado: dd/mm/aa o dd/mm/aaaa")
        return

    resultado = fecha_en_extendido((dia, mes, anio), ANIO_CORTE)
    print(resultado)


if __name__ == "__main__":
    main()
