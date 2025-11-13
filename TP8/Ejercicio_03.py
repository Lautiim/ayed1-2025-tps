def partes_correo(correo: str) -> tuple:
    """
    Funcion que valida y separa un correo electronico en sus partes.

    Pre: correo es una cadena con un email a validar.

    Post: retorna (local, dom1, dom2, ...) o () si el formato es invalido.
    """
    # Si no es string, ya fue
    if not isinstance(correo, str):
        return ()

    # No permitimos espacios ni caracteres de control (tabs, saltos de linea, etc)
    if any(ch.isspace() for ch in correo):
        return ()

    # Debe haber exactamente un '@'
    if correo.count("@") != 1:
        return ()

    local, dominio = correo.split("@")

    # Local y dominio no pueden ser vacios
    if not local or not dominio:
        return ()

    # No permitimos puntos consecutivos ni puntas con punto
    if ".." in local or ".." in dominio:
        return ()
    if local[0] == "." or local[-1] == ".":
        return ()
    if dominio[0] == "." or dominio[-1] == ".":
        return ()

    # Validar caracteres del local: letras, digitos y . _ - +
    for ch in local:
        if not (ch.isalnum() or ch in "._-+"):
            return ()

    # El dominio debe tener al menos un punto (e.g., uade.edu)
    labels = dominio.split(".")
    if len(labels) < 2:
        return ()

    # Validar cada etiqueta del dominio: letras/digitos o '-'; sin iniciar/terminar con '-'
    for lab in labels:
        if not lab:  # evita etiquetas vacias por '..'
            return ()
        if lab[0] == "-" or lab[-1] == "-":
            return ()
        for ch in lab:
            if not (ch.isalnum() or ch == "-"):
                return ()

    # Si llegamos hasta aca, esta todo bien
    return tuple([local] + labels)


def main():
    # Pedimos un correo y mostramos las partes o tupla vacia si es invalido
    correo = input("Ingresá un correo electrónico: ").strip()
    partes = partes_correo(correo)
    if partes:
        print(partes)
    else:
        print("Formato inválido. Tupla vacía: ()")


if __name__ == "__main__":
    main()
