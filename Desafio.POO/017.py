from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preço):
        self.produto = nome
        self.valor = preço
  
    def etiqueta(self):
        conteudo = f'{self.produto.center(30, ' ')}'
        conteudo += f"-" * 30
        precof = f"R${self.valor:,.2f}"
        conteudo += f"{precof.center(30, '-')}"

        etiqueta = Panel(conteudo, title='ETIQUETA', width= 34)
        print(etiqueta)

pr1 = Produto('MacBook Pro', 10500)
print(pr1)

pr1.etiqueta()

