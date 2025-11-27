from typing import List, Any


def _ancho_columna(matriz: List[List[Any]], col: int, fila: int = 0) -> int:
    """Devuelve el ancho máximo (len(str())) de la columna 'col' recursivamente."""
    if fila == len(matriz):
        return 0
    actual = len(str(matriz[fila][col]))
    resto = _ancho_columna(matriz, col, fila + 1)
    return actual if actual > resto else resto


def _anchos_columnas(matriz: List[List[Any]], col: int = 0) -> List[int]:
    """Construye la lista de anchos por columna recursivamente."""
    if not matriz:
        return []
    if col == len(matriz[0]):
        return []
    return [_ancho_columna(matriz, col)] + _anchos_columnas(matriz, col + 1)


def _imprimir_elementos_fila(
    matriz: List[List[Any]], fila: int, col: int, anchos: List[int]
) -> None:
    """Imprime recursivamente los elementos de una fila."""
    if col == len(matriz[fila]):
        return
    print(f"{matriz[fila][col]:>{anchos[col]}}", end=" ")
    _imprimir_elementos_fila(matriz, fila, col + 1, anchos)


def _imprimir_filas(matriz: List[List[Any]], fila: int, anchos: List[int]) -> None:
    """Imprime cada fila recursivamente."""
    if fila == len(matriz):
        return
    _imprimir_elementos_fila(matriz, fila, 0, anchos)
    print()  # fin de la fila
    _imprimir_filas(matriz, fila + 1, anchos)


def imprimir_matriz_recursiva(matriz: List[List[Any]]) -> None:
    """Imprime una matriz MxN con columnas alineadas usando solo recursión."""
    if not matriz:
        print("(matriz vacía)")
        return
    anchos = _anchos_columnas(matriz)
    _imprimir_filas(matriz, 0, anchos)


if __name__ == "__main__":
    casos = [
        [],
        [[5]],
        [[1, 20, 3], [400, 5, 6], [7, 8, 900]],
        [[-1, -200, 3], [40, -5, 600], [7000, 8, -9]],
    ]
    for i, matriz in enumerate(casos, 1):
        print(f"Caso {i}:")
        imprimir_matriz_recursiva(matriz)
        print("-" * 40)
