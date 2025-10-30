"""Escribir una función que reciba como parámetro una cadena de caracteres en la que
las  palabras  se  encuentran  separadas  por  uno  o  más  espacios.  Devolver  otra
cadena  con  las  palabras  ordenadas  según  su  longitud,  dejando  un  espacio  entre
cada  una.  Los  signos  de  puntuación  no  deben  ser  tenidos  en  cuenta  al  medir  la
longitud de las palabras, pero deberán conservarse en la cadena final."""

import re


def ordenar_palabras_por_longitud(cadena: str) -> str:
    # Dividimos la cadena en palabras usando expresiones regulares.
    palabras = re.findall(
        r"\S+", cadena
    )  # \S+ coincide con secuencias de caracteres no espaciales (palabras)

    # Función para calcular la longitud de una palabra sin signos de puntuación

    # Usamos una expresión regular para eliminar los signos de puntuación, y luego calculamos la longitud.
    longitud_sin_puntuacion = lambda palabra: len(re.sub(r"[^\w]", "", palabra))

    # Ordenar las palabras según su longitud sin signos de puntuación
    palabras_ordenadas = sorted(palabras, key=longitud_sin_puntuacion)

    # Unir las palabras ordenadas en una sola cadena con un espacio entre ellas
    resultado = " ".join(palabras_ordenadas)

    return resultado


def main():
    cadena = "Hola,   mundo! Esto es  una prueba."
    resultado = ordenar_palabras_por_longitud(cadena)
    print("Cadena original:")
    print(cadena)
    print("Cadena con palabras ordenadas por longitud:")
    print(resultado)


if __name__ == "__main__":
    main()
