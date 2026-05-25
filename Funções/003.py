'''
 Funções - def em Python - *args **kwargs(parte 3)
'''
def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])
    
lista1 = [20,12,17,35,25]
lista2 = [13, 22 ,17 ,14, 19]
func(*lista1, *lista2, nome='Luiz', sobrenome='Miranda')
    
    
    


