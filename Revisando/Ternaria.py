# Operação Ternária ==> Simplificar IF e ELSE em uma única linha
idade = 18

#Jeito original
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
    
# Com a operação ternária
id = 17

print('Maior de idade' if id >=18 else 'Menor de idade')