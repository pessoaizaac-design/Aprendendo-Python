class Pessoa:
    def __init__(self, nome = "", idade = ""):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1