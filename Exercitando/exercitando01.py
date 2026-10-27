# Exercitando Itertools

from itertools import *

print("Exercício 01")
status = ["Carregando", "Processando", "Finalizado"]

count = 0
for s in cycle(status):
    if count <= 15:
        print(f"{count} ==> {s}")
        count += 1
    else:
        break
print()

print("Exercício 02")
palavra_repetida = list(repeat("Python", 6))

print(palavra_repetida)
print()

print("Exercício 03")
ingredientes = ["Queijo", "Tomate", "Frango", "Milho", "Bacon"]

combinacoes = list(combinations(ingredientes, 3))
print(combinacoes)
print()

print("Exercício 04")
tamanhos = ["P", "M", "G"]
estampas = ["Preta", "Branca"]

combinacoes_dois = list(product(tamanhos, estampas))
print(combinacoes_dois)
print()

print("Exercício 05")
pendentes = ["Estudar Python", "Praticar Java"]
em_andamento = ["Criar uma landing page", "Estudar CSS"]
concluidas = ["Aprender funções", "Estudar listas"]

juntos = list(chain(pendentes, em_andamento, concluidas))
print(juntos)
print()

print("Exercício 06")
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
selecionados = [False, True, True, False, True]

aprovados = list(compress(nomes, selecionados))
print(aprovados)
print()

print("Exercício 07")
numeros = [1, 2, 3, 4]

permutacao = list(permutations(numeros, 2))
print(permutacao)
print()