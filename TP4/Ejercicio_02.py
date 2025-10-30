def main():
    cadena = input(
        "Ingrese una cadena: "
    )  # Solicitamos al usuario que ingrese una cadena de caracteres
    longitud = len(cadena)
    espacios = 80 - longitud
    if espacios > 0:  # Si la cadena es más corta que 80 caracteres, la centramos
        print(" " * (espacios // 2) + cadena)
    else:
        print(
            cadena
        )  # Si la cadena es igual o más larga que 80 caracteres, la imprimimos como lo que es.


if __name__ == "__main__":
    main()
