class Conta_Bancaria:
    '''
    Cria uma conta que permiti fazer saques e depósitos
    '''
    def __init__(self, id, nome, saldo='0'):
        self.id = id
        self.titular = nome
        self.dinheiro = saldo
        print(f'Conta {self.id} criada com sucesso, seu saldo atual é de R${self.dinheiro}')
    
    def __str__(self):
         return f'O titular da conta {self.id} se chama {self.titular}, ele possui R${self.dinheiro}'
    
    def depositar(self, valor=0):
        self.dinheiro += valor
        print(f'Depósito de R$ {valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor=0):
        if valor > self.dinheiro:
            print(f'Saque de {valor:,.2f} negado na conta {self.id}')
        else:   
         self.dinheiro -= valor
         print(f'Saque de R$ {valor:,.2f} autorizado na conta {self.id}')

c1 = Conta_Bancaria(112, 'Gustavo', 500)
print(c1)


