
class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
        
    def depositar(self, valor):
        if valor < 0:
            print(f'O VALOR DE R$ {valor} É INVÁLIDO PARA DEPOSITAR')
        else:
            print(f'O VALOR DE R${valor} FOI DEPOSITADO NA SUA CONTA!')
            self._saldo += valor
            
    def sacar(self, valor):
        if valor > self._saldo:
            print(f'SAQUE DE R$ {valor} FOI NEGADO POR SER MAIOR QUE SEU SALDO!')
        else:
            print(f'O VALOR DE R$ {valor} FOI SACADO COM SUCESSO!')
            self._saldo -= valor
            
    def analisar_saldo(self):
        print(f'O SEU SALDO ATUAL É DE R$ {self._saldo}')
            
b1 = ContaBancaria(2000)
b1.depositar(259)
b1.sacar(2000)
b1.analisar_saldo()
