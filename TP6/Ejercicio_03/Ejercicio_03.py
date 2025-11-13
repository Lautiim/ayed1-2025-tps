import os

# --- Definición de los nombres de archivo ---
# Usamos constantes para evitar errores de tipeo
ARCHIVO_ALTURAS = "TP6\\Ejercicio_03\\alturas_atletas.txt"
ARCHIVO_PROMEDIOS = "TP6\\Ejercicio_03\\promedios_alturas.txt"


def GrabarRangoAlturas():
    """
    Graba en un archivo las alturas de los atletas de distintas disciplinas.
    Los datos se ingresan desde el teclado.
    Formato:
    <Deporte 1>
    <altura 1>
    <altura 2>
    ...
    """
    print(f"\n--- 1. Grabando Alturas en '{ARCHIVO_ALTURAS}' ---")

    # Usamos 'w' (write) para crear el archivo desde cero.
    # Si el archivo ya existe, lo sobrescribirá.
    try:
        with open(ARCHIVO_ALTURAS, "w", encoding="utf-8") as f:

            while True:
                # Bucle exterior: Pide el deporte
                deporte = input(
                    "\nIngrese el nombre del deporte (o 'fin' para terminar): "
                ).strip()
                if deporte.lower() == "fin":
                    break

                # Escribimos el nombre del deporte en el archivo
                f.write(deporte + "\n")

                print(f"Ingrese alturas para {deporte} (en metros, ej: 1.85).")
                print("Escriba 'fin' cuando termine con este deporte.")

                # Bucle interior: Pide las alturas para ese deporte
                while True:
                    altura_str = input(f"  Altura atleta (o 'fin'): ").strip()

                    if altura_str.lower() == "fin":
                        break  # Termina este deporte y vuelve al bucle exterior

                    # Validación de la altura
                    try:
                        altura = float(altura_str)
                        if altura <= 0:
                            print("Error: La altura debe ser un número positivo.")
                            continue  # Pide de nuevo la altura

                        # Escribimos la altura en el archivo
                        f.write(str(altura) + "\n")

                    except ValueError:
                        print(
                            "Error: Entrada inválida. Debe ingresar un número (ej: 1.85) o 'fin'."
                        )

        print(f"Datos de altura guardados exitosamente en '{ARCHIVO_ALTURAS}'.")
        return True  # Indica que la operación fue exitosa

    except IOError as e:
        print(f"Error al intentar escribir en el archivo '{ARCHIVO_ALTURAS}': {e}")
        return False  # Indica que la operación falló


def GrabarPromedio():
    """
    Lee el archivo de alturas, calcula el promedio por disciplina
    y lo graba en un nuevo archivo de promedios.
    Formato:
    <Deporte 1>
    <Promedio de alturas deporte 1>
    ...
    """
    print(f"\n--- 2. Calculando Promedios en '{ARCHIVO_PROMEDIOS}' ---")

    deporte_actual = None
    alturas_deporte_actual = []

    try:
        # Abrimos ambos archivos: uno para leer (r) y otro para escribir (w)
        with open(ARCHIVO_ALTURAS, "r", encoding="utf-8") as f_in, open(
            ARCHIVO_PROMEDIOS, "w", encoding="utf-8"
        ) as f_out:

            # Función interna para procesar y guardar un deporte
            def procesar_y_guardar_deporte(deporte, alturas):
                if deporte and alturas:  # Solo si hay datos que procesar
                    promedio = sum(alturas) / len(alturas)
                    print(
                        f"  Procesando {deporte}: {len(alturas)} atletas, Promedio: {promedio:.2f}m"
                    )
                    f_out.write(deporte + "\n")
                    f_out.write(str(promedio) + "\n")

            # Leemos el archivo de alturas línea por línea
            for linea in f_in:
                linea_limpia = linea.strip()
                if not linea_limpia:  # Ignoramos líneas vacías
                    continue

                # Intentamos convertir la línea a un número (float)
                try:
                    altura = float(linea_limpia)
                    # Si tiene éxito, es una altura. La añadimos a la lista actual.
                    alturas_deporte_actual.append(altura)

                except ValueError:
                    # Si falla, no es un número, por lo tanto es un NUEVO DEPORTE

                    # 1. Procesamos el deporte ANTERIOR (si había uno)
                    procesar_y_guardar_deporte(deporte_actual, alturas_deporte_actual)

                    # 2. Empezamos el nuevo deporte
                    deporte_actual = (
                        linea_limpia  # Guardamos el nombre del nuevo deporte
                    )
                    alturas_deporte_actual = []  # Reseteamos la lista de alturas

            # --- Fin del bucle ---
            # Debemos procesar el ÚLTIMO deporte que quedó en memoria
            procesar_y_guardar_deporte(deporte_actual, alturas_deporte_actual)

        print(f"Archivo de promedios guardado exitosamente en '{ARCHIVO_PROMEDIOS}'.")
        return True

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de entrada '{ARCHIVO_ALTURAS}'.")
        return False
    except IOError as e:
        print(f"Error de E/S al procesar archivos: {e}")
        return False
    except ZeroDivisionError:
        print(
            f"Error: Se encontró un deporte ('{deporte_actual}') sin alturas registradas."
        )
        return False


