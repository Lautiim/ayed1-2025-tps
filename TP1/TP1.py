def mayor(num1 :int, num2 :int, num3 :int) -> int:
    """ Obtener el mayor de 3 numeros

    Pre: Recibe tres numeros, los numeros deben ser enteros.

    Post: Devuelve el valor del mayor de los tres numeros recibidos, en caso de que no exista un mayor unico devuelve -1

    """
    # Se verifica que los numeros sean enteros
    assert(isinstance(num1, int)), "Los numeros deben ser enteros"
    assert(isinstance(num2, int)), "Los numeros deben ser enteros"
    assert(isinstance(num3, int)), "Los numeros deben ser enteros"

    if num1 == num2: # Si no existe un numero mayor la funcion devuelve
        if num1 == num3: 
            return -1
    else:
        return max(num1, num2, num3)

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    
    # Se solicitan tres numeros enteros al usuario
    num1 = int(input("Ingrese el primer numero.. "))
    num3 = int(input("Ingrese el tercer numero.. "))
    num2 = int(input("Ingrese el segundo numero.. "))

    resultado = mayor(num1, num2, num3) # Se llama a la funcion que calcula el mayor de los tres numeros

    # Se imprime el resultado
    if resultado == -1:
        print("\nNo hay un mayor unico.")
    else:
        print(f"\nEl mayor de los tres numeros es: {resultado}")

if __name__ == "__main__":
    main()