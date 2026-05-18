from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisando(self):
        condicao = f'Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n'
        condicao += 'Cada participante comerá 0.4Kg e  cada Kg custa R$82.40\n'

        pessoas = self.quant
        recomenda = (pessoas * 400)
        condicao += f'Recomendo [blue]comprar {recomenda}Kg[/] de carne\n'

        custo = (recomenda/1000) * 82.40
        condicao += f'O custo total será de [green]R${custo:,.2f}[/]\n'

        pagar = custo / pessoas
        condicao += f'Cada pessoa irá pagar [yellow]R${pagar:,.2f}[/] para participar'
        
        
        convite = Panel(condicao, title= 'Churras dos amigos', width= 70)
        print(convite)

p1 = Churrasco('Churras dos Amigos', 15)
p1.analisando()