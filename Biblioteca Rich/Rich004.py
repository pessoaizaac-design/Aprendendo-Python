from rich.traceback import install
install()
'''
Uma forma mais organizada de mostrar o erro, facilitando o entendimento!
'''

def divisao(x=1,y=1):
    return x / y

print(divisao(50,0))