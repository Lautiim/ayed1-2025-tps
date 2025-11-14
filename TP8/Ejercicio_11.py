def contarvocales(palabra: str) -> dict[str, int]:
    """
    Cuenta las vocales en una palabra.

    Pre: palabra es una cadena de texto.
    
    Post: retorna diccionario con cantidad de cada vocal (a, e, i, o, u).
    """
    # Inicializamos el diccionario con todas las vocales en 0
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertimos a minusculas y contamos
    for letra in palabra.lower():
        if letra in vocales:
            vocales[letra] += 1
    
    return vocales


def main():
    # Pedimos la frase
    frase = input("Ingresá una frase: ").strip()
    
    if not frase:
        print("No ingresaste nada.")
        return
    
    # Dividimos en palabras
    palabras = frase.split()
    
    print("\nAnálisis de vocales por palabra:")
    print("-" * 50)
    
    # Procesamos cada palabra
    for palabra in palabras:
        resultado = contarvocales(palabra)
        total = sum(resultado.values())
        
        print(f"\nPalabra: {palabra}")
        print(f"Total de vocales: {total}")
        print("Detalle:", end=" ")
        
        # Mostramos solo las vocales que aparecen
        detalles = [f"{vocal}: {cant}" for vocal, cant in resultado.items() if cant > 0]
        if detalles:
            print(", ".join(detalles))
        else:
            print("ninguna")


if __name__ == "__main__":
    main()
