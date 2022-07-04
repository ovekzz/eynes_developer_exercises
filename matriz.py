import random

matriz = []

for i in range(5):
    fila_de_matriz = [random.randint(0, 2) for numero in range(5)]
    matriz.append(fila_de_matriz)

contador_de_filas = 0

for fila in matriz:
    contador_de_filas += 1

    if fila[0] == fila[1] == fila[2] == fila[3]:
        print(f"fila {contador_de_filas}, columna 1 a 4")
    elif fila[1] == fila[2] == fila[3] == fila[4]:
        print(f"fila {contador_de_filas}, columna 2 a 5")

matriz_invertida = []

for columna in range(5):
    fila_matriz_invertida = [matriz[fila][columna] for fila in range(5)]
    matriz_invertida.append(fila_matriz_invertida)

contador_de_columnas = 0

for columna in matriz_invertida:
    contador_de_columnas += 1
    if columna[0] == columna[1] == columna[2] == columna[3]:
        print(f"columna {contador_de_columnas}, fila 1 a 4")

    elif columna[1] == columna[2] == columna[3] == columna[4]:
        print(f"columna {contador_de_columnas}, fila 2 a 5")
