
class Estoque:
    def __init__(self):
        self.estoque = {}
        
    def adicionar_produto(self, nome, preco, quantidade):
        self.estoque[nome] = {'Preço': preco,'Quantidade': quantidade}
        
    def remover_produto(self,nome):
        if nome in self.estoque:
            del self.estoque[nome]
            print(f'{nome} FOI REMOVIDO COM SUCESSO!')
        else:
            print(f'{nome} NÃO FOI ENCONTRADO NO ESTOQUE')
            
    def calcula_total(self, nome, preco, quantidade):
        if nome in self.estoque:
          preco = self.estoque['Preço']
          quantidade = self.estoque['Quantidade']
            
          total = preco * quantidade
          return total
        else:
          print(f'{nome} NÃO FOI ENCONTRADO NO ESTOQUE')
          
          
        

