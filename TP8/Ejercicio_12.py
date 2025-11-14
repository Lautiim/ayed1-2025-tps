def incrementar_precios_cuadernos(precios: dict, porcentaje: float = 15):
    """
    Incrementa el precio de todos los articulos que contengan 'cuaderno'.

    Pre: precios es un diccionario; porcentaje es un numero.

    Post: modifica los precios de cuadernos in-place.
    """
    for articulo in precios:
        # Buscamos la palabra 'cuaderno' (insensible a mayusculas)
        if "cuaderno" in articulo.lower():
            precios[articulo] *= 1 + porcentaje / 100


from collections.abc import Mapping


def encontrar_mas_caro(
    precios: Mapping[str, float | int],
) -> tuple[str | None, float | int]:
    """
    Encuentra el articulo mas costoso.

    Pre: precios es un diccionario no vacio.

    Post: retorna tupla (articulo, precio) del item mas caro.
    """
    if not precios:
        return None, 0

    articulo_max = max(precios, key=lambda k: precios[k])
    return articulo_max, precios[articulo_max]


def main():
    # Creamos el diccionario de precios
    precios = {
        "Lapicera azul": 350,
        "Cuaderno tapa dura 100 hojas": 1500,
        "Cuaderno tapa blanda 48 hojas": 800,
        "Resaltador amarillo": 450,
        "Carpeta A4": 650,
        "Cuaderno universitario 200 hojas": 2500,
        "Goma de borrar": 120,
        "Regla 30cm": 280,
        "Marcador negro": 520,
        "Tijera escolar": 890,
    }

    print("=== LIBRERÍA - SISTEMA DE PRECIOS ===\n")

    # Mostramos precios originales
    print("1. Lista de precios ORIGINAL:")
    print("-" * 50)
    for articulo, precio in sorted(precios.items()):
        print(f"{articulo:.<40} ${precio:>8.2f}")

    # Incrementamos precios de cuadernos
    incrementar_precios_cuadernos(precios, 15)

    # Mostramos precios actualizados
    print("\n2. Lista de precios ACTUALIZADA (cuadernos +15%):")
    print("-" * 50)
    for articulo, precio in sorted(precios.items()):
        # Marcamos los cuadernos con un asterisco
        marca = " *" if "cuaderno" in articulo.lower() else ""
        print(f"{articulo:.<40} ${precio:>8.2f}{marca}")

    # Encontramos el item mas caro
    mas_caro, precio_max = encontrar_mas_caro(precios)

    print("\n3. Artículo MÁS COSTOSO:")
    print("-" * 50)
    print(f"Artículo: {mas_caro}")
    print(f"Precio: ${precio_max:.2f}")


if __name__ == "__main__":
    main()
