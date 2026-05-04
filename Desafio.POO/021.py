from rich import print

class Caneta:
    def __init__(self, caneta, texto):
        traducao = {
"azul" : "b blue",
"vrde" : "b green",
"roxo" : "b purpel",
"rosa" : "b pink",
"vermelho" : "b red",
"branco" : "b white",
"preto" : "b black",
"amarelo" : "b yellow"  
}
        
        self.caneta = traducao.get(caneta.lower(), "b white")
        self.texto = texto
        self.aberta = False

    def destampar(self):
        self.aberta = True
        print('Caneta aberta!')

    def tampar(self):
        self.aberta = False
        print('Caneta fechada!')

    def escrever(self):
        if self.aberta:
            print(f'[{self.caneta}]{self.texto}[/{self.caneta}]')
        else:
            print('Você não consegue escrever pois sua caneta está fechada!')


c1 = Caneta("Azul", "Isso é um teste")
c1.destampar()
c1.escrever()