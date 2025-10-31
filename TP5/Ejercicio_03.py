"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes  cuyo  número  se  recibe  como  parámetro.  Los  nombres  de  los  meses  deberán
obtenerse  de  una  lista  de  cadenas  de  caracteres  inicializada  dentro  de  la  función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones"""


def obtener_nombre_mes(numero_mes: int) -> str:
    """Funcion que devuelve el nombre del mes correspondiente al número recibido como parámetro.

    Pre: Recibe un número entero que representa el mes (1-12).

    Post: Devuelve el nombre del mes como un String. Si el número es inválido,
    lanza una excepción con un mensaje específico.
    """
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    try:
        if not isinstance(numero_mes, int):
            raise TypeError("El número del mes debe ser un entero.")
        if numero_mes < 1 or numero_mes > 12:
            raise ValueError("Número de mes inválido. Debe estar entre 1 y 12.")
        return meses[numero_mes - 1]
    except Exception as error:
        print(f"Error: {error}")
        return ""


def main():
    try:
        numero_mes = int(input("Ingrese el número del mes (1-12): ").strip())
        nombre_mes = obtener_nombre_mes(numero_mes)
        if nombre_mes:
            print(f"El nombre del mes es: {nombre_mes}")
        else:
            print("No se pudo obtener el nombre del mes debido a un error.")
    except ValueError:
        print("Error: La entrada no es un número entero válido.")


if __name__ == "__main__":
    main()
