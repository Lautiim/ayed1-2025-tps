def ingresar_numero_natural() -> int:
    """Solicita al usuario ingresar un número natural y valida la entrada.

    Pre: No recibe parámetros.

    Post: Devuelve un número natural (entero mayor que 0) ingresado por el usuario o lanza excepciones con mensajes
    específicos en caso de errores de validación.
    """
    while True:
        entrada = input("Ingrese un número natural (entero mayor que 0): ").strip()

        try:
            try:
                numero = float(
                    entrada
                )  # Añadimos otro try para capturar errores de conversión a float
            except ValueError:
                raise ValueError("La entrada no es un número.")
            if not numero.is_integer():
                raise ValueError("El número debe ser un entero.")
            numero = int(numero)  # Convertimos a entero
            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            return numero  # Si todo es correcto, devolvemos el número
        except ValueError as error:
            print(f"Error: {error}")
        except Exception:
            print("Error: La entrada no es un número válido.")


def main():
    numero_natural = ingresar_numero_natural()
    print(f"Número natural ingresado correctamente: {numero_natural}")


if __name__ == "__main__":
    main()
