try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Você não pode dividir um número por zero!")
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
else:
    print(f"O resultado da divisão é {resultado}")
finally:
    print("Fim da execução do bloco de tratamento.")
    
    
def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('n2 não pode ser 0')
    return n1 / n2

