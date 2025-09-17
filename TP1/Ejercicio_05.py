import random

def __main__():

    # Generamos un numero random del 1 al 100.
    num = 10
    
    # Funcion para determinar si un numero es oblongo.
    # Un numero es oblongo cuando es resultado de la multiplicacion de dos numeros    
    es_oblongo = lambda num: any((i * (i + 1)) == num for i in range(1, num)) # Utilizando any() debido a que no se puede iterar en un lambda
    es_triangular = lambda num: any((i * (i + 1) / 2) == num for i in range(1, num)) # any() devuelve verdadero si en algun caso se cumple la sentencia

    # Iteramos empezando desde 1 hasta llegar al numero generado
    if es_oblongo(num):  # Si se encuentra que el numero es oblongo se detiene el bucle
        print(f"El numero {num} es oblongo")
    else:  # Si no se encuentra que el numero es oblongo el bucle finaliza y se informa al usuario.
        print(f"El numero {num} no es oblongo")

    if es_triangular(num):
        print(f"El numero {num} es triangular")
    else:
        print(f"El numero {num} no es triangular")

if __name__ == "__main__":
    __main__()