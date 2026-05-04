from rich import print
from rich.panel import Panel
'''
Maneira mais simples de criar um paiel pro meio da biblioteca rich
'''

classe = Panel('Isso daqui é um teste', style='Red', width= 25, title='[blue]Mensagem[/]')
print(classe)