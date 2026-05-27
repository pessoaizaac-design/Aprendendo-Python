from abc import ABC
from abc import abstractclassmethod

class Poligono(ABC):
    def __init__(self, lados=0):
        self.lados =lados

    @abstractclassmethod
    def perimetro(self):
        pass

    @abstractclassmethod
    def area(self):
        pass

class Quadrado(Poligono):

    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    