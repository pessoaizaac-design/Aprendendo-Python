'''
 Funções - def em Python (parte 2)
'''
def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor encontrado')
    
def dividir(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

div = dividir(8, 4)
if div:
    print(dividir)
else:
    print('Conta inválida')