from abc import ABC, abstractclassmethod

class Bebida_Quente(ABC):

    def preparar(self):
        print('---Iniciando o Preparo---')
        self.ferver()
        self.misturar()
        self.servir()
        print('---Bebida Pronta---')

    def ferver(self):
        print('1. Fervendo água a 100 graus celsius.')
        

    @abstractclassmethod
    def misturar(self):
        pass

    @abstractclassmethod
    def servir(self):
        pass

class Cafe(Bebida_Quente):

    def misturar(self):
        print('2. Passando água pressurizada pelo pó de café moído.')
    
    def servir(self):
        print('3. Servindo em xícara pequena')
    
class Cha(Bebida_Quente):

    def misturar(self):
        print('2. Mergulhando o sachê  de ervas na água.')
    
    def servir(self):
        print('3. Servindo com canela na porcelna com limão.')

class Leite(Bebida_Quente):

    def misturar(self):
        print('2. Passando vapor pressurizado pelo bico de leite.')
    
    def servir(self):
        print('3. Servino na caneca grande,já com café')

        