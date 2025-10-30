def contar_subcadena(cadena: str, subcadena: str) -> int:
    """Funcion que cuenta las apariciones no superpuestas de una subcadena en una cadena, ignorando mayúsculas y minúsculas.
    De forma no necesariamente contigua.

    Pre: Recibe una cadena de caracteres y una subcadena a buscar.

    Post: Devuelve un entero con la cantidad de apariciones no superpuestas de la subcadena en la cadena, sin distinguir entre mayúsculas y minúsculas.
    """
    assert cadena is not None, "La cadena no debe ser None"
    assert subcadena is not None, "La subcadena no debe ser None"
    assert (
        cadena != "" and subcadena != ""
    ), "La cadena y la subcadena no deben estar vacías"
    assert isinstance(cadena, str) and isinstance(
        subcadena, str
    ), "La cadena y la subcadena deben ser de tipo str"

    if not subcadena:
        return 0

    texto = cadena.lower()
    patron = subcadena.lower()

    contador = 0
    j = 0  # índice en 'patron'
    for ch in texto:
        if ch == patron[j]:
            j += 1
            if j == len(patron):
                contador += 1
                j = 0  # Reinicia para buscar la siguiente ocurrencia no superpuesta
    return contador


def main():
    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
    subcadena = "UADE"
    cantidad = contar_subcadena(cadena, subcadena)
    print(f"Cantidad encontrada: {cantidad}")


if __name__ == "__main__":
    main()
