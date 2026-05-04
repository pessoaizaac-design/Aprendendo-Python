from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_jogo(self,joguinho):
        self.jogos_favoritos.append(joguinho)

    def lista__jogos(self): 
        condicao = f'Nome real: {self.nome}\n'
        condicao += f'Jogos favoritos: \n{}'
        

        lista_jogos = Panel(condicao, title=f'Jogador <{self.nick}>')
        print(lista_jogos)

    