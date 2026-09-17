# Encapsulamento

'''
public, protected and private

_privado/protected (public_)
__privado (_NOMECLASSE__nomeatributo)
'''

# 1 dunder - recomendo não acessar o atributo! (protected)
# 2 dunders -  recomenda de uma maneira mais forte não acessar o atributo!

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir(self, id, cliente):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: cliente}
        else:
            self.__dados['clientes'].update({id: cliente})

    def listar(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar(self,id):
        del self.__dados['clientes'][id]

#-----------------------------------------------------------------------------------------

bd = BaseDeDados()
bd.inserir(1, 'Higor')
bd.inserir(2, 'Pedro')
bd.__dados = 'Outra coisa'
# print(bd.__dados)
print(bd._BaseDeDados__dados) # Mudança de nome do atributo
# bd.listar()
print(bd.dados) # Conseguimos acessar por conta da Property ( ñ conseguimos alterar)


        