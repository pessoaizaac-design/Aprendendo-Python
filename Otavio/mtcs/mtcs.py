class MetaClass(type):
    def __new__(mcs, name, bases, namespace):
        print('__new__ da metaclass')
        cls = super().__new__(mcs, name, bases, namespace)      
        return cls
       

class Person:
    def __new__(cls, *arg, **kwargs):
        print('__new__ da cls')
        return super().__new__(cls)
    
    def __init__(self, nome, último_nome):
        self.nome = nome
        self.último_nome = último_nome
    

     
pessoa1 = Person('Luiz', 'Otávio')
pessoa2 = Person('Maria', 'Oliveira')
