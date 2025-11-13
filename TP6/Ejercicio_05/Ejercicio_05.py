def leer_formato_1(nombre_archivo: str) -> list:
    """
    Lee un archivo con formato 1 (campos de longitud fija).
    
    Formato esperado:
    - Apellido y Nombre: posiciones 0-19 (20 caracteres)
    - Fecha: posiciones 20-28 (8 caracteres)
    - Domicilio: posiciones 29 en adelante (resto de la línea)
    
    Pre:
        nombre_archivo: nombre del archivo a leer
        
    Post:
        lista de diccionarios con los datos de cada empleado
    """
    empleados = []
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.rstrip('\n\r')
                
                # Extraer campos según posiciones fijas
                if len(linea) >= 29:
                    apellido_nombre = linea[0:20].strip()
                    fecha = linea[20:28].strip()
                    domicilio = linea[29:].strip()
                    
                    empleado = {
                        'apellido_nombre': apellido_nombre,
                        'fecha': fecha,
                        'domicilio': domicilio
                    }
                    empleados.append(empleado)
        
        return empleados
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return []
    except Exception as e:
        print(f"Error al leer archivo formato 1: {e}")
        return []


def leer_formato_2(nombre_archivo: str) -> list:
    """
    Lee un archivo con formato 2 (campos precedidos por longitud de 2 dígitos).
    
    Formato esperado:
    - Cada campo está precedido por un número de 2 dígitos que indica su longitud
    - Ejemplo: 10Pérez Juan082008021114Corrientes 348
    
    Pre:
        nombre_archivo: nombre del archivo a leer
        
    Post:
        lista de diccionarios con los datos de cada empleado
    """
    empleados = []
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.rstrip('\n\r')
                
                empleado = extraer_campos_formato_2(linea)
                if empleado:
                    empleados.append(empleado)
        
        return empleados
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return []
    except Exception as e:
        print(f"Error al leer archivo formato 2: {e}")
        return []


def extraer_campos_formato_2(linea: str) -> dict:
    """
    Extrae los tres campos de una línea en formato 2.
    
    Pre:
        linea: cadena con el formato XXcampo1XXcampo2XXcampo3
        
    Post:
        diccionario con los campos extraídos o None si hay error
    """
    try:
        campos = []
        posicion = 0
        
        # Extraer 3 campos
        for _ in range(3):
            if posicion + 2 > len(linea):
                return None
            
            # Leer los 2 dígitos de longitud
            longitud_str = linea[posicion:posicion + 2]
            if not longitud_str.isdigit():
                return None
            
            longitud = int(longitud_str)
            posicion += 2
            
            # Leer el campo
            if posicion + longitud > len(linea):
                return None
            
            campo = linea[posicion:posicion + longitud]
            campos.append(campo)
            posicion += longitud
        
        return {
            'apellido_nombre': campos[0],
            'fecha': campos[1],
            'domicilio': campos[2]
        }
    
    except Exception as e:
        print(f"Error al extraer campos: {e}")
        return None


def escribir_csv(empleados: list, nombre_archivo: str):
    """
    Escribe los datos de empleados en formato CSV sin usar la librería csv.
    
    Pre:
        empleados: lista de diccionarios con los datos
        nombre_archivo: nombre del archivo CSV a crear
    """
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            # Escribir encabezado
            archivo.write('Apellido y Nombre,Fecha de alta,Domicilio\n')
            
            # Escribir datos
            for empleado in empleados:
                linea_csv = formatear_linea_csv(
                    empleado['apellido_nombre'],
                    empleado['fecha'],
                    empleado['domicilio']
                )
                archivo.write(linea_csv + '\n')
        
        print(f"Archivo CSV creado exitosamente: {nombre_archivo}")
        print(f"Total de registros: {len(empleados)}")
    
    except Exception as e:
        print(f"Error al escribir archivo CSV: {e}")


