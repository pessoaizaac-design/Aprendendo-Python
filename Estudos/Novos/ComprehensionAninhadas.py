# comprehensions aninhadas - loops dentro de outros loops
#-----------------------------------------------------------------------------------------
'''
linhas = int(input("Quanta linhas: "))
colunas = int(input("Quantas columas: "))
caracter = input("Informe o caracter a ser usado: ")

for i in range(linhas):
    for j in range(colunas):
        print(caracter, end="")
    print()
'''
#-----------------------------------------------------------------------------------------

caixas = [['Ovo 1, Ovo 2'], ['Ovo 3', 'Ovo 4'],['Ovo 5', 'Ovo 6']]

loop_externo = []
for caixa in caixas:
    for ovo in caixa:
        loop_externo.append(ovo)

loop_interno = [ovo for caixa in caixas for ovo in caixa]
print(loop_interno)

#-----------------------------------------------------------------------------------------

tres_tres = [["Hello" for i in range(3)] for j in range(3)]
for linha in tres_tres:
    print(linha)

#-----------------------------------------------------------------------------------------

numeros = [[2, 15, 17], [11, 5, 22], [8, 13, 1]]
maiores_que_dez = [num for linha in numeros for num in linha if num > 10]
print(maiores_que_dez)

#-----------------------------------------------------------------------------------------

