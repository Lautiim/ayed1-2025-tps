from typing import List


def _suma_fila(fila: List[int], idx: int = 0) -> int:
    """Suma recursivamente los elementos de una fila."""
    if idx == len(fila):
        return 0
    return fila[idx] + _suma_fila(fila, idx + 1)


def _suma_matriz(matriz: List[List[int]], fila: int = 0) -> int:
    """Suma recursivamente las filas de la matriz."""
    if fila == len(matriz):
        return 0
    return _suma_fila(matriz[fila]) + _suma_matriz(matriz, fila + 1)


def sumar_matriz(matriz: List[List[int]]) -> int:
    """Devuelve la suma de todos los elementos de la matriz MxN."""
    return _suma_matriz(matriz)


if __name__ == "__main__":
    casos = [
        [],  # matriz vacía
        [[5]],  # 1x1
        [[1, 2, 3], [4, 5, 6]],  # rectangular
        [[-1, -2], [3, -4], [10]],  # mezcla de negativos y positivos
        [[0, 0, 0], [0], [0, 0]],  # todos ceros
    ]
    for i, m in enumerate(casos, 1):
        print(f"Caso {i}: {m} -> suma = {sumar_matriz(m)}")
