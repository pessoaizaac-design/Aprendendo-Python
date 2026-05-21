from dataclasses import dataclass, field

class OldPerson:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        class_str = f'{self.__class__.__name__}'\
            f'({self.firstname} {self.lastname})'
        return class_str
    
    def __eq__(self, o: object):
        return self.lastname == o.lastname
        
    def __repr__(self):
        return str(self)
    
@dataclass
class Person:
    firstname: str
    lastname: str
    active: bool = False
    addresses: list = field(default_factory=list)
    fullname: str = field(default ='Missing', init=False, repr=False, compare=False)

    def __post_init__(self):
        self.fullname = f'{self.firstname}'\
        + '' + {self.lastname}
