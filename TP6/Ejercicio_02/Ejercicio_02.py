import os


def dividir_archivo_por_lineas(archivo_entrada: str, max_lineas: int) -> bool:
    """
    Funcion para dividir un archivo de texto en partes, según un número máximo de líneas.

    Pre: Recibe la ruta al archivo de entrada (str) y el número máximo (int)
    de líneas por cada parte.

    Post: Genera archivos de salida con el sufijo _parte_N.
    Devuelve True si tuvo éxito, False si falló (ej. archivo no existe).
    """

    # Validamos que el archivo de entrada exista
    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo '{archivo_entrada}' no se pudo encontrar.")
        return False

    # Validar que el número de líneas sea positivo
    if max_lineas <= 0:
        print("Error: El número máximo de líneas debe ser mayor a cero.")
        return False

    # Preparar nombres de archivo base
    base_nombre, extension = os.path.splitext(archivo_entrada)

    try:
        # Abrir el archivo de entrada para leerlo línea por línea
        with open(archivo_entrada, "r", encoding="utf-8") as f_in:

            part_number = 1  # Contador para el número de parte
            f_out = None  # Variable para el archivo de salida
            line_count = 0  # Contador de líneas para la parte actual

            # Bucle principal: leer línea por línea
            for linea in f_in:

                # Decidir si necesitamos un nuevo archivo de salida
                # Se necesita un archivo nuevo si:
                # Es la primera línea que leemos (f_out es None)
                # O si el archivo actual ya está lleno (line_count >= max_lineas)
                if f_out is None or line_count >= max_lineas:

                    if f_out:  # Si había un archivo abierto, lo cerramos
                        f_out.close()
                        part_number += 1  # Pasamos al siguiente número de parte

                    # Crear el nombre del nuevo archivo
                    nombre_salida = f"{base_nombre}_parte_{part_number}{extension}"
                    print(f"Creando archivo: {nombre_salida}")

                    # Abrir el nuevo archivo de salida
                    f_out = open(nombre_salida, "w", encoding="utf-8")
                    line_count = 0  # Reiniciar el contador de líneas

                # Escribimos la línea y actualizamos el contador
                f_out.write(linea)
                line_count += 1

            # Fin del bucle, cerrar el último archivo
            if f_out:
                f_out.close()

            print("\n¡División de archivo completada exitosamente!")
            return True

    except IOError as e:
        print(f"Error de E/S (lectura/escritura): {e}")
        return False
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return False


def main():
    print("--- Divisor de Archivos de Texto (por Líneas) ---")

    # --- Pedir Archivo de Entrada ---
    archivo = input("Ingrese el nombre (o ruta) del archivo a dividir: ").strip()

    # --- Pedir Número de Líneas ---
    max_lineas_input = 0
    while True:
        try:
            max_lineas_input = int(
                input("Ingrese el número máximo de líneas por parte (ej. 100): ")
            )
            if max_lineas_input <= 0:
                print("Por favor, ingrese un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # --- Ejecutar la función ---
    if max_lineas_input > 0:
        dividir_archivo_por_lineas(archivo, max_lineas_input)


if __name__ == "__main__":
    main()
