def obtener_claves(clave_maestra: int) -> tuple[int, int]:
    """Función para obtener las claves de las cajas fuertes a partir de la clave maestra

    Pre: Recibe un número entero que representa la clave maestra

    Post: Devuelve una tupla con dos enteros, la primera clave (impar) y la segunda clave (par)
    """
    assert clave_maestra >= 0, "La clave maestra debe ser un número entero no negativo"
    assert isinstance(clave_maestra, int), "La clave maestra debe ser un número entero"

    clave1 = 0  # Clave de la primera caja fuerte
    clave2 = 0  # Clave de la segunda caja fuerte
    posicion = 1  # Posición del dígito actual (1 para impar, 2 para par)
    multiplicador1 = 1  # Multiplicador para la primera clave
    multiplicador2 = 1  # Multiplicador para la segunda clave

    while clave_maestra > 0:
        digito = clave_maestra % 10  # Obtenemos el último dígito
        if posicion % 2 != 0:  # Posición impar
            clave1 += digito * multiplicador1  # Construimos la primera clave
            multiplicador1 *= 10  # Actualizamos el multiplicador
        else:  # Posición par
            clave2 += digito * multiplicador2  # Construimos la segunda clave
            multiplicador2 *= 10  # Actualizamos el multiplicador
        clave_maestra //= 10  # Eliminar el último dígito
        posicion += 1

    return clave1, clave2


def main():
    clave_maestra = int(input("Ingrese la clave maestra (número entero): "))
    clave1, clave2 = obtener_claves(clave_maestra)
    print(f"La primera clave (impar) es: {clave1}")
    print(f"La segunda clave (par) es: {clave2}")


if __name__ == "__main__":
    main()
