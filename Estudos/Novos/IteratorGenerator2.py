# Iterators
'''
nums = [1, 2, 3] # um Iteravel mas não é um Iterador
nums_iterable = iter(nums) # Torna nums um Iterador
'''
#-----------------------------------------------------------------------------------------
'''
while True:
    try:
        print(next(nums_iterable))
    except StopIteration:
        break
'''
#-----------------------------------------------------------------------------------------
'''
print(next(nums_iterable))
print(dir(nums_iterable))
'''
#-----------------------------------------------------------------------------------------
'''
print(next(nums_iterable))
print(next(nums_iterable))
print(next(nums_iterable)) # Se passar do tamanho da lista ocorre o StopIteration
'''

'''
for num in nums:
    print(num)
'''
#-----------------------------------------------------------------------------------------

'''
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
'''
#-----------------------------------------------------------------------------------------

# Generator = Iterator
# pausa a fução e retorna o valor
# use yield ao invés de return
# você pode iterar sem carregar tudo na memória
# yield = uma torneira gota

'''
def my_range(start,end):
    current = start
    while current < end:
        yield current
        current +=1

num = my_range(1, 10)

print(next(num))
print(next(num))
print(next(num))
print(next(num))
'''


# yield - torna o código mais eficiente e ocupa menos memória!

'''
def ler_csv(nome_arquivo):
    for linha in open(nome_arquivo, "r"):
        yield linha


vendas = ler_csv("Novos/vendas.csv")
print(vendas)
'''

def count_to(n):
    count = 1
    while count <= n:
       yield count
       count += 1
       
number = int(input("Escrece um número para contar: "))

for n in count_to(number):
    print(n)