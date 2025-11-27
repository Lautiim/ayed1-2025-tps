from typing import List  # Typing para poder usar List[int]


def indice_minimo(lista: List[int], inicio: int) -> int:
    """Devuelve el índice del menor elemento en lista[inicio:].

    Implementado recursivamente sin usar min()/max().
    """
    fin = len(lista) - 1
    if inicio == fin:
        return inicio
    # Obtener índice mínimo del resto
    idx_restante = indice_minimo(lista, inicio + 1)
    # Comparar el elemento actual con el mínimo del resto
    if lista[inicio] <= lista[idx_restante]:
        return inicio
    return idx_restante


def seleccion_recursiva_inplace(lista: List[int], inicio: int = 0) -> None:
    """Ordena la lista usando selección recursiva."""
    if inicio >= len(lista) - 1:
        return
    idx_min = indice_minimo(lista, inicio)
    if idx_min != inicio:
        lista[inicio], lista[idx_min] = lista[idx_min], lista[inicio]
    seleccion_recursiva_inplace(lista, inicio + 1)


def ordenar_por_seleccion_recursiva(lista: List[int]) -> List[int]:
    """Devuelve una nueva lista ordenada mediante selección recursiva."""
    copia = list(lista)
    seleccion_recursiva_inplace(copia)
    return copia


if __name__ == "__main__":
    pruebas = [
        [],
        [5],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 2, 1, 3, 0, -1, -1],
    ]
    for caso in pruebas:
        print(f"Original: {caso} -> Ordenada: {ordenar_por_seleccion_recursiva(caso)}")
