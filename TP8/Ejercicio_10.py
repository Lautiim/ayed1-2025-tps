def eliminarclaves(diccionario: dict, claves: list) -> tuple[dict, int]:
    """
    Elimina claves de un diccionario.

    Pre: diccionario es un dict; claves es una lista de claves a eliminar.

    Post: retorna tupla (diccionario_modificado, cantidad_eliminadas).
    """
    contador = 0

    # Iteramos sobre las claves a eliminar
    for clave in claves:
        # Intentamos eliminar; si existe, incrementamos contador
        if clave in diccionario:
            del diccionario[clave]
            contador += 1

    return diccionario, contador


def main():
    # Creamos un diccionario de ejemplo
    productos = {
        "manzana": 150,
        "banana": 80,
        "pera": 120,
        "uva": 200,
        "naranja": 90,
        "kiwi": 180,
    }

    print("Diccionario original:")
    print(productos)

    # Pedimos claves a eliminar
    print("\nIngresá las claves a eliminar (separadas por comas):")
    entrada = input("Claves: ").strip()

    if entrada:
        # Separamos por comas y limpiamos espacios
        claves_eliminar = [c.strip() for c in entrada.split(",")]

        # Llamamos a la funcion
        resultado, cantidad = eliminarclaves(productos, claves_eliminar)

        print(f"\nClaves eliminadas: {cantidad}")
        print("\nDiccionario modificado:")
        print(resultado)
    else:
        print("\nNo se ingresaron claves para eliminar.")


if __name__ == "__main__":
    main()
