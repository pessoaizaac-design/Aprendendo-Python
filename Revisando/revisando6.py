# Revisando Python avançado para Intermediário geral!

from itertools import *
from functools import *
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

print("Desafio 1")
turnos = ['Manhâ', 'Tarde', 'Noite']
c = 0

for turno in cycle(turnos):
    if c < 12:
        print(turno)
        c += 1
    else:
        break    
print()

print("Desafio 2")
repetidor = list(repeat(7,8))

print(sum(repetidor))
print()

print("Desafio 3")
jogadores = ["Neymar", "Vini Jr.", "Rodrygo", "Raphinha", "Endrick"]

duplas = list(combinations(jogadores, 2))
print(duplas)
print()

print("Desafio 4")
linguagens = ["Python", "Java", "JavaScript"]
niveis = ["Iniciante", "Intermediário", "Avançado"]

combinacoes = list(product(linguagens, niveis))
print(combinacoes)
print()

print("Desafio 5")
aprovados = ["Ana", "Carlos"]
reprovados = ["Bruno", "Pedro"]
recuperacao = ["Julia", "Marcos"]

alunos = list(chain(aprovados, reprovados, recuperacao))
print(alunos)
print()

print("Desafio 6")
produtos = ["Teclado", "Mouse", "Monitor", "Headset", "Webcam"]
disponiveis = [True, False, True, True, False]

produtos_disponiveis = list(compress(produtos, disponiveis))
print(produtos_disponiveis)
print()

print("Desafio 7")
letras = ["A", "B", "C", "D"]

permutacoes = list(permutations(letras, 3))
print(permutacoes)
print()

print("Desafio 8")
class Pix:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def pagar(self, valor):
        if valor <= 0:
            print("SÓ VALORES ACIMA DE ZERO!")
        elif valor > self.saldo:
            print("VALOR INDISPONÍVEL NA CONTA!")
        else:
            self.saldo = self.saldo - valor
            print(f"PIX EFETUADO COM SUCESSO! SEU SALDO ATUAL AGORA É: {self.saldo}")

class Cartao:
    def __init__(self, credito_disponivel):
        self.credito = credito_disponivel

    def pagar(self, valor):
        if valor <= 0:
            print("SÓ VALORES ACIMA DE ZERO!")
        elif valor > self.credito:
            print("VALOR INDISPONÍVEL NO CARTÃO!")
        else:
            self.credito = self.credito - valor
            print(f"PAGAMENTO EFETUADO, SEU CRÉDITO AGORA É DE: {self.credito}")
print()

print("Desafio 9")
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f'A ÁREA DESSE RETÂNGULO É IGUAL A: {area}')

class Circulo(FormaGeometrica):
    def __init__(self, raio):
            self.raio = raio

    def calcular_area(self):
        area = 3.14 * (self.raio ** 2)
        print(f'A ÁREA DESSE CÍRCULO É IGUAL A: {area}')
print()

print("Desafio 10")
class Cofre:
    def __init__(self, titular,valor):
        self._titular = titular
        self._valor = valor

    def adicionar_dinheiro(self, quantia):
        if quantia <= 0:
            print("SÓ PODE DEPOSITAR UMA QUANTIA MAIOR QUE ZERO")
        else:
            self._valor += quantia
            print("DEPOSITO EFETUADO COM SUCESSO!")

    def retirar_dinheiro(self,quantia):
        if quantia <= 0:
            print("SÓ PODE SACAR UMA QUANTIA MAIOR OU IGUAL A ZERO")
        elif quantia > self._valor:
            print("SALDO INDISPONÍVEL PARA SAQUE!")
        else:
            self._valor -= quantia
            print("SAQUE EFETUADO COM SUCESSO!")

    def conferir_saldo(self):
        print(f'''
    ----- SEU COFRE ---
    [TITULAR] => {self._titular}
    [SALDO] => {self._valor}
''')
print()

print("Desafio 11")
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def consultar_salario(self, taxa_adicional):
        self.salario = self.salario + (self.salario * (taxa_adicional/100))
        print(f'''
        --- SEU SALÁRIO ---
        [NOME] => {self.nome}
        [SALÁRIO] => {self.salario}
        [CARGO] => GERENTE
''')

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def consultar_salario(self, linguagem):
        print(f'''
        --- SEU SALÁRIO ---
        [NOME] => {self.nome}
        [SALÁRIO] => {self.salario}
        [LINGUAGEM] => {linguagem}
''')
print()