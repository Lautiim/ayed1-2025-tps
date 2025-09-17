def registrar_pacientes() -> tuple[list[int], list[int]]:
    """Funcion para registrar a los pacientes que ingresan a la clinica.
    
    Pre: No tiene prerequisitos.

    Post: Devuelve dos listas:
        - lista_urgencias: con los números de afiliados atendidos por urgencia.
        - lista_turnos: con los números de afiliados atendidos por turno.
    """
    pacientes_urgencia = [] # Lista para pacientes por urgencia
    pacientes_turno = []    # Lista para pacientes por turno


    # Bucle para registrar pacientes
    while True:
        # Solcitamos el numero de afiliado
        nro_afiliado = int(input("Ingrese el numero de afiliado (4 dígitos) o -1 para finalizar: "))
        if nro_afiliado == -1: # Si ingresa -1, finalizamos el registro
            break
            
        # Validación del número de afiliado
        if nro_afiliado < 1000 or nro_afiliado > 9999: # Debe tener 4 dígitos, si no, mostramos un mensaje de error
            print("Error: El numero de afiliado debe tener 4 dígitos.")
        else: # Si es valido, solicitamos el tipo de visita
            while True:
                tipo_visita = int(input("Tipo de visita (0: Urgencia, 1: Turno): "))
                if tipo_visita == 0:
                    pacientes_urgencia.append(nro_afiliado)
                    break
                elif tipo_visita == 1:
                    pacientes_turno.append(nro_afiliado)
                    break
                else:
                    print("Error: Tipo de visita inválido. Debe ingresar 0 o 1.")
            
    return pacientes_urgencia, pacientes_turno

def mostrar_listados(pacientes_urgencia: list[int], pacientes_turno: list[int]) -> None:
    """Funcion para listar los pacientes por urgencia y por turno.
    
    Pre: Se ingresan dos listas:
        - pacientes_urgencia (list): Lista de pacientes por urgencia.
        - pacientes_turno (list): Lista de pacientes por turno.

    Post: Muestra por pantalla los pacientes atendidos por urgencia y por turno (en orden de llegada).
        
    """
    # Validamos que las listas sean listas
    assert isinstance(pacientes_urgencia, list), "Error: pacientes_urgencia debe ser una lista."
    assert isinstance(pacientes_turno, list), "Error: pacientes_turno debe ser una lista."

    print("\n--- Pacientes atendidos por urgencia ---")
    if pacientes_urgencia: # Si hay pacientes por urgencia, los mostramos
        for i, nro_afiliado in enumerate(pacientes_urgencia, 1): # Enumerate para mostrar el numero de orden
            print(f"{i}. Afiliado: {nro_afiliado}")
    else:
        print("No se atendieron pacientes por urgencia.")
        
    print("\n--- Pacientes atendidos por turno ---")
    if pacientes_turno:
        for i, nro_afiliado in enumerate(pacientes_turno, 1): # Enumerate para mostrar el numero de orden
            print(f"{i}. Afiliado: {nro_afiliado}")
    else:
        print("No se atendieron pacientes por turno.")

def buscar_afiliado(pacientes_urgencia: list[int], pacientes_turno: list[int]) -> None:
    """Funcion para buscar un afiliado y mostrar cuantas veces fue atendido por urgencia y por turno.
    
    Pre: Recibe dos listas: 
        - pacientes_urgencia (list): Lista de pacientes por urgencia.
        - pacientes_turno (list): Lista de pacientes por turno.

    Post: Muestra por pantalla cuantas veces fue atendido el afiliado buscado por urgencia y por turno.
    """
    # Validamos que las listas sean listas
    assert isinstance(pacientes_urgencia, list), "Error: pacientes_urgencia debe ser una lista."
    assert isinstance(pacientes_turno, list), "Error: pacientes_turno debe ser una lista."

    while True:
        nro_afiliado = int(input("\nIngrese número de afiliado a buscar o -1 para finalizar: "))
        if nro_afiliado == -1: # Si ingresa -1, finalizamos la búsqueda
            break

        # Contamos cuantas veces fue atendido por urgencia
        atenciones_urgencia = pacientes_urgencia.count(nro_afiliado)
        atenciones_turno = pacientes_turno.count(nro_afiliado)
        
        # Mostramos por pantalla los resultados
        print(f"El afiliado {nro_afiliado} fue atendido:")
        print(f"- Por urgencia: {atenciones_urgencia} veces")
        print(f"- Por turno: {atenciones_turno} veces")

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    
    # pacientes_urgencia, pacientes_turno = registrar_pacientes()
    pacientes_urgencia, pacientes_turno = registrar_pacientes()
    mostrar_listados(pacientes_urgencia, pacientes_turno)
    buscar_afiliado(pacientes_urgencia, pacientes_turno)

if __name__ == "__main__":
    main()