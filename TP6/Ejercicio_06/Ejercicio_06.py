from datetime import datetime
import os


# Constantes del hotel
PISOS = 10
HABITACIONES_POR_PISO = 6

# Estructura de datos del hotel
habitaciones = [[None for _ in range(HABITACIONES_POR_PISO)] for _ in range(PISOS)]
huespedes_registrados = []


def limpiar_pantalla():
    """
    Función que limpia la pantalla de la consola.

    Pre: Ninguna.

    Post: La pantalla de la consola queda limpia.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """
    Función que pausa la ejecución hasta que el usuario presione Enter.

    Pre: Ninguna.

    Post: El programa espera a que el usuario presione Enter.
    """
    input("\nPresione Enter para continuar...")
    limpiar_pantalla()


def registrar_ingreso(
    dni: int, apellido_nombre: str, fecha_ingreso: str, cantidad_ocupantes: int
) -> tuple | None:
    """
    Función que registra el ingreso de un huésped y le asigna una habitación disponible.

    Pre: dni > 0, apellido_nombre no vacío, fecha_ingreso formato DDMMAAAA, cantidad_ocupantes > 0.

    Post: Se registra el huésped y se asigna una habitación disponible.
          Retorna el número de habitación asignada (piso, habitacion) o None si no hay.
    """
    # Buscar habitación disponible
    for piso in range(PISOS):
        for hab in range(HABITACIONES_POR_PISO):
            if habitaciones[piso][hab] is None:
                # Asignar habitación
                huesped = {
                    "dni": dni,
                    "apellido_nombre": apellido_nombre,
                    "fecha_ingreso": fecha_ingreso,
                    "cantidad_ocupantes": cantidad_ocupantes,
                    "piso": piso + 1,
                    "habitacion": hab + 1,
                }
                habitaciones[piso][hab] = huesped
                huespedes_registrados.append(huesped)
                return (piso + 1, hab + 1)

    return None


def cargar_desde_archivo(nombre_archivo: str) -> bool:
    """
    Función que carga huéspedes desde un archivo CSV y los registra en el hotel.

    Pre: nombre_archivo es una ruta válida a un archivo CSV.

    Post: Se cargan todos los huéspedes del archivo y se asignan habitaciones.
          Los DNI no deben repetirse. Retorna True si hubo registros exitosos.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            # Saltar encabezado si existe
            inicio = 1 if lineas and "DNI" in lineas[0] else 0

            registros_ok = 0
            registros_error = 0

            for i in range(inicio, len(lineas)):
                linea = lineas[i].strip()
                if not linea:
                    continue

                resultado = procesar_linea_csv(linea)
                if resultado:
                    registros_ok += 1
                else:
                    registros_error += 1

            print(f"\nRegistros procesados correctamente: {registros_ok}")
            if registros_error > 0:
                print(f"Registros con errores: {registros_error}")

            return registros_ok > 0

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return False
    except Exception as e:
        print(f"Error al cargar archivo: {e}")
        return False


def procesar_linea_csv(linea: str) -> bool:
    """
    Función que procesa una línea CSV y registra el huésped si los datos son válidos.

    Pre: linea es una cadena con formato CSV.

    Post: Procesa la línea y registra el huésped si los datos son válidos.
          Retorna True si fue exitoso, False en caso contrario.
    """
    try:
        campos = parsear_csv(linea)

        if len(campos) < 4:
            return False

        dni = int(campos[0])
        apellido_nombre = campos[1]
        fecha_ingreso = campos[2]
        cantidad_ocupantes = int(campos[3])

        # Validar que el DNI no esté repetido
        if dni_existe(dni):
            print(f"Advertencia: DNI {dni} ya registrado. Se omite.")
            return False

        # Validar fecha
        if not validar_fecha(fecha_ingreso):
            print(f"Advertencia: Fecha inválida {fecha_ingreso}. Se omite.")
            return False

        # Registrar
        resultado = registrar_ingreso(
            dni, apellido_nombre, fecha_ingreso, cantidad_ocupantes
        )

        if resultado is None:
            print(f"Advertencia: No hay habitaciones disponibles para DNI {dni}")
            return False

        return True

    except (ValueError, IndexError) as e:
        return False


