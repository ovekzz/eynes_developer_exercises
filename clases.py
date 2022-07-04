import math


class Circulo():
    """ test
    >>> cuadrado = Circulo(0)
    Traceback (most recent call last):
        ...
    Exception: No es posible que el radio sea igual o menor a 0
    >>> circulo = Circulo(12)
    >>> circulo.radio
    12
    >>> circulo.modificar_radio(5)
    >>> circulo.radio
    5
    >>> circulo.modificar_radio(0)
    Traceback (most recent call last):
        ...
    Exception: No es posible que el radio sea igual o menor a 0
    >>> circulo.radio
    5
    >>> otro_circulo = circulo * 5
    >>> otro_circulo.radio
    25
    >>> print(circulo)
    El radio del circulo es: 5
    El area del circulo es: 78.53981633974483
    El perimetro del circulo es: 31.41592653589793
    """

    def __init__(self, radio):
        self.radio = radio

        if self.radio <= 0:
            raise Exception(
                "No es posible que el radio sea igual o menor a 0"
                )

    def area(self):
        return math.pi*self.radio**2

    def perimetro(self):
        return 2*math.pi*self.radio

    def modificar_radio(self, radio):
        if radio <= 0:
            raise Exception(
                "No es posible que el radio sea igual o menor a 0 "
                )
        else:
            self.radio = radio

    def __mul__(self, n):
        if n <= 0:
            raise ValueError(
                "el radio debe ser multiplicado por un numero mayor a 0"
            )
        return Circulo(self.radio * n)

    def __str__(self):
        return f"El radio del circulo es: {self.radio} \n"\
               f"El area del circulo es: {self.area()} \n"\
               f"El perimetro del circulo es: {self.perimetro()}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
