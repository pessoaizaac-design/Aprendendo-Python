
class Heroi:
    def __init__(self, nome, vida = 100, ataque = 0, classe = 'Humano'):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.classe = classe
        
    def atacar_vilao(self, inimigo,):
        return f'{self.nome} atacou {inimigo.nome} e de {inimigo.vida} HP ele foi para {inimigo.vida - self.ataque} HP'
        

class Inimigo:
      def __init__(self, nome, vida = 100, ataque = 0, classe = 'Humano'):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.classe = classe
        
      def atacar_heroi(self, heroi,):
        return f'{self.nome} atacou {heroi.nome} e de {heroi.vida} HP ele foi para {heroi.vida - self.ataque} HP'
    
heroi = Heroi('Batman', 100, 20)
inimigo = Inimigo('Coringa', 100, 10)

print(heroi.atacar_vilao(inimigo))
print(inimigo.atacar_heroi(heroi))
        
        