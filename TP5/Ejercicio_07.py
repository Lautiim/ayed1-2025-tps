"""Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe  generar  un  número  al  azar  entre  1  y  500 y  el usuario  debe  adivinarlo.  Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-
mero que tiene que  adivinar es  mayor o  menor que  el ingresado. Cuando  consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el  número.  Si  el  usuario  introduce  algo  que  no  sea  un  número  se  mostrará  un 
mensaje en pantalla y se lo contará como un intento más.
"""
from random import randint

def adivina_el_numero() -> None:
    """Función de un juego para adivinar un número generado al azar entre 1 y 500.

    Pre: No recibe parámetros.

    Post: Permite al usuario intentar adivinar el número generado, proporcionando pistas
    si el número es mayor o menor. Cuenta los intentos, incluyendo entradas inválidas (no numéricas),
    y muestra el total de intentos al adivinar correctamente.
    """
    numero_azar = randint(1, 500)
    intentos = 0

    print("¡Comienza el juego!")
    print("Eligi un número entre 1 y 500. ¿Fijate si podes adivinar cuál es?")

    while True:
        entrada = input("Ingresa tu intento: ").strip()
        intentos += 1

        try:
            numero_usuario = int(entrada)

            if numero_usuario < numero_azar: # El número es mayor, el usuario debe intentar con un número mayor
                print("El número que tienes que adivinar es mayor.")
            elif numero_usuario > numero_azar: # El número es menor, el usuario debe intentar con un número menor
                print("El número que tienes que adivinar es menor.")
            else:
                print(f"¡Bien ahiii! Adivinaste el número {numero_azar} en {intentos} intentos.")
                break
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
def main():
    adivina_el_numero()
if __name__ == "__main__":
    main()