def parsear_csv(linea: str) -> list:
    """
    Función que parsea una línea CSV y extrae los campos.

    Pre: linea es una cadena.

    Post: Retorna una lista con los campos del CSV.
    """
    campos = []
    campo_actual = []
    en_comillas = False

    for char in linea:
        if char == '"':
            en_comillas = not en_comillas
        elif char == "," and not en_comillas:
            campos.append("".join(campo_actual).strip())
            campo_actual = []
        else:
            campo_actual.append(char)

    # Agregar último campo
    if campo_actual:
        campos.append("".join(campo_actual).strip())

    return campos


def dni_existe(dni: int) -> bool:
    """
    Función que verifica si un DNI ya está registrado en el hotel.

    Pre: dni es un número entero.

    Post: Retorna True si el DNI ya está registrado, False en caso contrario.
    """
    for huesped in huespedes_registrados:
        if huesped["dni"] == dni:
            return True
    return False


def validar_fecha(fecha_str: str) -> bool:
    """
    Función que valida si una fecha tiene formato DDMMAAAA correcto.

    Pre: fecha_str es una cadena.

    Post: Retorna True si la fecha tiene formato DDMMAAAA válido, False en caso contrario.
    """
    if len(fecha_str) != 8:
        return False

    try:
        dia = int(fecha_str[0:2])
        mes = int(fecha_str[2:4])
        anio = int(fecha_str[4:8])

        fecha = datetime(anio, mes, dia)
        return True
    except:
        return False


def piso_mas_ocupado():
    """
    Función que determina el piso con mayor cantidad de habitaciones ocupadas.

    Pre: El hotel ha sido inicializado.

    Post: Retorna el número de piso (1-10) con mayor cantidad de habitaciones ocupadas
          y la cantidad de habitaciones ocupadas.
    """
    max_ocupadas = 0
    piso_max = 1

    for piso in range(PISOS):
        ocupadas = sum(1 for hab in habitaciones[piso] if hab is not None)
        if ocupadas > max_ocupadas:
            max_ocupadas = ocupadas
            piso_max = piso + 1

    return piso_max, max_ocupadas


def habitaciones_vacias():
    """
    Función que cuenta la cantidad de habitaciones vacías en el hotel.

    Pre: El hotel ha sido inicializado.

    Post: Retorna la cantidad total de habitaciones vacías en el hotel.
    """
    vacias = 0
    for piso in range(PISOS):
        for hab in range(HABITACIONES_POR_PISO):
            if habitaciones[piso][hab] is None:
                vacias += 1
    return vacias


def proxima_desocupacion():
    """
    Función que determina cuál será la próxima habitación en desocuparse.

    Pre: Existe al menos un huésped registrado.

    Post: Retorna los datos de la habitación que se desocupará primero
          (la que tiene fecha de ingreso más antigua).
    """
    if not huespedes_registrados:
        return None

    huesped_mas_antiguo = None
    fecha_mas_antigua = None

    for huesped in huespedes_registrados:
        fecha = convertir_fecha(huesped["fecha_ingreso"])
        if fecha_mas_antigua is None or fecha < fecha_mas_antigua:
            fecha_mas_antigua = fecha
            huesped_mas_antiguo = huesped

    return huesped_mas_antiguo


def convertir_fecha(fecha_str: str) -> datetime:
    """
    Función que convierte una cadena de fecha a objeto datetime.

    Pre: fecha_str tiene formato DDMMAAAA.

    Post: Retorna un objeto datetime con la fecha.
    """
    dia = int(fecha_str[0:2])
    mes = int(fecha_str[2:4])
    anio = int(fecha_str[4:8])
    return datetime(anio, mes, dia)


def calcular_dias_alojamiento(fecha_ingreso_str: str) -> int:
    """
    Función que calcula los días de alojamiento desde una fecha hasta hoy.

    Pre: fecha_ingreso_str tiene formato DDMMAAAA.

    Post: Retorna la cantidad de días de alojamiento.
    """
    fecha_ingreso = convertir_fecha(fecha_ingreso_str)
    fecha_actual = datetime.now()
    dias = (fecha_actual - fecha_ingreso).days
    return dias


