class Teste:
    def __init__(self, n='', s='indefinido', i=''):
        self.nome = n
        self.sexo = s
        self.idade = i

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f'Seu nome é {self.nome}, você é do sexo {self.sexo} e possui {self.idade} anos de idade'
  
  
teste1 = Teste('Higor', 'Masculino', 18)
print(teste1)

teste2 = Teste('Mauro', 'Masculino', 70)
print(teste2)

