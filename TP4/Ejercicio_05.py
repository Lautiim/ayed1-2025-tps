def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """Función que filtra las palabras de una frase que tienen N o más caracteres utilizando ciclos (for) normales

    Pre: Recibe una cadena de caracteres y un entero N que indica la longitud mínima de las palabras a filtrar

    Post: Devuelve una cadena con las palabras que tienen N o más caracteres
    """
    assert isinstance(frase, str), "La frase debe ser una cadena de caracteres"
    assert isinstance(n, int) and n >= 0, "N debe ser un entero no negativo"

    palabras = frase.split()  # Dividimos la frase en palabras
    resultado = []  # Almacenará las palabras filtradas

    for palabra in palabras:  # Recorremos cada palabra
        if len(palabra) >= n:  # Si la longitud de la palabra es mayor o igual a N
            resultado.append(palabra)  # La añadimos al resultado

    return " ".join(
        resultado
    )  # Unimos las palabras filtradas en una sola cadena separadas por espacios


def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """Función que filtra las palabras de una frase que tienen N o más caracteres utilizando listas por comprensión

    Pre: Recibe una cadena de caracteres y un entero N que indica la longitud mínima de las palabras a filtrar

    Post: Devuelve una cadena con las palabras que tienen N o más caracteres
    """
    assert isinstance(frase, str), "La frase debe ser una cadena de caracteres"
    assert isinstance(n, int) and n >= 0, "N debe ser un entero no negativo"

    palabras = frase.split()  # Dividimos la frase en palabras
    resultado = [
        palabra for palabra in palabras if len(palabra) >= n
    ]  # Lista por comprensión para filtrar las palabras
    # Si la longitud de la palabra es mayor o igual a N, la añadimos al resultado

    return " ".join(
        resultado
    )  # Unimos las palabras filtradas en una sola cadena separadas por espacios


def filtrar_palabras_filter(frase: str, n: int) -> str:
    """Función que filtra las palabras de una frase que tienen N o más caracteres utilizando la función filter

    Pre: Recibe una cadena de caracteres y un entero N que indica la longitud mínima de las palabras a filtrar

    Post: Devuelve una cadena con las palabras que tienen N o más caracteres
    """
    assert isinstance(frase, str), "La frase debe ser una cadena de caracteres"
    assert isinstance(n, int) and n >= 0, "N debe ser un entero no negativo"

    palabras = frase.split()  # Dividimos la frase en palabras

    # Aca usamos un lambda para definir la función que filtra las palabras
    # La función lambda toma una palabra y devuelve True si su longitud es mayor o igual a N, False en caso contrario
    resultado = filter(
        lambda palabra: len(palabra) >= n, palabras
    )  # Filtramos las palabras usando filter

    return " ".join(resultado)  # Unimos las palabras filtradas en una sola cadena


def main():
    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese el valor de N (entero no negativo): "))

    print("\nFiltrado utilizando ciclos normales:")
    print(filtrar_palabras_ciclos(frase, n))

    print("\nFiltrado utilizando listas por comprensión:")
    print(filtrar_palabras_comprension(frase, n))

    print("\nFiltrado utilizando la función filter:")
    print(filtrar_palabras_filter(frase, n))


if __name__ == "__main__":
    main()
