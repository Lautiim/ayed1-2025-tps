"""
Este es un docstring de módulo
que debe ser eliminado.
"""

# Este es un comentario simple que debe eliminarse


def funcion_ejemplo(x, y):
    """
    Esta es una función de ejemplo.
    Este docstring debe ser eliminado.
    """
    resultado = x + y  # Este comentario también debe eliminarse
    return resultado


class MiClase:
    """
    Este es un docstring de clase
    con comillas simples triples.
    """

    def __init__(self):
        self.valor = 10  # Comentario en init
        self.texto = "Este es un # dentro de comillas, NO es comentario"
        self.otro = "También # dentro de comillas simples"

    def metodo(self):
        # Comentario al inicio de método
        x = 5
        return x


# Comentario al final del archivo
print("Hola mundo")  # Comentario al final de la línea
