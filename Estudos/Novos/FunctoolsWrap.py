# Functools Wrap
#-----------------------------------------------------------------------------------------
from functools import *

# singledispatch - permite criar funções genéricas; se comporta de acordo com o tipo do dado

'''
@singledispatch
def fun(arg):
    pass

@fun.register
def _(arg: int):
    print('Fui chamada para um inteiro')

@fun.register
def _(arg: str):
    print('Fui chamada para uma string')

fun('string')
'''

#singledisparhcmethod - serve para métodos de classes
'''
class NeuraNetwork:
    @singledispatchmethod
    def negar(self,arg):
        raise NotImplementedError('Não foi implementado')

    @negar.register
    def _(self,arg: int):
        return -arg

    @negar.register
    def _(seçf,arg: bool):
        return not arg

x = NeuraNetwork()
print(x.negar(False))
'''

# partial - permite congelar parâmetros da função

'''
def mul(n1,n2):
    return n1 *  n2

dobro = partial(mul, n2=2)
triplo = partial(mul, n2=3)

print(mul(1,2))
print(dobro(10))
'''

# partialmethod - conglear parâmetro de uma classe

class Numero:

    def mul(self,n1,n2):
        return n1 * n2

    dobrar = partialmethod(mul, n2=2)

n = Numero()
print(n.mul(3,5))
print(n.dobrar(15))

