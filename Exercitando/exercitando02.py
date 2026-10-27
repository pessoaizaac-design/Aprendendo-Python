# Exercitando POO

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

print("Exercício 01")
class Email:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data

    def enviar(self, mensagem):
        print(f'{mensagem} para {self.nome} no dia {self.data} por E-mail!')

class Sms(Email):
    def __init__(self, nome, data):
        super().__init__(nome, data)

    def enviar(self, mensagem):
        print(f'{mensagem} enviada para {self.nome} no dia {self.data} por SMS!')

def executar(mensagem, funcao):
    funcao.enviar(mensagem)

cliente_email = Email("Higor", 18)
cliente_sms = Sms("Higor", 22)

executar("Seu boleto vence hoje", cliente_email)
executar("Código de acesso: 9942", cliente_sms)

print()

print("Exercício 02")
class Pagamento(ABC):
    def __init__(self, nome, destinatario):
        self.destinatario = destinatario
        self.nome = nome.upper()

    @abstractmethod
    def processar(self, valor):
        pass

class PagamentoPix(Pagamento):
    def __init__(self, nome, destinatario):
        super().__init__(nome, destinatario)

    def processar(self, valor):
        print(f'{self.nome} --> Pagando {valor} para {self.destinatario} em Pix!')

class PagamentoCartao(Pagamento):
    def __init__(self, nome, destinatario):
        super().__init__(nome, destinatario)

    def processar(self, valor):
        print(f'{self.nome} --> Pagando {valor} para {self.destinatario} em Cartão!')

def realizar_transacao(forma_pagamento, valor_total):
    forma_pagamento.processar(valor_total)

cliente_pix = PagamentoPix("Higor", "Loja de Informática")
cliente_cartao = PagamentoCartao("Ana", "Supermercado")

realizar_transacao(cliente_pix, 250.00)
realizar_transacao(cliente_cartao, 120.50)

print()

print("Exercício 03")

class Estoque:
    def __init__(self, produto, valor, quantidade):
        self.produto = produto
        self.valor = valor
        self._quantidade = quantidade

    def adicionar_estoque(self, quantia):
        if quantia <=0:
            print("Não é possível adicionar uma quantia negativa ou igual a zero no estoque!")
        else:
            self._quantidade += quantia
            print("Quantia de unidades adicionada com sucesso ao estoque!")

    def remover_estoque(self, quantia):
        if quantia <=0:
            print("Não é possível remover uma quantia negativa ou igual a zero no estoque!")
        elif quantia > self._quantidade:
            print("Não é possível remover uma quantia maior que a do estoque!")
        else:
            self._quantidade -= quantia
            print("Quantia de unidades removidas com sucesso do estoque!")

    def consultar(self):
        print(f'''
        ----- ESTOQUE -----
        [PRODUTO] => {self.produto}
        [VALOR] => {self.valor}
        [ESTOQUE] => {self._quantidade}
''')

estocado = Estoque("Teclado", 199.99, 40)

estocado.adicionar_estoque(10)
estocado.adicionar_estoque(-10)
print()
estocado.remover_estoque(1000)
estocado.remover_estoque(15)

estocado.consultar()

print()

print("Exercício 04")
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Admin(Usuario):
    def __init__(self, nome, email, nivel_acesso):
        super().__init__(nome, email)
        self.nivel = nivel_acesso

    def mostrar(self):
        print(f'{self.nome} com e-mail: {self.email} é um ADMIN com {self.nivel} de acesso!')

class Cliente(Usuario):
    def __init__(self, nome, email, pontos):
        super().__init__(nome, email)
        self.pontos = pontos

    def mostrar(self):
        print(f'{self.nome} com e-mail: {self.email} é um CLIENTE com {self.pontos} de pontos!')

print()

print("Exercício 05")
class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor <= 0:
            print("Dê um valor positivo para a nova largura!")
        else:
            self._largura = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            print("Dê um valor positivo para a nova altura!")
        else:
            self._altura = valor 

    @property
    def area(self):
        return self._largura * self._altura

meu_retangulo = Retangulo(5, 4)
print(f"Área inicial: {meu_retangulo.area}") 

meu_retangulo.largura = 10
print(f"Nova Área: {meu_retangulo.area}")

meu_retangulo.altura = -2
    
print()

print("Exercício 06")
class ValidarNumero:
    def __init__(self):
        pass

    @staticmethod
    def eh_positivo(numero):
        if numero >= 0:
            return True
        else:
            return False

print()

print("Exercício 07")
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    @classmethod
    def a_partir_de_texto(cls, texto):
        nome, salario_texto = texto.split(",")
        salario = float(salario_texto)
        return cls(nome, salario)

    def exibir(self):
        print(f"Funcionário: {self.nome} | Salário: R$ {self.salario:.2f}")

dados = "Carlos,3500"
novo_funcionario = Funcionario.a_partir_de_texto(dados)
novo_funcionario.exibir()

print()

print("Exercício 08")

@dataclass
class Tarefa:
    descricao: str
    prioridade: str
    concluida: bool = False

tarefas = [
    Tarefa("Estudar Python", "Alta"),
    Tarefa("Lavar a louça", "Média", concluida=True),
    Tarefa("Fazer compras", "Baixa"),
    Tarefa("Academia", "Alta", concluida=True)
]

print("\n--- TAREFAS NÃO CONCLUÍDAS ---")
for tarefa in tarefas:
    if not tarefa.concluida:
        print(f'[{tarefa.prioridade}] {tarefa.descricao}')