import random


def generador_de_personas():
    personas = []

    for identificador in range(1, 11):
        edad = random.randint(1, 100)
        personas.append({"id": identificador, "edad": edad})

    return personas


def ordenar_personas_de_mayor_a_menor_edad(personas):
    personas_ordenadas = sorted(
        personas, key=lambda ordenar_por: ordenar_por["edad"], reverse=True
        )

    print(personas_ordenadas[0]["id"])
    print(personas_ordenadas[-1]["id"])

    return personas_ordenadas


if __name__ == "__main__":
    personas = generador_de_personas()
    ordenar_personas_de_mayor_a_menor_edad(personas)
