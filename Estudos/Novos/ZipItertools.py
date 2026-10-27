# Zipping
from itertools import *

#-----------------------------------------------------------------------------

a = [10, 20, 30, 40, 50, 60]
b = [1, 2, 3, 4]
# c = 'ABC'

#-----------------------------------------------------------------------------

# x = list(zip(a, b, c)) 
# Passa uma lista de tamanho três, pois ele pega o de menor quanridade

#-----------------------------------------------------------------------------

# x = list(zip(a, b, strict=False)) 
# se Strict = False faz igual o ex acima

# print(x)
# passa uma lista de tuplas (list), e um Dicionário (dict)

#-----------------------------------------------------------------------------

# c = [x+y for x,y in zip(a,b,strict=False)]
# print(c)

#-----------------------------------------------------------------------------

c = list(zip_longest(a,b, fillvalue=0))
print(c)

#-----------------------------------------------------------------------------
 
# Count - loop infinito
#x = count(start= 10, step=1)
#for i in count(start=10, step=1):
    #print(i)
    #if i == 20:
        #break

#-----------------------------------------------------------------------------

# Cycle # Loop do seu iteravél
#y = cycle('abc')
#count = 0
#for i in y:
    #print(i)
    #count +=1
    #if count == 6:
        #break

#-----------------------------------------------------------------------------

# Repeat - repete o number quantas vezes você definir
#z = repeat(10,3)
#for i in z:
    #print(i)

#-----------------------------------------------------------------------------

# Acumulate - pecorre a lista e vai somando os numbers (acumulando)
#w = accumulate([1, 2, 3, 4 ,5])
#for i in w:
    #print(i)

#-----------------------------------------------------------------------------

# Chain - caminha str por str da list ou text
#v = chain('caio', [1,2,3])
#for i in v:
    #print(i)

#-----------------------------------------------------------------------------

# Compress - usa 1 ou 0 para definir se printa ou não o elemento
#p = list(compress([1, 2, 3, 4, 5], [1, 0, 0, 1, 1]))
#print(p)

#-----------------------------------------------------------------------------

# Product
#for i in range(1,4):
    #x = list(product('abcd', repeat=i))
    #print(len(x))

#-----------------------------------------------------------------------------

# Permutation - igual o product só que sem valores repetidos
x = list(permutations('abc', 2))
print(x)