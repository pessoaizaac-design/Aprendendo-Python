import os

name = os.environ.get('USERNAME')
print(f'User: {name}')

print(os.getcwd())

novo_caminho = r'C:/Users/pesso/Downloads'
os.chdir(novo_caminho)
print(os.getcwd())

os.mkdir('TESTE')
print(os.listdir())

os.makedirs(r'C:/Users/pesso/Downloads/Junho/03/06')
print(os.listdir())

os.rmdir(r'C:/Users/pesso/Downloads/Junho/03/06')

