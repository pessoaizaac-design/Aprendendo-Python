# Split, Join e Enumerate

# Split --> Transformar uma string em uma lista.
texto = 'Aprender é legal'

palavras = texto.split()
print(palavras)
# Saída = ['Aprender', 'é', 'legal']

# Possível dividir se usar vírgulas e outros fatores
texto = 'Aprender,é,legal'

palavras = texto.split(',')
print(palavras)
# Saída = ['Aprender', 'é', 'legal']

# Join --> Processo inverso do Split
lista = ['Aprender', 'é', 'legal!']

palavras = ' '.join(lista)
print(palavras)
# Saída = Aprender é legal!

#Enumerate --> Usado em loops (for) para numeração

frutas = ['Maçã', 'Banana', 'Laranja']

for posicao, fruta in enumerate(frutas):
    print(f'A fruta {fruta} está na posição {posicao}')
# Saída = A fruta Maçã está na posição 0
# Saída = A fruta Banana está na posição 1
# Saída = A fruta Laranja está na posição 2