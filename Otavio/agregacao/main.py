from Otavio.agregacao.agregacao import Produto
from Otavio.agregacao.agregacao import CarrinhoDeCompras

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 199)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 50)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())

