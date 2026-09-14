# Métodos de classe
class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        print(f'{self.nome} nasceu em {self.ano_atual - self.idade}')

    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        return cls(nome, idade)