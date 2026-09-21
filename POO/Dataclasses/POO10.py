# __str__

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'{self.name} ({self.grade})'

    def __repr__(self):
        return

mary = Student("Mary", "A+")
print(mary)

mary_str = str(mary)
print(mary_str)

# __repr__

class Student2:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"Student('{self.nome}', '{self.nota}')"

maria = Student2("Maria", "10")
mary_string = repr(maria)
print(mary_string)