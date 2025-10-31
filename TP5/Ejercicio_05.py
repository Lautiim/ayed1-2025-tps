"""La  raíz  cuadrada  de  un  número  puede  obtenerse  mediante  la  función  sqrt()  del
módulo  math.  Escribir  un  programa  que  utilice  esta  función  para  calcular  la  raíz
cuadrada  de  un  número  cualquiera  ingresado  a  través  del  teclado.  El  programa
debe  utilizar  manejo  de  excepciones  para  evitar  errores  si  se  ingresa  un  número
negativo"""

from math import sqrt  # Importamos solo la función sqrt del módulo math je.


def calcular_raiz_cuadrada() -> None:
    """Funcion que solicita al usuario ingresar un número y calcula su raíz cuadrada.

    Pre: No recibe parámetros.

    Post: Imprime la raíz cuadrada del número ingresado. Si el número es negativo,
    levanta la excepción e informa al usuario.
    """
    try:
        numero = float(
            input("Ingrese un número para calcular su raíz cuadrada: ").strip()
        )
        if numero < 0:
            raise ValueError(
                "No se puede calcular la raíz cuadrada de un número negativo."
            )
        raiz_cuadrada = sqrt(numero)
        print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}.")
    except ValueError as error:
        print(f"Error: {error}")
    except Exception:
        print("Error: La entrada no es un número válido.")


def main():
    calcular_raiz_cuadrada()


if __name__ == "__main__":
    main()
