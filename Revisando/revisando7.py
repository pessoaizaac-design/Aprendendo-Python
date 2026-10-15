# Revisando Python avançado para Intermediário geral!

from itertools import *
from functools import *
from dataclasses import *

print("Desafio 1")
precos = [10, 25, 40, 80, 100]

aumento = list(map(lambda x: x + (x * 0.15), precos))
print(aumento)
print()

print("Desafio 2")
idades = [12, 18, 25, 16, 32, 17, 41, 15]

maioridade = list(filter(lambda x: x >= 18, idades))
print(maioridade)
print()

print("Desafio 3")
notas = [7, 8, 6, 9, 10]

maior_nota = reduce(lambda x, y: x if x >= y else y ,notas)
print(maior_nota)
print()

print("Desafio 4")
@singledispatch
def exibir_dado():
    pass

@exibir_dado.register
def _(dado: int):
    print(f"FUNÇÃO INT CHAMADA: {dado * 2}")

@exibir_dado.register
def _(dado: float):
    print(f'FUNÇÃO FLOAT CHAMADA: {dado:.2f}')

@exibir_dado.register
def _(dado: str):
    print(f'FUNÇÃO STR CHAMADA: {dado.upper()}')

exibir_dado('Python é Bom')
print()

print("Desafio 5")
def calcular_preco(preco, desconto):
    return preco - (preco * desconto / 100)

preco_promocional = partial(calcular_preco, desconto= 20)

print(preco_promocional(1020))
print(preco_promocional(2034))
print(preco_promocional(1988))
print()

print("Desafio 6")
nomes = {"Ana", "Higor", "Carlos", "Beatriz"}

extensao = {nome: len(nome) for nome in nomes}
print(extensao)
print()

print("Desafio 7")
numeros = [3, 8, 12, 15, 20, 23, 30, 35, 40]

order_list = [number * 2 for number in numeros if number % 5 == 0]
print(order_list)
print()

print("Desafio 8")
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            print("SÓ PODE EXISTIR PREÇO MAIOR QUE ZERO")
            self._preco = 0.0
        else:
            self._preco = valor
            print("PREÇO ALTERADO COM SUCESSO")
print()

print("Desafio 9")
class Validador:
    def __init__(self):
        pass

    @staticmethod
    def validar_email(email):
        if "@" in email and email.endswith(".com"):
            print(f"SEU E-MAILFOI VALIDADO COM SUCESSO! --> {email}")
        else:
            print(f"SEU E-MAIL NÃO FOI VALIDADO --> {email}")    

Validador.validar_email("pessoaizaac@gmail.")
print()

print("Desafio 10")
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    @classmethod
    def livro_atual(cls, titulo, autor):
        return cls(titulo, autor, 2026)
print()

print("Desafio 11")
@dataclass
class Filme:
    titulo: str
    diretor: str
    ano: int
    nota: float

filme1 = Filme("Interestelar", "Christopher Nolan", 2014, 8.6)
filme2 = Filme("A Origem", "Christopher Nolan", 2010, 8.8)
filme3 = Filme("O Último Retrato", "Stanley Tucci", 2017, 6.3)

lista_filmes = [filme1, filme2, filme3]

print("--- FILMES COM NOTA IGUAL OU SUPERIO A 8 ---")
for filme in lista_filmes:
    if filme.nota >= 8:
         print(f"Filme: {filme.titulo} | Diretor: {filme.diretor} | Nota: {filme.nota}")