import os

# --- Ubicación del Script ---
script_dir = os.path.dirname(os.path.abspath(__file__))

# --- Rutas de Archivos ---
archivo_entrada = os.path.join(script_dir, 'nombres.txt')
archivo_armenia = os.path.join(script_dir, 'ARMENIA.TXT')
archivo_italia = os.path.join(script_dir, 'ITALIA.TXT')
archivo_espana = os.path.join(script_dir, 'ESPAÑA.TXT')

# Contadores para saber cuántos registros se guardaron
contadores = {
    archivo_armenia: 0,
    archivo_italia: 0,
    archivo_espana: 0,
    "descartados": 0
}

# --- Procesamiento ---
try:
    # Abrimos el archivo de entrada en modo lectura ('r')
    # y los de salida en modo escritura ('w').
    with open(archivo_entrada, 'r', encoding='utf-8') as f_in, \
         open(archivo_armenia, 'w', encoding='utf-8') as f_arm, \
         open(archivo_italia, 'w', encoding='utf-8') as f_ita, \
         open(archivo_espana, 'w', encoding='utf-8') as f_esp:

        print(f"--- Procesando archivo '{archivo_entrada}' ---")

        # Leemos el archivo de entrada línea por línea
        for linea in f_in:
            linea_limpia = linea.strip() # QuitaMOS espacios en blanco y saltos de línea

            # Ignoramos líneas vacías
            if not linea_limpia:
                continue

            # Separamos la línea por la coma para obtener el apellido
            partes = linea_limpia.split(',')
            
            # Verificamos que la línea tenga el formato esperado
            if len(partes) > 0:
                # El apellido es la primera parte antes de la coma
                apellido = partes[0].strip()
                
                # Convertimos a mayúsculas para la comparación
                apellido_upper = apellido.upper()

                # Verificamos las condiciones
                if apellido_upper.endswith("IAN"):
                    f_arm.write(linea_limpia + "\n")
                    contadores[archivo_armenia] += 1
                elif apellido_upper.endswith("INI"):
                    f_ita.write(linea_limpia + "\n")
                    contadores[archivo_italia] += 1
                elif apellido_upper.endswith("EZ"):
                    f_esp.write(linea_limpia + "\n")
                    contadores[archivo_espana] += 1
                else:
                    contadores["descartados"] += 1
            else:
                # Línea mal formada o sin coma
                contadores["descartados"] += 1

    # --- Informe Final ---
    print("\n--- Proceso Finalizado ---")
    print(f"Resultados guardados en:")
    print(f"  {archivo_armenia}: {contadores[archivo_armenia]} registros")
    print(f"  {archivo_italia}: {contadores[archivo_italia]} registros")
    print(f"  {archivo_espana}: {contadores[archivo_espana]} registros")
    print(f"Registros descartados: {contadores['descartados']}")

except FileNotFoundError:
    print(f"\nERROR: El archivo de entrada '{archivo_entrada}' no existe.")
    print("Por favor, cree el archivo en el mismo directorio y vuelva a intentarlo.")
except Exception as e:
    print(f"\nHa ocurrido un error inesperado: {e}")