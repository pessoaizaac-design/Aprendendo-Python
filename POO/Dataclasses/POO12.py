# dataclasses
# Facilita a vida no POO e encurta os codes de classes

from dataclasses import dataclass, field

'''
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __repr__(self):
        class_str = f'{self.__class__.__name__}'\
            f'({self.name} {self.lastname})'
        return class_str

    def __eq__(self, o):
        return self.lastname == o.lastname
'''

#-----------------------------------------------------------------------------------------

'''
Default - Serve para passar um valor padrão.
Default_Factory - Serve para funções que geram valores ( list, dict e etc..).

Init - Ele indica que o valor vai ser iniciado.
__post_init__ - Permite que vocÇe faça validações ou calcule campos dependentes.

repr - Decide se ele vai ser mostrado no print ou não.
compare - Serve para comparar valores.
kw_only - Se ativo só permite chamar o campo como kwarg.

frozen - Se ativo ele torna o campo estáticoa (bloqueada).
slots - Serve para trocar o dict e consome menos memória.
'''
     
@dataclass(frozen=True, slots=True)
class Person:
    name: str
    lastname: str
    active: bool = False
    adress: list = field(default_factory=list, repr=False, compare=False, kw_only=False)
    full_name: str = field(default='Missing', init=True, repr=True)

    def __post_init__(self):
        full_name = f'{self.name}'\
            f'{self.lastname}'
        object.__setattr__(self, 'full_name', full_name)

    def get_full_name(self):
        return self.full_name

if __name__ == '__main__':
    john1 = Person("John", "Doe", True, ['R1'], 'John Doe')
    john2 = Person("John", "Doe", True, ['R2'])

    print(john1)
    print(john1.get_full_name())
    # print(john2.full_name)
    # print(john1 == john2)