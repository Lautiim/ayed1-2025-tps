def son_ortogonales(vector1: tuple, vector2: tuple, tol: float = 1e-9) -> bool:
	"""
	Verifica ortogonalidad usando el producto escalar.
	
	Pre: vector1 y vector2 son iterables de longitud 2 con valores numericos; tol >= 0.
	
	Post: True si |x1*x2 + y1*y2| <= tol; caso contrario False.
	"""
	# Chequeo basico de estructura
	if not (
		isinstance(vector1, (tuple, list))
		and isinstance(vector2, (tuple, list))
		and len(vector1) == 2
		and len(vector2) == 2
	):
		return False

	# Convertimos a float; si no se puede, es invalido
	try:
		x1, y1 = float(vector1[0]), float(vector1[1])
		x2, y2 = float(vector2[0]), float(vector2[1])
	except (ValueError, TypeError):
		return False

	# Producto de escalar y comparacion con tolerancia
	dot = x1 * x2 + y1 * y2
	return abs(dot) <= max(0.0, float(tol))


def main():
	# Pedimos los dos vectores y mostramos si son ortogonales
	try:
		a_str = input("Ingresá vector A (x y): ").strip()
		ax, ay = map(float, a_str.split())
		b_str = input("Ingresá vector B (x y): ").strip()
		bx, by = map(float, b_str.split())
	except Exception:
		print("Entrada inválida. Ejemplo: '2 3' y luego '-3 2'.")
		return

	resultado = son_ortogonales((ax, ay), (bx, by))
	
	if resultado:
		print("Los vectores son ortogonales.")
	else:
		print("Los vectores no son ortogonales.")


if __name__ == "__main__":
	main()

