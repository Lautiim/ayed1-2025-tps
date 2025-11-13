import string


def limpiar_palabra(palabra: str) -> str:
    """
    Elimina signos de puntuacion de una palabra.

    Pre: palabra es una cadena de texto.

    Post: retorna la palabra sin puntuacion, en minusculas.
    """
    # Quitamos puntuacion y convertimos a minuscula
    sin_puntuacion = "".join(ch for ch in palabra if ch not in string.punctuation)
    return sin_puntuacion.lower()


def palabras_unicas_ordenadas(frase: str) -> list[str]:
    """
    Extrae palabras unicas y las ordena por longitud.

    Pre: frase es una cadena de texto.

    Post: retorna lista de palabras unicas ordenadas por longitud.
    """
    # Dividimos en palabras
    palabras = frase.split()

    # Limpiamos y agregamos a un conjunto para eliminar repetidas
    palabras_limpias = set()
    for palabra in palabras:
        limpia = limpiar_palabra(palabra)
        if limpia:  # solo agregamos si no quedo vacia
            palabras_limpias.add(limpia)

    # Ordenamos por longitud y luego alfabeticamente para desempate
    lista = list(palabras_limpias)
    lista.sort()  # primero alfabeticamente
    lista.sort(key=len)  # luego por longitud (estable)
    ordenadas = lista
    return ordenadas


def main():
    # Pedimos la frase y mostramos las palabras unicas ordenadas
    frase = input("Ingresá una frase: ").strip()
    if not frase:
        print("No ingresaste nada.")
        return

    palabras = palabras_unicas_ordenadas(frase)

    print("\nPalabras únicas ordenadas por longitud:")
    for palabra in palabras:
        print(palabra)


if __name__ == "__main__":
    main()
