from rich import print
import time

class livro:
    def __init__(self, titulo, paginas = 1):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        self.avançou = 0
        self.concluido = False
        print(f" [blue] Você acabou de abrir o livro [red]'{self.titulo}' [/]  que tem [green] {self.paginas} paginas[/] no total. voçê agora está na [/][yellow]  pagina  {self.pagina_atual} [/] ")

    def passar_pagina(self, quantas):
        if self.concluido == True:
            print(f'[red] Voçê já concluiu o livro [/] [green] {self.titulo} [/]')
            return
            
        for i in range(quantas):
            if self.pagina_atual >= self.paginas:
                print(f' [green] Parabens, voçê chegou ao final do livro [/] [red] {self.titulo} [/]')
                self.concluido = True
                break
            time.sleep(0.4)
            print(f'pag{self.pagina_atual} :right_arrow:   ', end= '', flush= True)
            self.pagina_atual += 1
            self.avançou += 1
            
        print(f'[blue] voçê avançou {self.avançou} paginas e agora está na [/]{i} [yellow] pagina {self.pagina_atual} [/]')

    