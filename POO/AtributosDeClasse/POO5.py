# Atributos de classe

class A:
    vc = 123

    def __init__(self):
        self.vc = 321

a1 = A()
a2 = A()

A.vc = 'Alterado' # altera em todas as instâncias por conta do self

print(a1.vc)
print(a2.vc)
print(A.vc) # com o dunder init o vc=123 só é atríbuido a classe

'''
a1.vc =321 # Só muda a instância a1, não afeta a classe

print(a1.__dict__) # retorna --> {"vc": 321}
print(a2.__dict__) # retorna --> {}
print(A.__dict__) # retorna --> {'__module__': '__main__', 'vc': 123}

'''


