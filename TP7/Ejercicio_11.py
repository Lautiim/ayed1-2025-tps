from typing import List


def _min_fila(fila: List[int], idx: int = 0) -> int:
    """Devuelve el mínimo de la fila recursivamente."""
    if not fila:
        raise ValueError("Fila vacía: no se puede determinar mínimo")
    if idx == len(fila) - 1:
        return fila[idx]
    resto = _min_fila(fila, idx + 1)
    return fila[idx] if fila[idx] < resto else resto


def _min_matriz(matriz: List[List[int]], fila: int = 0) -> int:
    """Devuelve el mínimo de la matriz recursivamente."""
    if not matriz:
        raise ValueError("Matriz vacía: no se puede determinar mínimo")
    if fila == len(matriz) - 1:
        return _min_fila(matriz[fila])
    resto = _min_matriz(matriz, fila + 1)
    min_fila_actual = _min_fila(matriz[fila])
    return min_fila_actual if min_fila_actual < resto else resto


def minimo_matriz(matriz: List[List[int]]) -> int:
    """Función pública: retorna el mínimo de la matriz MxN."""
    return _min_matriz(matriz)


if __name__ == "__main__":
    casos = [
        [[5]],
        [[3, 2, 7], [9, -1, 4], [10, 0, 6]],
        [[-5, -2], [-3, -10], [-1, -4]],
        [[1, 1, 1], [1, 1], [1]],
        [[100, 50], [75], [25, 125, -200]],
    ]
    for i, m in enumerate(casos, 1):
        print(f"Caso {i}: mínimo = {minimo_matriz(m)}")
    # Caso especial: matriz vacía
    try:
        minimo_matriz([])
    except ValueError as e:
        print("Esperado matriz vacía ->", e)
