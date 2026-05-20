from composicao import Cliente, Endereco

cliente1 = Cliente("Luiz", 32)
cliente1.insere_endereco('Recife','Pe')
print(cliente1.nome, cliente1.idade)
cliente1.lista_endereco()
del cliente1
print()


cliente2 = Cliente('Maria', 22)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome, cliente2.idade)
cliente2.lista_endereco()
print()

cliente3 = Cliente('Romerio', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome, cliente3.idade)
cliente3.lista_endereco()
print()

print('=' * 68)