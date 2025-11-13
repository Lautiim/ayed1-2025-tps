"""
Desarrollar un programa para eliminar todos los comentarios de un programa  es-
crito  en  lenguaje  Python.  Tener  en  cuenta  que  los  comentarios  comienzan  con  el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do-
bles)  y  que  también  se  considera  comentario  a  las  cadenas  de  documentación
(docstrings)
"""


def eliminar_comentarios(archivo_entrada, archivo_salida):
    """
    Elimina todos los comentarios de un archivo Python.

    Args:
        archivo_entrada: nombre del archivo Python a procesar
        archivo_salida: nombre del archivo de salida sin comentarios
    """
    try:
        with open(archivo_entrada, "r", encoding="utf-8") as entrada:
            lineas = entrada.readlines()

        lineas_sin_comentarios = []
        en_docstring = False
        delimitador_docstring = None

        for linea in lineas:
            linea_procesada = procesar_linea(linea, en_docstring, delimitador_docstring)

            # Detectar inicio/fin de docstrings
            if '"""' in linea or "'''" in linea:
                resultado = manejar_docstring(
                    linea, en_docstring, delimitador_docstring
                )
                en_docstring = resultado["en_docstring"]
                delimitador_docstring = resultado["delimitador"]

                # Si la línea tiene solo el docstring, la omitimos
                if en_docstring or (not en_docstring and es_solo_docstring(linea)):
                    continue

            # Si estamos dentro de un docstring, omitir la línea
            if en_docstring:
                continue

            # Procesar línea para eliminar comentarios #
            linea_sin_comentario = eliminar_comentario_linea(linea)

            # Solo agregar si la línea no está vacía o tiene contenido
            if linea_sin_comentario.strip():
                lineas_sin_comentarios.append(linea_sin_comentario)
            elif not linea.strip():  # Preservar líneas en blanco originales
                lineas_sin_comentarios.append("\n")

        # Guardar resultado
        with open(archivo_salida, "w", encoding="utf-8") as salida:
            salida.writelines(lineas_sin_comentarios)

        print(f"Archivo procesado exitosamente.")
        print(f"Archivo de entrada: {archivo_entrada}")
        print(f"Archivo de salida: {archivo_salida}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


def procesar_linea(linea, en_docstring, delimitador):
    """Procesa una línea individual del archivo."""
    return linea


def manejar_docstring(linea, en_docstring, delimitador_actual):
    """
    Detecta y maneja el estado de los docstrings.

    Returns:
        dict con 'en_docstring' y 'delimitador'
    """
    # Buscar triple comilla simple o doble
    if '"""' in linea:
        delimitador = '"""'
    elif "'''" in linea:
        delimitador = "'''"
    else:
        return {"en_docstring": en_docstring, "delimitador": delimitador_actual}

    # Verificar si el delimitador está dentro de una cadena
    if esta_en_cadena(linea, delimitador):
        return {"en_docstring": en_docstring, "delimitador": delimitador_actual}

    # Contar ocurrencias del delimitador
    cuenta = contar_delimitadores(linea, delimitador)

    if not en_docstring:
        # Comenzando un docstring
        if cuenta == 1:
            return {"en_docstring": True, "delimitador": delimitador}
        elif cuenta == 2:
            # Docstring en una sola línea
            return {"en_docstring": False, "delimitador": None}
    else:
        # Terminando un docstring
        if delimitador_actual == delimitador and cuenta >= 1:
            return {"en_docstring": False, "delimitador": None}

    return {"en_docstring": en_docstring, "delimitador": delimitador_actual}


def es_solo_docstring(linea):
    """Verifica si una línea contiene solo un docstring."""
    linea_strip = linea.strip()
    return linea_strip.startswith('"""') or linea_strip.startswith("'''")


def contar_delimitadores(linea, delimitador):
    """Cuenta cuántas veces aparece el delimitador en la línea."""
    contador = 0
    pos = 0
    while pos < len(linea):
        pos = linea.find(delimitador, pos)
        if pos == -1:
            break
        if not esta_en_cadena_hasta_pos(linea, pos):
            contador += 1
        pos += len(delimitador)
    return contador


def esta_en_cadena(linea, subcadena):
    """Verifica si una subcadena está dentro de comillas."""
    pos = linea.find(subcadena)
    if pos == -1:
        return False
    return esta_en_cadena_hasta_pos(linea, pos)


def esta_en_cadena_hasta_pos(linea, pos):
    """Verifica si una posición está dentro de una cadena delimitada por comillas."""
    en_comilla_simple = False
    en_comilla_doble = False

    for i in range(pos):
        char = linea[i]

        # Ignorar caracteres escapados
        if i > 0 and linea[i - 1] == "\\":
            continue

        if char == '"' and not en_comilla_simple:
            en_comilla_doble = not en_comilla_doble
        elif char == "'" and not en_comilla_doble:
            en_comilla_simple = not en_comilla_simple

    return en_comilla_simple or en_comilla_doble


def eliminar_comentario_linea(linea):
    """
    Elimina el comentario # de una línea, respetando comillas.
    """
    resultado = []
    en_comilla_simple = False
    en_comilla_doble = False
    i = 0

    while i < len(linea):
        char = linea[i]

        # Verificar escape
        if i > 0 and linea[i - 1] == "\\":
            resultado.append(char)
            i += 1
            continue

        # Manejar comillas
        if char == '"' and not en_comilla_simple:
            en_comilla_doble = not en_comilla_doble
            resultado.append(char)
        elif char == "'" and not en_comilla_doble:
            en_comilla_simple = not en_comilla_simple
            resultado.append(char)
        elif char == "#" and not en_comilla_simple and not en_comilla_doble:
            # Encontramos un comentario, detener aquí
            # Mantener el salto de línea si existe
            if linea.rstrip().endswith("\n") or linea.endswith("\n"):
                resultado.append("\n")
            break
        else:
            resultado.append(char)

        i += 1

    return "".join(resultado)


def main():
    """Función principal del programa."""
    print("=" * 60)
    print("ELIMINADOR DE COMENTARIOS DE ARCHIVOS PYTHON")
    print("=" * 60)

    archivo_entrada = input("\nIngrese la ruta del archivo Python a procesar: ").strip()

    # Generar nombre de archivo de salida
    if archivo_entrada.endswith(".py"):
        archivo_salida = archivo_entrada[:-3] + "_sin_comentarios.py"
    else:
        archivo_salida = archivo_entrada + "_sin_comentarios"

    respuesta = (
        input(f"¿Desea guardar como '{archivo_salida}'? (S/N): ").strip().upper()
    )

    if respuesta == "N":
        archivo_salida = input("Ingrese el nombre del archivo de salida: ").strip()

    print("\nProcesando archivo...")
    eliminar_comentarios(archivo_entrada, archivo_salida)
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
