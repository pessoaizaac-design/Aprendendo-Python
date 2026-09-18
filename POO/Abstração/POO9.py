# Abstração

from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self,nome):
        self.nome = nome

    @abstractmethod
    def jogar(self):
        pass

class Goleiro(Jogador):
    def jogar(self):
        print(f"{self.nome} está defendo o gol!")

class Linha(Jogador):
    def jogar(self):
        print(f"{self.nome} está jogando na linha!")

j1 = Goleiro("Alisson")
j2 = Linha("Neymar")

j1.jogar()
j2.jogar()