def listado_por_dias_alojamiento():
    """
    Función que genera un listado de huéspedes ordenado por días de alojamiento.

    Pre: El hotel tiene huéspedes registrados.

    Post: Retorna una lista de huéspedes ordenada por cantidad de días de alojamiento
          (descendente).
    """
    # Calcular días de alojamiento para cada huésped
    huespedes_con_dias = []
    for huesped in huespedes_registrados:
        dias = calcular_dias_alojamiento(huesped["fecha_ingreso"])

        huesped_info = huesped.copy()
        huesped_info["dias_alojamiento"] = dias
        huespedes_con_dias.append(huesped_info)

    # Ordenar por días (descendente)
    huespedes_con_dias.sort(key=lambda x: x["dias_alojamiento"], reverse=True)

    return huespedes_con_dias


def mostrar_estado_hotel():
    """
    Función que muestra el estado actual de todas las habitaciones del hotel.

    Pre: El hotel ha sido inicializado.

    Post: Muestra en pantalla el estado de todas las habitaciones.
    """
    print("\n" + "=" * 80)
    print("ESTADO ACTUAL DEL HOTEL")
    print("=" * 80)

    for piso in range(PISOS):
        print(f"\nPiso {piso + 1}:")
        for hab in range(HABITACIONES_POR_PISO):
            habitacion = habitaciones[piso][hab]
            if habitacion is None:
                estado = "VACÍA"
            else:
                estado = f"Ocupada - {habitacion['apellido_nombre']} (DNI: {habitacion['dni']})"
            print(f"  Habitación {hab + 1}: {estado}")

    pausar()


