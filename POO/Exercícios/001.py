# Métodos de instância

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        if valor <= 0:
            print("VALOR INDISPONÍVEL PARA DEPÓSITO")
        else:
            print("DEPÓSITO EFETUADO COM SUCESSO")
            self.saldo += valor

    def sacar(self,valor):
        if valor > self.saldo:
            print("SALDO INDISPONÍVEL")
        elif valor <= 0:
            print("VALOR INDISPONÍVEL PARA SAQUE")
        else:
            print("SAQUE EFETUADO COM SUCESSO")
            self.saldo -= valor

    def mostrar_saldo(self):
        print(f'''
            ---- SALDO --- 
            TITULAR: {self.titular}
            SALDO: {self.saldo}
        ''')
#-----------------------------------------------------------------------------------------

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self,percentual):
        if percentual <= 0:
            print("PERCENTUAL INVÁLIDO PARA AUMENTO")
        else:
            self.salario = self.salario + self.salario * (percentual / 100)
            print("AUMENTO EFETUADO COM SUCESSO")

    def promover(self,novo_cargo, aumento):
        if self.cargo == novo_cargo:
            print("CARGO JÁ OCUPADO")
        else:
            self.cargo = novo_cargo
            self.salario = self.salario + self.salario * (aumento / 100)
            print(f"SEU NOVO CARGO: {novo_cargo} | COM AUMENTO DE: {aumento}")

    def mostrar_informacoes(self):
        print(f'''
            ---- FUNCIONÁRIO ----
            Nome: {self.nome}
            Cargo: {self.cargo}
            Salário: {self.salario}
        ''')
#-----------------------------------------------------------------------------------------

# Métodos de classe

class Produto:
    produtos = 0
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.produtos += 1

    @classmethod
    def total_produtos(cls):
        print(f'TOTAL DE PRODUTOS CADASTRADOS: {cls.produtos}')
#-----------------------------------------------------------------------------------------

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    @classmethod
    def criar_menor(cls, name, email):
        return cls(name, email, 17)

#-----------------------------------------------------------------------------------------

# Métodos estáticos

class Validador:
    def __init__(self):
        pass

    @staticmethod
    def validar_cpf(cpf):
        return len(cpf) == 11 and cpf.isdigit()
#-----------------------------------------------------------------------------------------

class Temperatura:
    @staticmethod
    def para_fahrenheit(temperatura):
        temperatura = (temperatura * 1.8) + 32
        print(f'Essa temperatura em Fahrenheit fica: {temperatura:.2f} F°')

    @staticmethod
    def para_celsius(temperatura):
        temperatura = (temperatura - 32) / 1.8
        print(f'Essa temperatura em Celsius fica: {temperatura:.2f} C°')
#-----------------------------------------------------------------------------------------

class Conta:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial 

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = novo_saldo
#-----------------------------------------------------------------------------------------

class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O SALDO NÃO PODE SER NEGATIVO")
        elif novo_preco == 0:
            print("O PREÇO DEVE SER DIFERENTE DE ZERO")
        else:
            if hasattr(self, "_preco"):
                print(f"Preço Anterior: {self._preco}")
            else:
                print("Cadrastrando novo preço...")
            self._preco = novo_preco
            print(f'Novo Preço: {self._preco}')

produto = Product("Teclado", 150)

print(produto.preco)
produto.preco = 180
print(produto.preco )      
    