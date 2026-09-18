# Herança

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

class Secretaria(Pessoa):
    def __init__(self, id_secretaria, nome, idade, altura):
        super().__init__(nome, idade, altura)
        self.id_secretaria = id_secretaria

class Vendendor(Pessoa):
    pass

