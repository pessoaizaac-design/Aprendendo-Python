# w+ = Ler e escrever no arquivo (apaga as linhas adicionas nos outros momentos)
# r+ = Ler oq está dentro do arquivo
# a+ = Ativa o append mode (add coisas no arquivo sem apagar ele)


file = open('abc.txt', 'w+') # Open = abrir o arquivo
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
print('==============')

file.seek(0, 0)
print('Lndo linhas:')
print(file.read())
print('==============')

file.seek(0, 0)
print(file.readline(), end='') # ReadLine = ler uma linha
print(file.readline(), end='')
print(file.readline(), end='')
print('==============')

file.seek(0,0)
for linha in file.readlines(): # ReadLines = Ler todas as linhas escritas
    print(linha)

file.close()

with open('abc.txt', 'w+') as file: # Não precisa fechar o arquivo
    file.write('Linha 1\n') # Write = escrever
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    
    file.seek(0) # Seek = onde o arquivo cmc a ser lido
    print(file.read()) # Read = o arquivo cmc a ser lido
    
