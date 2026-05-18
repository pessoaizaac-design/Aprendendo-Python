class Teste:
    '''
    Essa Class cria uma def com os indicadore: nome, sexo e idade. 

    Existe outra def chamada Aniversario, que quando chamada adciona 1 ano a mais de idade ou quanto você colocar dentro dos parêntes.

    E por último a def mensagem que dá return no print dos valores que você indica para os itens constados:
    variável = Class(n, s, i)
    '''
    def __init__(self, n='', s='indefinido', i=''):
        self.nome = n
        self.sexo = s
        self.idade = i

    def aniversario(self):
        self.idade += 1

    def __str__(self): #Deixa o code mais limpo, so dando um print no nome dele
        return f'Seu nome é {self.nome}, você é do sexo {self.sexo} e possui {self.idade} anos de idade'
    

    def __getstate__(self):
        return f'Nome = {self.nome}, sexo = {self.sexo} e idade = {self.idade}'


teste1 = Teste('Higor', 'Masculino', 18)
print(teste1)

print(teste1.__getstate__()) #Igual o __dict__ só que personalisável
print(teste1.__dict__) #Mostra as informações como se fosse uma lista

print(Teste.__doc__)#Mundo 2, mostras as informações que vc detalha nas 3 áspas