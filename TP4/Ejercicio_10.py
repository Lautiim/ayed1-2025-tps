"""Desarrollar  una  función para  reemplazar  todas  las  apariciones  de  una  palabra  por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de  reemplazos  realizados.  Tener  en  cuenta  que  sólo deben  reemplazarse
palabras  completas,  y  no  fragmentos  de  palabras.  Escribir  también  un  programa
para verificar el comportamiento de la función."""

import re


def reemplazar_palabra(
    cadena: str, palabra_vieja: str, palabra_nueva: str
) -> tuple[str, int]:
    """Reemplaza todas las apariciones de una palabra completa por otra en una cadena.

    Pre: Recibe una cadena de texto, una palabra a reemplazar y la nueva palabra.

    Post: Devuelve la cadena modificada y la cantidad de reemplazos realizados.
    """
    assert isinstance(cadena, str), "La cadena debe ser una cadena de caracteres."
    assert (
        isinstance(palabra_vieja, str) and palabra_vieja
    ), "La palabra a reemplazar debe ser una cadena no vacía."
    assert isinstance(
        palabra_nueva, str
    ), "La nueva palabra debe ser una cadena de caracteres."

    # Encontramos y reemplazamos las palabras completas usando expresiones regulares
    patron = r"\b" + re.escape(palabra_vieja) + r"\b"
    # Patrón para palabra completa, \b indica límite de palabra, re.escape para manejar caracteres especiales, \b indica límite de palabra

    # Cuenta los reemplazos realizados
    cantidad_reemplazos = 0

    def contador_reemplazos(
        match: re.Match,
    ) -> str:  # Función interna para contar los reemplazos
        nonlocal cantidad_reemplazos  # Usamos nonlocal para modificar la variable externa
        cantidad_reemplazos += 1  # Incrementamos el contador
        return palabra_nueva  # Retornamos la nueva palabra para el reemplazo

    contador = 0
    nueva_cadena = re.sub(
        patron, contador_reemplazos, cadena
    )  # Reemplazamos usando la función interna

    return nueva_cadena, cantidad_reemplazos


def main():
    cadena = "La casa es grande. La casa tiene un jardín. Casamiento es una palabra diferente."
    palabra_vieja = "casa"
    palabra_nueva = "perro chiquitito"

    nueva_cadena, cantidad_reemplazos = reemplazar_palabra(
        cadena, palabra_vieja, palabra_nueva
    )

    print("Cadena original:")
    print(cadena)
    print("\nCadena modificada:")
    print(nueva_cadena)
    print(f"\nCantidad de reemplazos realizados: {cantidad_reemplazos}")


if __name__ == "__main__":
    main()
