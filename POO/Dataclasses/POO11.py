# if __name__ = "__main__"
# Serve para verificar se o código está sendo executado diretamente ou se foi importado
# Quando importado ele ignora o IF e executa o que estiver na outra página!


def somar(a, b):
    return a + b

# Bloco de verificação
if __name__ == "__main__":
    print("O arquivo calculadora.py foi executado DIRETO!")
    resultado = somar(5, 5)
    print(f"O teste de 5 + 5 deu: {resultado}")