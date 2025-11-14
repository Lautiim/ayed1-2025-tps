def matriz_a(n: int) -> list[list[int]]:
    """
    Genera matriz con diagonal de numeros impares crecientes.

    Pre: n > 0.

    Post: retorna matriz donde diagonal[i] = 2*i+1, resto 0.
    """
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = 2 * i + 1
    return m


def matriz_b(n: int) -> list[list[int]]:
    """
    Genera matriz con anti-diagonal de potencias de 3.

    Pre: n > 0.

    Post: retorna matriz con m[i][n-1-i] = 3**(n-1-i), resto 0.
    """
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][n - 1 - i] = 3 ** (n - 1 - i)
    return m


def matriz_c(n: int) -> list[list[int]]:
    """
    Genera matriz triangular inferior con valores descendentes.

    Pre: n > 0.

    Post: fila i tiene i+1 valores N-i y resto 0.
    """
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        val = n - i
        for j in range(i + 1):
            m[i][j] = val
    return m


def matriz_d(n: int) -> list[list[int]]:
    """
    Genera matriz con filas constantes descendiendo en potencia de 2.

    Pre: n > 0.

    Post: fila i llena con 2**(n-1-i).
    """
    m = []
    for i in range(n):
        val = 2 ** (n - 1 - i)
        m.append([val] * n)
    return m


def matriz_e(n: int) -> list[list[int]]:
    """
    Genera matriz con numeros consecutivos en posiciones de paridad impar.

    Pre: n > 0.

    Post: celdas donde (i+j)%2==1 reciben 1..k; resto 0.
    """
    m = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                m[i][j] = num
                num += 1
    return m


def matriz_f(n: int) -> list[list[int]]:
    """
    Genera matriz con triangulo inferior derecha numerado.

    Pre: n > 0.

    Post: region donde j >= n-1-i se llena con 1..; resto 0.
    """
    m = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for offset in range(i + 1):
            j = n - 1 - offset
            m[i][j] = num
            num += 1
    return m


def matriz_g(n: int) -> list[list[int]]:
    """
    Genera matriz en espiral (sentido horario) con 1..n^2.

    Pre: n > 0.

    Post: retorna matriz espiral.
    """
    m = [[0] * n for _ in range(n)]
    top, left = 0, 0
    bottom, right = n - 1, n - 1
    num = 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            m[top][j] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            m[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                m[bottom][j] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                m[i][left] = num
                num += 1
            left += 1
    return m


def matriz_h(n: int) -> list[list[int]]:
    """
    Genera matriz por anti-diagonales de arriba hacia abajo (top->bottom).

    Pre: n > 0.

    Post: diagonales con suma i+j = s llenas en orden top->bottom, s ascendente.
    Patron ejemplo para n=4:
    1  2  4  7
    3  5  8 11
    6  9 12 14
    10 13 15 16
    """
    m = [[0] * n for _ in range(n)]
    num = 1
    # Primer tramo: diagonales que inician en fila 0 (s = 0..n-1)
    for s in range(n):
        for i in range(s + 1):  # i = fila
            fila = i
            col = s - i
            m[fila][col] = num
            num += 1
    # Segundo tramo: diagonales que inician en ultima columna (s = n .. 2n-2)
    for s in range(n, 2 * n - 1):
        count = 2 * n - 1 - s  # cantidad de elementos en la diagonal
        start_row = s - (n - 1)
        for t in range(count):
            fila = start_row + t
            col = (n - 1) - t
            m[fila][col] = num
            num += 1
    return m


def matriz_i(n: int) -> list[list[int]]:
    """
    Genera matriz por anti-diagonales alternando direccion.

    Pre: n > 0.

    Post: anti-diagonales pares bottom->top, impares top->bottom.
    """
    m = [[0] * n for _ in range(n)]
    num = 1
    for s in range(2 * n - 1):
        r_start = min(s, n - 1)
        r_end = max(0, s - (n - 1))
        if s % 2 == 0:  # par: bottom->top
            r_range = range(r_start, r_end - 1, -1)
        else:  # impar: top->bottom
            r_range = range(r_end, r_start + 1)
        for r in r_range:
            c = s - r
            m[r][c] = num
            num += 1
    return m


def imprimir_matriz(m: list[list[int]], titulo: str):
    """
    Imprime matriz en formato simple.

    Pre: m lista de listas; titulo cadena.

    Post: muestra titulo y contenido sin librerias externas.
    """
    print(f"\nPatron {titulo}:")
    ancho = len(str(len(m) * len(m)))
    for fila in m:
        print(" ".join(f"{v:{ancho}d}" for v in fila))


def main():
    try:
        n = int(input("Ingresá N (tamaño de las matrices): "))
        if n <= 0:
            print("N debe ser positivo.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    imprimir_matriz(matriz_a(n), "a")
    imprimir_matriz(matriz_b(n), "b")
    imprimir_matriz(matriz_c(n), "c")
    imprimir_matriz(matriz_d(n), "d")
    imprimir_matriz(matriz_e(n), "e")
    imprimir_matriz(matriz_f(n), "f")
    imprimir_matriz(matriz_g(n), "g")
    imprimir_matriz(matriz_h(n), "h")
    imprimir_matriz(matriz_i(n), "i")


if __name__ == "__main__":
    main()