def formatear_linea_csv(campo1: str, campo2: str, campo3: str) -> str:
    """
    Formatea una línea CSV manejando correctamente las comas y comillas.
    
    Pre:
        campo1, campo2, campo3: valores de los campos
        
    Post:
        línea formateada en formato CSV
    """
    campos = [campo1, campo2, campo3]
    campos_formateados = []
    
    for campo in campos:
        campo_formateado = escapar_campo_csv(campo)
        campos_formateados.append(campo_formateado)
    
    return ','.join(campos_formateados)


def escapar_campo_csv(campo: str) -> str:
    """
    Escapa un campo para formato CSV.
    Si contiene comas, comillas o saltos de línea, se encierra entre comillas
    y se duplican las comillas internas.
    
    Pre:
        campo: valor del campo a escapar
        
    Post:
        campo escapado según reglas CSV
    """
    # Verificar si necesita ser encerrado en comillas
    necesita_comillas = False
    
    if ',' in campo or '"' in campo or '\n' in campo or '\r' in campo:
        necesita_comillas = True
    
    if necesita_comillas:
        # Duplicar las comillas internas
        campo = campo.replace('"', '""')
        # Encerrar entre comillas
        campo = f'"{campo}"'
    
    return campo


def convertir_archivo(archivo_entrada: str, tipo_formato: int):
    """
    Convierte un archivo de formato 1 o 2 a CSV.
    
    Pre:
        archivo_entrada: nombre del archivo a convertir
        tipo_formato: 1 o 2 según el formato del archivo
    """
    print("\n" + "=" * 60)
    print(f"Convirtiendo archivo: {archivo_entrada}")
    print(f"Formato detectado: {tipo_formato}")
    print("=" * 60)
    
    # Leer datos según el formato
    if tipo_formato == 1:
        empleados = leer_formato_1(archivo_entrada)
    elif tipo_formato == 2:
        empleados = leer_formato_2(archivo_entrada)
    else:
        print("Error: Tipo de formato inválido")
        return
    
    if not empleados:
        print("No se pudieron leer datos del archivo.")
        return
    
    # Mostrar algunos datos leídos
    print(f"\nPrimeros registros leídos:")
    for i, emp in enumerate(empleados[:3]):
        print(f"  {i+1}. {emp['apellido_nombre']} - {emp['fecha']} - {emp['domicilio']}")
    
    if len(empleados) > 3:
        print(f"  ... y {len(empleados) - 3} registros más")
    
    # Generar nombre de archivo de salida
    if archivo_entrada.endswith('.txt'):
        archivo_salida = archivo_entrada[:-4] + '.csv'
    else:
        archivo_salida = archivo_entrada + '.csv'
    
    # Escribir CSV
    print(f"\nGenerando archivo CSV: {archivo_salida}")
    escribir_csv(empleados, archivo_salida)


def menu_principal():
    """Menú principal del programa."""
    print("\n" + "=" * 60)
    print("CONVERSOR DE FORMATOS DE EMPLEADOS A CSV")
    print("=" * 60)
    print("\nFormatos disponibles:")
    print("  1. Formato con campos de longitud fija")
    print("  2. Formato con longitud precedida por 2 dígitos")
    print("  0. Salir")
    
    while True:
        print("\n" + "-" * 60)
        opcion = input("\nSeleccione el formato del archivo a convertir (0-2): ").strip()
        
        if opcion == '0':
            print("\n¡Hasta luego!")
            break
        
        if opcion not in ['1', '2']:
            print("Opción inválida. Por favor, ingrese 1, 2 o 0.")
            continue
        
        tipo_formato = int(opcion)
        archivo = input("Ingrese la ruta del archivo a convertir: ").strip()
        
        if archivo:
            convertir_archivo(archivo, tipo_formato)
        else:
            print("Debe ingresar un nombre de archivo.")


def main():
    """Función principal del programa."""
    menu_principal()


if __name__ == "__main__":
    main()