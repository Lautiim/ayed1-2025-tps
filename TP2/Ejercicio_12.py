import re

def registrar_ingresos() -> list[int]:
    """Funcion para ingresar a los socios.
    
    Pre: No tiene precondiciones.

    Post: Devuelve una lista con los numeros de socio ingresados.
    
    """
    # ingresos = []
    ingresos = [12345, 23456, 12345, 34567, 23456, 12345, 45678, 56789]

    while True: # Solicitamos datos hasta que el usuario ingrese 0
        numero_socio = int(input("Ingrese el numero de socio, debe tener 5 dígitos(0 para terminar): "))
        if numero_socio == 0:
            break
        if re.match(r"^\d{5}$", str(numero_socio)): # Verificamos que el numero tenga 5 digitos
            ingresos.append(numero_socio)
        else:
            print("Número invalido. Debe tener 5 dígitos.")
    return ingresos

def informar_ingresos(ingresos: list[int]) -> None:
    """Funcion para informar cuantas veces ingreso cada socio (sin repetir).

    Pre: Recibe una lista de enteros positivos, que representan los numeros de socio.

    Post: Imprime por pantalla la cantidad de ingresos por socio (sin repetir).
    """
    # Validamos que la lista sea una lista
    assert isinstance(ingresos, list), "El parámetro debe ser una lista."
    # Validamos que la lista sea una lista de enteros positivos
    assert all(isinstance(socio, int) and socio > 0 for socio in ingresos), "La lista debe contener solo enteros positivos."


    print("\n--- Ingresos por socio ---")
    socios_unicos = set(ingresos) # Usamos un set para obtener los socios sin repetir

    for socio in socios_unicos: # Recorremos los socios unicos
        cantidad = ingresos.count(socio) # Contamos cuantas veces ingreso el socio
        print(f"Socio {socio}: {cantidad} ingresos")

def eliminar_socio(ingresos: list[int], socio_baja: int) -> int:
    """Funicon para eliminar todos los ingresos de un socio dado de baja.

    Pre: Recibe una lista de enteros positivos, que representan los numeros de socio. Y un entero positivo, que representa el numero de socio a eliminar.

    Post: Retorna la cantidad de ingresos eliminados del socio dado de baja.
    """
    # Validamos que la lista sea una lista
    assert isinstance(ingresos, list), "El parametro debe ser una lista."
    # Validamos que la lista sea una lista de enteros positivos
    assert all(isinstance(socio, int) and socio > 0 for socio in ingresos), "La lista debe contener solo enteros positivos."
    # Validamos que el socio a eliminar sea un entero positivo
    assert isinstance(socio_baja, int) and socio_baja > 0, "El numero de socio a eliminar debe ser un entero positivo."

    # Contamos cuantas veces ingreso el socio a eliminar
    cantidad_eliminados = ingresos.count(socio_baja)
    ingresos[:] = [socio for socio in ingresos if socio != socio_baja] # Eliminamos todas las apariciones del socio a eliminar
    
    return cantidad_eliminados

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    ingresos = registrar_ingresos()
    informar_ingresos(ingresos)

    print("\nRegistros de ingresos antes de eliminar:")
    print(ingresos)

    socio_baja = int(input("\nIngrese el número de socio dado de baja: "))
    eliminados = eliminar_socio(ingresos, socio_baja)

    print("\nRegistros de ingresos después de eliminar:")
    print(ingresos)
    print(f"Se eliminaron {eliminados} ingresos del socio {socio_baja}.")

if __name__ == "__main__":
    main()