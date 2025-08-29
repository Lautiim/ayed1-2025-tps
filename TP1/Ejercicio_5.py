import random

def __main__():
    # Funcion para determinar si un numero es oblongo.
    # Un numero es oblongo cuando es resultado de la multiplicacion de dos numeros    
    es_oblongo = lambda i, num: i * (i+1) == num
    es_triangular = lambda i, num: i * (i+1) / 2 == num

    # Generamos un numero random del 1 al 100.
    num = random.randint(1, 100)

    # Iteramos empezando desde 1 hasta llegar al numero generado
    for i in range(1, num):
        if es_oblongo(i, num): # Si se encuentra que el numero es oblongo se detiene el bucle
            print(f"El numero {num} es oblongo")
            break
    else: # Si no se encuentra que el numero es oblongo el bucle finaliza y se informa al usuario.
        print(f"El numero {num} no es oblongo")

    for i in range(1, num):
        if es_triangular(i, num):
            print(f"El numero {num} es triangular")
            break
    else:
        print(f"El numero {num} no es triangular")

if __name__ == "__main__":
    __main__()