from abc import ABC, abstractmethod
import math

# Encapsulamento

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Deposite um valor maior que 0")
        else:
            print("Depósito efetuado")
            self.__saldo += valor

    def sacar(self,valor):
        if valor <= 0:
            print("Saque um valor maior que 0")
        elif valor > self.__saldo:
            print("Saque um saldo disponível")
        else:
            print("Saque efetuado com sucesso")
            self.__saldo -= valor

    def consultar_saldo(self):
        print('---- Saldo ----')
        print(f'Titular: {self.titular}')
        print(f'Saldo: {self.__saldo}')

#-----------------------------------------------------------------------------------------

class Cadastro:
    def __init__(self,nome,email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def alterar_senha(self,senha_atual, nova_senha):
        if senha_atual == self.__senha:
            self.__senha = nova_senha
        else:
            print("Senha atual incorreta")

    def consultar(self,senha):
        if senha == self.__senha:
            print("Está é sua senha atual")
        else:
            print('senha incorreta!')

    def mostrar_conta(self):
        print(f'''
            --- Conta ---
            Nome: {self.__nome}
            E-mail: {self.__email}
            Senha: {self.__senha}
        ''')

#-----------------------------------------------------------------------------------------

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioPJ(Funcionario):
    def calcular_salario(self):
        print("Você recebe um salário fixo de 15.000 mais ganhos!")

#-----------------------------------------------------------------------------------------
        
class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

#-----------------------------------------------------------------------------------------

class Retangulo(Forma):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)


class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio**2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + hipotenusa
