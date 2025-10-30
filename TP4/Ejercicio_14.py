def verificar_email(email: str) -> bool:
    """Verifica si una dirección de correo electrónico es válida según los criterios dados.

    Pre: Recibe una cadena de caracteres que representa un correo electrónico.

    Post: Devuelve True si el correo es válido, False en caso contrario.
    """
    assert isinstance(email, str), "El correo electrónico debe ser una cadena de caracteres."
    assert email, "El correo electrónico no debe estar vacío."

    if email.count("@") != 1: # Si no tiene exactamente un '@', no es válido
        return False

    usuario, dominio = email.split("@") # Dividimos en usuario y dominio según el '@'

    if not usuario.isalnum(): # Verificamos que el usuario sea alfanumérico
        return False

    if not dominio or not (dominio.endswith(".com") or dominio.endswith(".com.ar")): # Verificamos el dominio, si está vacío o no termina correctamente (no .com o .com.ar)
        return False

    return True


def main():
    dominios = set() # Uso un set para almacenar dominios únicos

    while True:
        email = input(
            "Ingrese una dirección de correo electrónico (o presione Enter para finalizar): "
        ).strip() # Eliminamos espacios en blanco al inicio y al final
        if email == "": # Si la entrada está vacía, salimos del bucle
            break

        if verificar_email(email): # Verificamos si el email es válido, y si lo es, extraemos el dominio
            print(f"La dirección '{email}' es válida.")
            dominio = email.split("@")[1].lower()
            dominios.add(dominio)
        else: # Si el email no es válido, mostramos un mensaje de error
            print(f"La dirección '{email}' no es válida.")

    print("\nDominios únicos y ordenados:")
    for dominio in sorted(dominios): # Ordenamos los dominios y los mostramos únicos
        print(dominio)


if __name__ == "__main__":
    main()
