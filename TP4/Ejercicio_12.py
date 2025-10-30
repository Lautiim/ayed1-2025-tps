def crear_baraja_espanola() -> list[str]:
    palos = ["Oro", "Copa", "Espada", "Basto"]  # Palos de una baraja española
    numeros = [str(n) for n in range(1, 13)]  # Números del 1 al 12 como cadenas

    # Crear la lista de naipes usando una lista por comprensión
    # Para cada palo, combinarlo con cada número
    baraja = [f"{numero} {palo}" for palo in palos for numero in numeros]

    return baraja


def main():
    baraja = crear_baraja_espanola()
    print(baraja)


if __name__ == "__main__":
    main()
