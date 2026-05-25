'''
 Funções - def em Python (parte 1)
'''
def saudacao(msg = 'Olá', nome = 'Usuário'):
    return f'{msg} {nome}'
    
variavel = saudacao()
print(variavel)