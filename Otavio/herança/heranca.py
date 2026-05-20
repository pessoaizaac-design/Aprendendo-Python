class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self, assunto):
        print(f'O {self.nomeclasse} está falando sobre {assunto}...')

class Cliente(Pessoa):
    def comprar(self, item):
        print(f'{self.nome} está comprando {item}')
  

class Aluno(Pessoa):
    def estudar(self, materia):
        print(f'{self.nome} está estudando {materia}')