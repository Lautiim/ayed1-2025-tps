import random

def generar_pesos_naranjas(cantidad: int) -> list[int]:
    """Funcion para generar una lista de pesos aleatorios para las naranjas cosechadas.
    
    Pre: Recibe un entero positivo que representa la cantidad de naranjas cosechadas.

    Post: Devuelve una lista de enteros positivos que representan los pesos de las naranjas en gramos.
    """
    # Validamos que la cantidad sea positiva
    if cantidad < 0:
        raise ValueError("La cantidad de naranjas debe ser un entero positivo.")

    return [random.randint(150, 350) for _ in range(cantidad)]

def clasificar_naranjas(pesos: list[int]) -> tuple[list[int], list[int]]: # Es una tupla ya que son dos listas :3
    """Clasifica las naranjas para jugo o para cajon de reparto.
    
    Pre: Recibe una lista de enteros positivos que representan los pesos de las naranjas en gramos.

    Post: Devuelve dos listas de enteros:
        - La primera lista contiene los pesos de las naranjas aptas para cajon (200g a 300g).
        - La segunda lista contiene los pesos de las naranjas aptas para jugo (menos de 200g o más de 300g).    
    """
    # Validamos que los pesos sean positivos
    if any(peso < 0 for peso in pesos):
        raise ValueError("Los pesos de las naranjas no pueden ser negativos.")

    para_cajon = [naranja for naranja in pesos if 200 <= naranja <= 300] # Apilamos las naranjas aptas para cajon
    para_jugo = [naranja for naranja in pesos if naranja < 200 or naranja > 300] # Apilamos las naranjas aptas para jugo
    
    return para_cajon, para_jugo

def calcular_cajones(naranjas_para_cajon: list[int], capacidad_cajon: int = 100) -> list[int, int]:
    """Calcula la cantidad de cajones completos y sobrantes.
    
    Pre: Recibe una lista de enteros positivos que representan los pesos de las naranjas aptas para cajon y un entero positivo que representa la capacidad del cajon (por defecto 100).

    Post: Devuelve una lista con dos enteros:
        - El primer entero representa la cantidad de cajones completos.
        - El segundo entero representa la cantidad de naranjas sobrantes que no alcanzan para completar otro cajon.
    """
    # Validamos que la capacidad del cajon sea positiva
    if capacidad_cajon <= 0:
        raise ValueError("La capacidad del cajon debe ser un entero positivo.")
    # Validamos que las naranjas sean positivas
    if any(peso < 0 for peso in naranjas_para_cajon):
        raise ValueError("Los pesos de las naranjas no pueden ser negativos.")

    cajones_llenos = len(naranjas_para_cajon) // capacidad_cajon # Se calcula la cantidad de cajones completos
    sobrantes = len(naranjas_para_cajon) % capacidad_cajon # Se calcula la cantidad de naranjas sobrantes

    return [cajones_llenos, sobrantes]

def calcular_camiones(naranjas_para_cajon: list[int], capacidad_cajon: int = 100, max_carga_kg: int = 500, min_ocupacion: float = 0.8):
    """Calcula la cantidad de camiones necesarios segun la carga y ocupación mínima.

    Pre: Recibe los siguientes valores:
        - Una lista de enteros positivos que representan los pesos de las naranjas aptas para cajon.
        - Un entero positivo que representa la capacidad del cajon (por defecto 100).
        - Un entero positivo que representa la carga máxima del camión en kg (por defecto 500).
        - Un float entre 0 y 1 que representa la ocupación mínima del camión (por defecto 0.8).
    
    Post: Devuelve un entero positivo que representa la cantidad de camiones necesarios.
    """
    # Validamos que la capacidad del cajon sea positiva
    if capacidad_cajon <= 0:
        raise ValueError("La capacidad del cajon debe ser un entero positivo.")
    # Validamos que la carga máxima del camión sea positiva
    if max_carga_kg <= 0:
        raise ValueError("La carga máxima del camion debe ser un entero positivo.")
    # Validamos que la ocupación mínima esté entre 0 y 1
    if not (0 < min_ocupacion <= 1):
        raise ValueError("La ocupacion mínima debe estar entre 0 y 1.")
    # Validamos que las naranjas sean positivas
    if any(peso < 0 for peso in naranjas_para_cajon):
        raise ValueError("Los pesos de las naranjas no pueden ser negativos.")

    camiones = 0
    i = 0
    naranjas = len(naranjas_para_cajon) # Cantidad total de naranjas para cajon

    while i < naranjas: # Repetimos mientras haya naranjas o hasta completar un cajon
        # Tomamos un grupo de naranjas hasta llenar el cajon (de a lo sumo capacidad_cajon)
        grupo_de_naranjas = naranjas_para_cajon[i:i+capacidad_cajon] 
        # Calculamos el peso total del grupo de naranjas en kg
        peso_total = sum(grupo_de_naranjas) / 1000  # en kg

        # Si el peso total alcanza la ocupacion minima del camion
        if peso_total >= max_carga_kg * min_ocupacion / 100:
            camiones += 1 # Sumamos un camion
        elif peso_total >= max_carga_kg * min_ocupacion: # Si el peso total alcanza la ocupacion minima del camion
            camiones += 1 # Sumamos un camion
        
        # Avanzamos al siguiente grupo de naranjas
        i += capacidad_cajon

    # Una vez que se analizaron todas las naranjas, devolvemos la cantidad de camiones necesarios
    return camiones

def main():
    """ Funcion principal del programa """
    print("--------- Bienvenido ---------")
    cant_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    naranjas = generar_pesos_naranjas(cant_naranjas)

    # Mostrar pesos generados
    for i, peso in enumerate(naranjas, 1):
        print(f"Naranja {i}: {peso} gramos")

    para_cajon, para_jugo = clasificar_naranjas(naranjas)
    cajones_llenos, sobrantes = calcular_cajones(para_cajon)
    camiones = calcular_camiones(para_cajon)

    print(f"\nNaranjas para jugo: {len(para_jugo)}")
    print(f"Cajones completos llenos: {cajones_llenos}")
    print(f"Naranjas sobrantes para próximo reparto: {sobrantes}")
    print(f"Camiones necesarios (mínimo 80% de ocupación): {camiones}")

if __name__ == "__main__":
    main()