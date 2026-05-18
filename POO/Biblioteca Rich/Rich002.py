from rich import print
from rich.table import Table
'''
Cria uma tabela, de forma mais funcional e simples
'''

tabela = Table(title= 'TABELA DE PREÇOS')

tabela.add_column('Nome', justify='left')
tabela.add_column('Preço', justify= 'center', style='b green')

tabela.add_row("Lápis", "$1,50")
tabela.add_row('Borracha', '$2,50')

print(tabela)