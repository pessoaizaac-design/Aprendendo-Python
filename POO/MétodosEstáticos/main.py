# Métodos estáticos
from random import randint

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_de_nascimento(self):
        print(f'{self.nome} nasceu em {self.ano_atual - self.idade}')

    @classmethod
    def por_ano_de_nascimento(cls, name, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(name,idade)

    @staticmethod
    def gerar_id():
        rand = randint(10000, 19999)
        return rand
