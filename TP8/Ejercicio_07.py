def main():
    # Creamos el conjunto con numeros del 0 al 9
    numeros = set(range(10))
    
    print("Conjunto inicial:", numeros)
    print("\nIngresá números para eliminar del conjunto (o -1 para salir).")
    
    while True:
        try:
            # Pedimos un valor
            valor = int(input("\nValor a eliminar: "))
            
            # Si es -1, terminamos
            if valor == -1:
                print("\nFinalizando...")
                break
            
            # Intentamos eliminar usando remove
            try:
                numeros.remove(valor)
                print(f"Eliminado: {valor}")
            except KeyError:
                print(f"El valor {valor} no está en el conjunto.")
            
            # Mostramos el conjunto actualizado
            if len(numeros) == 0:
                print("El conjunto está vacío.")
            else:
                print("Conjunto actual:", numeros)
            
        except ValueError:
            print("Por favor, ingresá un número entero válido.")
    
    if len(numeros) == 0:
        print("\nConjunto final: vacío")
    else:
       print("\nConjunto final:", numeros)


if __name__ == "__main__":
    main()
