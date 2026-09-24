from dataclasses import *

@dataclass
class Aluno:
    nome: str
    idade: int
    curso: str
    notas: list[float] = field(default_factory=list)

    def adicionar_nota(self, nova_nota: float):
        self.notas.append(nova_nota)
        print("NOTA ADICIONADA COM SUCESSO")

    def calcular_media(self):
        if not self.notas:
            return 0.0

        geral = sum(self.notas)
        media = geral / len(self.notas)
        print(f'A MÉDIA DE {self.nome} FOI: {media:.2f}')
        return media
        

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            print("APROVADO")
        else:
            print("RECUPERAÇÃO")

    def historico(self):
        media = self.calcular_media()
        print(f'''
        --- HISTÓRICO ESCOLAR ---
        NOME: {self.nome}
        NOTAS: {self.notas}
        MÉDIA: {media:.2f}
        CURSO: {self.curso}
''')

@dataclass
class Produto:
    nome: str
    preco: float
    categoria: str
    estoque:int = 0

    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * (desconto / 100))
        print(f"DESCONTO DE {desconto}% APLICADO COM SUCESSO")

    def valor_estoque(self, quantidade):
        self.estoque += quantidade
        print(f'O VALOR DO ESTOQUE É IGUAL A --> {self.preco * sum(self.estoque)}')