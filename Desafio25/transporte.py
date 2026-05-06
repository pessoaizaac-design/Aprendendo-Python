from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0.0

    
        
    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    def calcular_frete(self):
      distancia = self.distancia
      valor_frete = distancia * 0.50
      self.frete = valor_frete
      return valor_frete

class Caminhao(Transporte):
    def calcular_frete(self):
        distancia = self.distancia
        valor_frete = distancia * 1.20
        self.frete = valor_frete

        if distancia >= 50:
         return valor_frete
        else:
         return 'Distância inválida para o uso do Caminhão como meio de frete!'
    
class Drone(Transporte):
    def calcular_frete(self):
        distancia = self.distancia
        valor_frete = distancia * 9.50
        self.frete = valor_frete

        if distancia >= 10:
            return valor_frete
        else:
           return 'Distância inválida para o uso do Drone como meio de frete!'
        