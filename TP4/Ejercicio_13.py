def numero_a_letras(numero: int) -> str:
    """Convierte un número entero entre 0 y 1 billón a su representación en letras.

    Pre: Recibe un número entero en el rango de 0 a 1 billón

    Post: Devuelve una cadena con la representación en letras del número.
    """
    assert isinstance(numero, int), "El número debe ser un entero."
    assert 0 <= numero <= 1_000_000_000_000, "El número debe estar entre 0 y 1 billón."

    unidades = [
        "",
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
    ]
    decenas_especiales = {
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince",
        16: "dieciséis",
        17: "diecisiete",
        18: "dieciocho",
        19: "diecinueve",
    }
    decenas = [
        "",
        "diez",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    ]
    centenas = [
        "",
        "ciento",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    ]

    if numero == 0:
        return "cero"
    if numero == 1_000_000_000_000:
        return "un billón"

    def procesar_tres_digitos(n: int) -> str:
        if n == 0:
            return ""

        resultado = ""

        # Centenas
        if n >= 100:
            if n == 100:
                resultado = "cien"
                return resultado
            resultado += centenas[n // 100] + " "
            n %= 100

        # Decenas especiales (10-19)
        if 10 <= n <= 19:
            return (resultado + decenas_especiales[n]).strip()

        # Decenas (20-90)
        if n >= 20:
            if n % 10 == 0:
                resultado += decenas[n // 10]
            else:
                if n // 10 == 2:
                    resultado += "veinti" + unidades[n % 10]
                else:
                    resultado += decenas[n // 10] + " y " + unidades[n % 10]
            return resultado.strip()

        # Unidades (1-9)
        if n > 0:
            resultado += unidades[n]

        return resultado.strip()

    partes = []

    # Mil millones
    if numero >= 1_000_000_000:
        cantidad = numero // 1_000_000_000
        if cantidad == 1:
            partes.append("mil millones")
        else:
            partes.append(procesar_tres_digitos(cantidad) + " mil millones")
        numero %= 1_000_000_000

    # Millones
    if numero >= 1_000_000:
        cantidad = numero // 1_000_000
        if cantidad == 1:
            partes.append("un millón")
        else:
            partes.append(procesar_tres_digitos(cantidad) + " millones")
        numero %= 1_000_000

    # Miles
    if numero >= 1_000:
        cantidad = numero // 1_000
        if cantidad == 1:
            partes.append("mil")
        else:
            partes.append(procesar_tres_digitos(cantidad) + " mil")
        numero %= 1_000

    # Unidades, decenas y centenas
    if numero > 0:
        partes.append(procesar_tres_digitos(numero))

    return " ".join(partes).strip()


def main():
    numeros_prueba = [
        0,
        1,
        15,
        20,
        21,
        100,
        912,
        1000,
        1500,
        10000,
        999999,
        1000000,
        1000000000,
    ]
    for numero in numeros_prueba:
        print(f"Número: {numero}")
        print(f"En letras: {numero_a_letras(numero)}\n")


if __name__ == "__main__":
    main()
