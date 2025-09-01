import random

def concatenar_numeros(num1: int, num2: int):
    """ Concatena dos números enteros positivos sin usar facilidades de Python no vistas en clase.

        Pre: Recibe dos numeros enteros (num1 y num2).

        Post: Devuelve un número entero, el resultante de concatenar num1 y num2.
    """

    if num1 < 0 or num2 < 0: # Verificamos que los numeros sean enteros positivos
        raise ValueError("Ambos numeros deben ser enteros positivos.")

    # Calculamos el factor de escala para el numero 2 (Por ej. 567)
    factor = 1 # En esta variable almacenamos el valor del factor que se necesita para desplazar num1 y dejar espacio a num2
    temp = num2 # Asignamos el valor a concatenar a temp para no modificar la informacion original
    while temp > 0: # Iteramos hasta que el valor de temp (567) sea menor a 0 (0.567)
        factor *= 10 # En cada vuelta multiplicamos por 10 el valor del factor, ya que multiplicar por 10 nos desplaza una posicion
        temp //= 10 # Hacemos una division entera para eliminar el digito desplazado (056.7), se eliminaria el 0 en la primer vuelta

    resultado = num1 * factor + num2 # Utilizando factor desplazamos los digitos de num1 para dejar espacio a num2 (1234000) y luego sumamos num2
    print(f"Numeros recibidos:\n - Número 1: {num1}\n - Número 2: {num2}")
    return resultado

print(concatenar_numeros(1234, 567))