# Métodos de classe
total_usuarios = 0

class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.idade = idade
        self.email = email

        Usuario.total_usuarios += 1

    @classmethod
    def total_usuarios(cls, dados):
        nome, idade, email = dados.split(',')
        idade = int(idade)
        return cls(nome, idade, email)

#-----------------------------------------------------------------------------------------

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @classmethod
    def from_string(cls, dados):
        nome, preco, estoque = dados.split(',')
        return cls(nome, preco, estoque)

produto_string = "Nootebook, 2500, 100"
novo_produto = Produto.from_string(produto_string)
#print(f'''
    # --- PRODUTO ---
     #[Nome] -> {novo_produto.nome}
     #[Preço] -> {novo_produto.preco}
     #[Estoque] -> {novo_produto.estoque}
#''')

#-----------------------------------------------------------------------------------------

# Métodos estáticos
class Conta:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def verificar_cpf(cpf):
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

#resultado = Temperatura.para_fahrenheit(30)
#resultado2 = Temperatura.para_celsius(30)

#-----------------------------------------------------------------------------------------

class ContaBanco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        if valor < 0:
            print(f'DEPOSITE UM VALOR POSITIVO!')
        else:
            print(f'VALOR DEPOSITADO NO SEU SALDO!')
            self.saldo += valor

    def sacar(self,valor):
        if valor > self.saldo:
            print(f'SALDO INDISPONÍVEL')
        elif valor < 0:
            print(f'SAQUE UM VALOR POSITIVO')
        else:
            self.saldo -= valor

    def consultar_saldo(self):
        print(f'''
            --- SALDO ---
              R$ {self.saldo}
        ''')

minha_conta = ContaBanco("Higor", 1000)
# Teste depósito
#minha_conta.depositar(500)

# Teste saque
#minha_conta.sacar(2000)
#minha_conta.sacar(300)

#Resultado final
#minha_conta.consultar_saldo()

#-----------------------------------------------------------------------------------------

class Compras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco):
        if preco < 0:
            print(f'PREÇO INVÁLIDO!')
        else:
            self.produtos.append((nome, preco))
            print(f'PRODTO ADICIONADO COM SUCESSO!')

    def remover_produto(self,nome):
        for item in self.produtos:
            if item[0] == nome:
                self.produtos.remove[item]
                print(f'ITEM REMOVIDO COM SUCESSO!')
                return
        print('PRODUTO NÃO ENCONTRADO NO CARRINHO')

    def calcular_total(self):
        total = 0
        for k,v in self.produtos:
            print(f'{k} --> R$ {v:.2f}')
            total += v
        print(f'''
            ---- TOTAL ----
              R$ {total:.2f}
        ''')

    def listar_produto(self):
       print("\n--- PRODUTOS NO CARRINHO ---")
       if not self.produtos:
           print("O CARRINHO ESTÁ VAZIO")
       else:
           for k in self.produtos:
               print(f'PRODUTO: {k[0]} | PREÇO R$ {k[1]:.2f}')
