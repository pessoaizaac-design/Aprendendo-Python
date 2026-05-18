from rich import print
from rich.traceback import install
install()

class Funcionario:
    def __init__(self, n, s, c):
        self.nome = n
        self.setor = s
        self.cargo = c

    def informacoes(self):
        return f':handshake: Olá me chamo [blue]{self.nome}[/], sou {self.cargo} do setor de {self.setor} da minha empresa '
    
p1 = Funcionario('Higor', 'TI', 'Programador')
print(p1.informacoes())

p2 = Funcionario('Dimitri', 'Saúde', 'Médico')
print(p2.informacoes())