def escribir_csv(nombre_archivo: str, huespedes: list[dict]):
    """
    Función que escribe los datos de huéspedes en un archivo CSV.

    Pre: nombre_archivo es una ruta válida, huespedes es una lista de diccionarios.

    Post: Se crea un archivo CSV con los datos de los huéspedes.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            # Escribir encabezado
            archivo.write("DNI,Apellido y Nombre,Fecha Ingreso,Cantidad Ocupantes\n")

            # Escribir datos
            for huesped in huespedes:
                linea = formatear_linea_csv(
                    str(huesped["dni"]),
                    huesped["apellido_nombre"],
                    huesped["fecha_ingreso"],
                    str(huesped["cantidad_ocupantes"]),
                )
                archivo.write(linea + "\n")

        print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Error al escribir archivo: {e}")


def formatear_linea_csv(campo1, campo2, campo3, campo4):
    """
    Función que formatea una línea CSV correctamente con 4 campos.

    Pre: Se reciben cuatro campos como cadenas.

    Post: Retorna una línea CSV formateada correctamente.
    """
    campos = [campo1, campo2, campo3, campo4]
    campos_formateados = []

    for campo in campos:
        if "," in campo or '"' in campo or "\n" in campo:
            campo = campo.replace('"', '""')
            campo = f'"{campo}"'
        campos_formateados.append(campo)

    return ",".join(campos_formateados)


def menu_principal():
    """
    Función que muestra el menú principal y gestiona las opciones del usuario.

    Pre: Ninguna.

    Post: Muestra el menú principal y gestiona las opciones del usuario.
    """
    limpiar_pantalla()
    print("\n" + "=" * 80)
    print("SISTEMA DE GESTIÓN DE HOTEL")
    print("=" * 80)
    print(f"Hotel: {PISOS} pisos, {HABITACIONES_POR_PISO} habitaciones por piso")
    print(f"Total de habitaciones: {PISOS * HABITACIONES_POR_PISO}")

    while True:
        print("\n" + "-" * 80)
        print("MENÚ PRINCIPAL")
        print("-" * 80)
        print("1. Registrar ingreso de huésped")
        print("2. Cargar huéspedes desde archivo CSV")
        print("3. Mostrar piso con mayor ocupación")
        print("4. Mostrar cantidad de habitaciones vacías")
        print("5. Mostrar próxima habitación a desocupar")
        print("6. Mostrar listado ordenado por días de alojamiento")
        print("7. Mostrar estado completo del hotel")
        print("8. Generar archivo CSV de ejemplo")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()
        limpiar_pantalla()

        if opcion == "1":
            registrar_huesped_manual()
        elif opcion == "2":
            cargar_archivo_menu()
        elif opcion == "3":
            mostrar_piso_mas_ocupado_menu()
        elif opcion == "4":
            mostrar_habitaciones_vacias_menu()
        elif opcion == "5":
            mostrar_proxima_desocupacion_menu()
        elif opcion == "6":
            mostrar_listado_dias()
        elif opcion == "7":
            mostrar_estado_hotel()
        elif opcion == "8":
            generar_archivo_ejemplo()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
            pausar()


def registrar_huesped_manual():
    """
    Función que registra un huésped con datos ingresados por el usuario.

    Pre: Ninguna.

    Post: Registra un huésped con datos ingresados por el usuario.
    """
    print("\n" + "=" * 80)
    print("REGISTRO DE HUÉSPED")
    print("=" * 80)

    try:
        dni = int(input("\nDNI del cliente: "))
        apellido_nombre = input("Apellido y Nombre: ").strip()
        fecha_ingreso = input("Fecha de ingreso (DDMMAAAA): ").strip()
        cantidad_ocupantes = int(input("Cantidad de ocupantes: "))

        if dni_existe(dni):
            print(f"\nError: El DNI {dni} ya está registrado en el hotel.")
            pausar()
            return

        if not validar_fecha(fecha_ingreso):
            print("\nError: Fecha inválida. Use formato DDMMAAAA.")
            pausar()
            return

        resultado = registrar_ingreso(
            dni, apellido_nombre, fecha_ingreso, cantidad_ocupantes
        )

        if resultado:
            piso, hab = resultado
            print(f"\n✓ Huésped registrado exitosamente")
            print(f"  Habitación asignada: Piso {piso}, Habitación {hab}")
        else:
            print("\n✗ No hay habitaciones disponibles.")

        pausar()

    except ValueError:
        print("\nError: Debe ingresar valores numéricos válidos para DNI y ocupantes.")
        pausar()


def cargar_archivo_menu():
    """
    Función que solicita el nombre de archivo y carga los huéspedes desde un CSV.

    Pre: Ninguna.

    Post: Carga huéspedes desde un archivo CSV.
    """
    print("\n" + "=" * 80)
    print("CARGAR HUÉSPEDES DESDE ARCHIVO")
    print("=" * 80)

    nombre_archivo = input("\nIngrese el nombre del archivo CSV: ").strip()

    print(f"\nCargando archivo '{nombre_archivo}'...")
    exito = cargar_desde_archivo(nombre_archivo)

    if exito:
        print(f"\n✓ Archivo cargado exitosamente")
        print(f"  Total de huéspedes: {len(huespedes_registrados)}")
        print(
            f"  Habitaciones ocupadas: {PISOS * HABITACIONES_POR_PISO - habitaciones_vacias()}"
        )

    pausar()


def mostrar_piso_mas_ocupado_menu():
    """
    Función que muestra el piso con mayor cantidad de habitaciones ocupadas.

    Pre: Ninguna.

    Post: Muestra el piso con mayor cantidad de habitaciones ocupadas.
    """
    piso, cantidad = piso_mas_ocupado()
    print(f"\n{'=' * 80}")
    print(f"PISO CON MAYOR OCUPACIÓN")
    print(f"{'=' * 80}")
    print(f"\nPiso: {piso}")
    print(f"Habitaciones ocupadas: {cantidad} de {HABITACIONES_POR_PISO}")
    pausar()


def mostrar_habitaciones_vacias_menu():
    """
    Función que muestra la cantidad de habitaciones vacías en el hotel.

    Pre: Ninguna.

    Post: Muestra la cantidad de habitaciones vacías en el hotel.
    """
    vacias = habitaciones_vacias()
    total = PISOS * HABITACIONES_POR_PISO
    print(f"\n{'=' * 80}")
    print(f"HABITACIONES VACÍAS")
    print(f"{'=' * 80}")
    print(f"\nHabitaciones vacías: {vacias}")
    print(f"Habitaciones ocupadas: {total - vacias}")
    print(f"Total de habitaciones: {total}")
    print(f"Ocupación: {((total - vacias) / total * 100):.1f}%")
    pausar()


def mostrar_proxima_desocupacion_menu():
    """
    Función que muestra la habitación que se desocupará primero.

    Pre: Ninguna.

    Post: Muestra la habitación que se desocupará primero.
    """
    huesped = proxima_desocupacion()

    print(f"\n{'=' * 80}")
    print(f"PRÓXIMA HABITACIÓN A DESOCUPAR")
    print(f"{'=' * 80}")

    if huesped is None:
        print("\nNo hay huéspedes registrados.")
    else:
        print(f"\nPiso: {huesped['piso']}")
        print(f"Habitación: {huesped['habitacion']}")
        print(f"Huésped: {huesped['apellido_nombre']}")
        print(f"DNI: {huesped['dni']}")
        print(f"Fecha de ingreso: {huesped['fecha_ingreso']}")
        print(f"Ocupantes: {huesped['cantidad_ocupantes']}")

    pausar()


def mostrar_listado_dias():
    """
    Función que muestra el listado de huéspedes ordenado por días de alojamiento.

    Pre: Ninguna.

    Post: Muestra el listado de huéspedes ordenado por días de alojamiento.
    """
    huespedes = listado_por_dias_alojamiento()

    print(f"\n{'=' * 80}")
    print(f"LISTADO DE HUÉSPEDES POR DÍAS DE ALOJAMIENTO")
    print(f"{'=' * 80}")

    if not huespedes:
        print("\nNo hay huéspedes registrados.")
    else:
        print(
            f"\n{'#':<4} {'Apellido y Nombre':<30} {'DNI':<12} {'Días':<6} {'Piso':<6} {'Hab':<6}"
        )
        print("-" * 80)

        for i, huesped in enumerate(huespedes, 1):
            print(
                f"{i:<4} {huesped['apellido_nombre']:<30} {huesped['dni']:<12} "
                f"{huesped['dias_alojamiento']:<6} {huesped['piso']:<6} {huesped['habitacion']:<6}"
            )

    pausar()


def generar_archivo_ejemplo():
    """
    Función que genera un archivo CSV de ejemplo con datos de huéspedes.

    Pre: Ninguna.

    Post: Genera un archivo CSV de ejemplo con datos de huéspedes.
    """
    print("\n" + "=" * 80)
    print("GENERAR ARCHIVO DE EJEMPLO")
    print("=" * 80)

    huespedes_ejemplo = [
        {
            "dni": 12345678,
            "apellido_nombre": "García Juan",
            "fecha_ingreso": "01112025",
            "cantidad_ocupantes": 2,
        },
        {
            "dni": 23456789,
            "apellido_nombre": "Rodríguez María",
            "fecha_ingreso": "05112025",
            "cantidad_ocupantes": 1,
        },
        {
            "dni": 34567890,
            "apellido_nombre": "Fernández Carlos",
            "fecha_ingreso": "08112025",
            "cantidad_ocupantes": 4,
        },
        {
            "dni": 45678901,
            "apellido_nombre": "López Ana",
            "fecha_ingreso": "10112025",
            "cantidad_ocupantes": 3,
        },
        {
            "dni": 56789012,
            "apellido_nombre": "Martínez Pedro",
            "fecha_ingreso": "11112025",
            "cantidad_ocupantes": 2,
        },
    ]

    nombre_archivo = "TP6\\Ejercicio_06\\huespedes_ejemplo.csv"
    escribir_csv(nombre_archivo, huespedes_ejemplo)
    print(f"\nArchivo generado con {len(huespedes_ejemplo)} registros de ejemplo.")
    pausar()


def main():
    """
    Función que ejecuta el programa principal.

    Pre: Ninguna.

    Post: Ejecuta el programa principal.
    """
    menu_principal()


if __name__ == "__main__":
    main()
