# Polimorfismo

class Jogador:
    def __init__(self, altura, velocidade, passe, drible, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.drible = drible
        self.precisao = precisao

    def passar(self):
        print("Mirar")
        print("Enconstar na bola com a força de passe do jogador")

    def chutar(self):
        print("Mirar")
        print("Encostar na bola com 2x a força do passe do jogador")

    def defender(self):
        print("Tentar tirar a bola do adversário")

class Goleiro(Jogador):
    def agarrar(self):
        print("Pular")
        print("Se esticar para pegar a bola")

    def defender(self):
        esta_fora_da_area = False
        if esta_fora_da_area:
            print("Usar apenas os pés, cabeça e ombro")
        else:
            print("Usar qualquer parte do corpo")
        print("Tentar tirar a bola do adversário")

class Linha(Jogador):
    def defender(self):
        print("Usar apenas os pés, cabeça e ombro")
        print("Tentar tirar a bola do adversário")

jogador1 = Goleiro(180, 60, 60, 50, 70)
jogador2 = Linha(175, 90, 80, 85, 90)

jogador1.defender()
jogador2.defender()