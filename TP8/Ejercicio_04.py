def fichas_encajan(ficha1: tuple, ficha2: tuple) -> bool:
	"""
	Indica si dos fichas de domino encajan usando conjuntos.
	
	Pre: ficha1 y ficha2 son tuplas (a, b) con numeros.
	
	Post: retorna True si tienen algun numero en comun; caso contrario False.
	"""
	assert isinstance(ficha1, (tuple, list)), "ficha1 debe ser una tupla o lista"
	assert isinstance(ficha2, (tuple, list)), "ficha2 debe ser una tupla o lista"

	# Validacion basica de estructura
	if not (
		isinstance(ficha1, (tuple, list))
		and isinstance(ficha2, (tuple, list))
		and len(ficha1) == 2
		and len(ficha2) == 2
	):
		return False

	# Convertimos a conjuntos y chequeamos interseccion
	set1 = set(ficha1)
	set2 = set(ficha2)
	
	return len(set1 & set2) > 0 # Hay interseccion (Si > 0, True) -> encajan 


def main():
	# Pedimos las dos fichas y mostramos si encajan
	try:
		entrada1 = input("Ingresá ficha 1 (dos enteros separados por espacio): ").strip()
		a, b = map(int, entrada1.split())
		entrada2 = input("Ingresá ficha 2 (dos enteros separados por espacio): ").strip()
		c, d = map(int, entrada2.split())
	except Exception:
		print("Entrada inválida. Ejemplo: '3 4' y luego '5 4'.")
		return

	resultado = fichas_encajan((a, b), (c, d))
	
	if resultado == True:
		print("Las fichas encajan.")
	else:
		print("Las fichas no encajan.")


if __name__ == "__main__":
	main()

