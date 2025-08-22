def total_viajes(viajes :int) -> float:
    """Funcion para calcular el total de gastos al viajar en subte dentro de un mes.

    Pre: Recibe un numero entero, que representa la cantidad de viajes.

    Post: Devuelve un numero flotante, representando el total de gastos en subte del mes.

    """
    # Se verifica que la variable viajes sea de tipo entero
    assert(isinstance(viajes, int)), "La cantidad de viajes debe ser un numero entero"

    valor_viaje = 1531.17  # Valor del viaje en subte actualizado segun buenosaires.gob.ar (21/08/2025)

    gasto_total = 0.0

    if viajes <= 0: # Si la cantidad de viajes es negativa o cero, se devuelve 0
        return gasto_total
    else:
        for i in range(1, viajes + 1): # Se empieza a calcular el gasto total, empezamos desde 1 y repetimos la cantidad de veces que se haya viajado.
            if i <= 20:
                gasto_total += valor_viaje  # Entre 1 y 20 viajes el valor es el normal
            elif i <= 30: # Entre 21 y 30 viajes el valor tiene un 20% de descuento 
                gasto_total += (valor_viaje * 0.80)
            elif i <= 40: # Entre 31 y 40 viajes el valor tiene un 30% de descuento
                gasto_total += (valor_viaje * 0.70)
            elif i > 40: # A partir de mas de 40 viajes el valor tiene un 40% de descuento
                gasto_total += (valor_viaje * 0.60)

        return gasto_total
    
def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")

    # Se solicita una cantidad de viajes realizados al usuario para validar la funcion
    viajes = int(input("Ingrese la cantidad de viajes realizados en el mes (-1 para salir): "))

    while viajes != -1:  # Se repite el hasta que el usuario ingrese -1
        total = total_viajes(viajes) # Se llama a la funcion para calcular el total gastado
        
        print(f"El total gastado en subte es: ${total:.2f}") # Se le muestra al usuario el total gastado.
        
        viajes = int(input("Ingrese la cantidad de viajes realizados en el mes (-1 para salir): "))

    print("\nNos vemoss!!!!")  # Mensaje de despedida al usuario

if __name__ == "__main__":
    main()