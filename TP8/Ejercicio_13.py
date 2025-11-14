def buscarclave(diccionario: dict, valor: int) -> list:
    """
    Encuentra todas las claves que apuntan a un valor especifico.

    Pre: diccionario es un dict; valor es el valor a buscar.

    Post: retorna lista de claves cuyo valor coincide con el buscado.
    """
    claves_encontradas = []
    
    # Iteramos sobre el diccionario
    for clave, val in diccionario.items():
        if val == valor:
            claves_encontradas.append(clave)
    
    return claves_encontradas


def main():
    # Creamos un diccionario de ejemplo con valores repetidos
    notas = {
        "Juan": 8,
        "María": 10,
        "Pedro": 8,
        "Ana": 7,
        "Luis": 10,
        "Sofia": 8,
        "Carlos": 9,
        "Laura": 10
    }
    
    print("=== BÚSQUEDA DE CLAVES POR VALOR ===\n")
    
    # Mostramos el diccionario
    print("Diccionario de notas:")
    print("-" * 40)
    for nombre, nota in sorted(notas.items()):
        print(f"{nombre:.<25} {nota}")
    
    # Probamos la función con diferentes valores
    print("\n" + "=" * 40)
    print("PRUEBAS DE BÚSQUEDA:")
    print("=" * 40)
    
    # Test 1: Buscar estudiantes con nota 10
    print("\n1. Estudiantes con nota 10:")
    resultado = buscarclave(notas, 10)
    print(f"   Encontrados: {resultado}")
    
    # Test 2: Buscar estudiantes con nota 8
    print("\n2. Estudiantes con nota 8:")
    resultado = buscarclave(notas, 8)
    print(f"   Encontrados: {resultado}")
    
    # Test 3: Buscar estudiantes con nota 5 (no existe)
    print("\n3. Estudiantes con nota 5:")
    resultado = buscarclave(notas, 5)
    if resultado:
        print(f"   Encontrados: {resultado}")
    else:
        print("   No se encontraron estudiantes con esa nota.")
    
    # Test 4: Búsqueda interactiva
    print("\n" + "=" * 40)
    print("BÚSQUEDA INTERACTIVA:")
    print("=" * 40)
    
    try:
        valor_buscar = int(input("\nIngresá una nota a buscar (1-10): "))
        resultado = buscarclave(notas, valor_buscar)
        
        if resultado:
            print(f"\nEstudiantes con nota {valor_buscar}:")
            for nombre in resultado:
                print(f"  - {nombre}")
        else:
            print(f"\nNo hay estudiantes con nota {valor_buscar}.")
    except ValueError:
        print("Valor inválido.")


if __name__ == "__main__":
    main()
