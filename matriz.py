import random

matriz = []

for i in range(5):
<<<<<<< Updated upstream
    fila_de_matriz = [random.randint(0, 2) for i in range(5)]
=======
    fila_de_matriz = [random.randint(0, 1) for numero in range(5)]
>>>>>>> Stashed changes
    matriz.append(fila_de_matriz)

contador_de_filas = 0

for fila in matriz:
    contador_de_filas += 1

    if fila[0] == fila[1] == fila[2] == fila[3]:
        print(f"hay 4 numeros consecutivos en la fila {contador_de_filas}, de la columna 1 a la 4")
    if fila[1] == fila[2] == fila[3] == fila[4]:
        print(f"hay 4 numeros consecutivos en la fila {contador_de_filas}, de la columna 2 a la 5")

contador_de_columnas = 0

for columnas in range(5):
    contador_de_columnas += 1

    if matriz[0][columnas] == matriz[1][columnas] == matriz[2][columnas] == matriz[3][columnas]:
        print(f"hay 4 numeros consecutivos en la columna {contador_de_columnas}, de la fila 1 a la 4")
    if matriz[1][columnas] == matriz[2][columnas] == matriz[3][columnas] == matriz[4][columnas]:
        print(f"hay 4 numeros consecutivos en la columna {contador_de_columnas}, de la fila 2 a la 5")