def MostrarMasAltos():
    """
    Muestra por pantalla las disciplinas cuyos atletas superan
    la estatura promedio general. Obtiene los datos del archivo de promedios.
    """
    print(f"\n--- 3. Mostrando Disciplinas por encima del Promedio General ---")

    promedios_por_deporte = {}  # Usamos un diccionario: {deporte: promedio}

    try:
        # --- Paso 1: Leer todos los promedios y guardarlos ---
        with open(ARCHIVO_PROMEDIOS, "r", encoding="utf-8") as f:
            while True:
                # Leemos de a 2 líneas: Deporte y Promedio
                deporte = f.readline().strip()
                if not deporte:  # Si la línea está vacía, llegamos al fin
                    break

                promedio_str = f.readline().strip()
                if not promedio_str:  # Seguridad por si el archivo está mal formado
                    print(
                        f"Advertencia: El deporte {deporte} no tiene un promedio asociado."
                    )
                    break

                try:
                    promedios_por_deporte[deporte] = float(promedio_str)
                except ValueError:
                    print(
                        f"Advertencia: Dato inválido para {deporte}: '{promedio_str}'"
                    )

        if not promedios_por_deporte:
            print("No hay datos de promedios para analizar.")
            return

        # --- Paso 2: Calcular el promedio general ---
        todos_los_promedios = list(promedios_por_deporte.values())
        promedio_general = sum(todos_los_promedios) / len(todos_los_promedios)

        print(f"El promedio general de altura es: {promedio_general:.2f}m")
        print("Disciplinas que superan el promedio general:")

        # --- Paso 3: Mostrar las disciplinas que superan el general ---
        encontrados = 0
        for deporte, promedio_atleta in promedios_por_deporte.items():
            if promedio_atleta > promedio_general:
                print(f"  - {deporte} (Promedio: {promedio_atleta:.2f}m)")
                encontrados += 1

        if encontrados == 0:
            print("  (Ninguna disciplina supera el promedio general)")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de promedios '{ARCHIVO_PROMEDIOS}'.")
    except ZeroDivisionError:
        print("Error: No se pueden calcular promedios, el archivo está vacío.")
    except IOError as e:
        print(f"Error al leer el archivo '{ARCHIVO_PROMEDIOS}': {e}")


def main():
    """
    Función principal que orquesta la ejecución del programa.
    """
    # Ejecutamos la primera función. Si falla, no continuamos.
    if GrabarRangoAlturas():
        # Ejecutamos la segunda. Si falla, no continuamos.
        if GrabarPromedio():
            # Ejecutamos la tercera.
            MostrarMasAltos()


# --- Punto de entrada del script ---
if __name__ == "__main__":
    main()
