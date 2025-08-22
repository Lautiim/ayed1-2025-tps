def calcular_cambio(monto: int, recibido: int) -> list:
    """Calcula el cambio a devolver en billetes.

    Pre: Recibe dos numeros enteros, uno representando el monto total y el otro la cantidad de dinero entregada.

    Post: Devuelve una lista con la cantidad de billetes a devolver de cada nomenclatura.

    """
    # Se verifica que los numeros sean enteros
    assert(isinstance(monto, int)), "El monto debe ser un numero entero"
    assert(isinstance(recibido, int)), "La cantidad de billetes debe ser un numero entero"

    valor_cambio = recibido - monto # Calculamos el cambio a devolver
    detalle_cambio = [] # Iniciamos la lista con la cantidad de billetes de cada valor.

    if valor_cambio < 0:
        assert valor_cambio < 0, "El dinero entregado es menor que el total a pagar"
    elif valor_cambio == 0:
        return [0, 0, 0, 0, 0, 0, 0] # Si el cambio es cero se devuelve una lista con ceros. Es decir, no hay cambio que devolver.
    elif ((recibido - monto) % 10 != 0): # Si el cambio no es un multiplo de 10 no existe un billete que cubra la necesidad
        assert ((recibido - monto) % 10 != 0), "El cambio no se puede devolver debido a la falta de billetes con denominacion adecuada."
    else:
        for valor in valores_billetes: # Recorremos los valores de los billetes
            # Calculamos la cantidad de billetes de ese valor, haciendo una division entera entre el cambio entre el valor del billete
            cantidad_billetes = valor_cambio // valor 
            valor_cambio %= valor # Calculamos el resto del cambio.

            detalle_cambio.append(cantidad_billetes) # Se agrega la cantidad de billetes de ese valor a la lista.
        
        return detalle_cambio

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    
    # Se solicita el monto total y el dinero recibido al usuario
    monto_total = int(input("\nIngrese el monto total: "))
    recibido = int(input("Ingrese el dinero recibido (-1 para cancelar): "))

    while recibido != -1:  # Se repite el hasta que el usuario ingrese -1
        if recibido < monto_total: # Si el dinero recibido es menor al monto total
            print("\nEl dinero recibido es menor que el monto total.")
        elif recibido == monto_total: # Si el dinero recibido es igual al monto total
            print("\nNo hay cambio que devolver.")
        elif ((recibido - monto_total) % 10 != 0): # Si el cambio no es un multiplo de 10 no existe un billete que cubra la necesidad
            print("\nEl cambio no se puede devolver debido a la falta de billetes con denominacion adecuada.")
        else: # Si el monto recibido es mayor al monto total
            cambio = calcular_cambio(monto_total, recibido) # Se llama a la funcion para calcular el cambio
            
            print("\nEl cambio a devolver es:")
            for i in range(len(valores_billetes)):
                print(f" - {cambio[i]} billetes de ${valores_billetes[i]}")

        monto_total = int(input("\nIngrese el monto total: "))
        recibido = int(input("Ingrese el dinero recibido (-1 para cancelar): "))

valores_billetes = [5000, 1000, 500, 200, 100, 50, 10] # Definimos la lista de valores de los billetes

if __name__ == "__main__":
    main()