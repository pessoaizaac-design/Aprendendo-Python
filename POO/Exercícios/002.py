# Polimorfismo

class Notificacao:
    def enviar(self,mensagem):
        print(f"Escrita: {mensagem}")

class Email(Notificacao):
    def enviar(self,mensagem):
        print(f"E-mail: {mensagem}")

class Sms(Notificacao):
    def enviar(self,mensagem):
        print(f"Sms: {mensagem}")

class Push(Notificacao):
    def enviar(self,mensagem):
        print(f"Push: {mensagem}")

#-----------------------------------------------------------------------------------------

class Pagar:
    def pagar(self, confirmacao):
        print(f"Dinheiro: {confirmacao}")

class Cartao(Pagar):
    def pagar(self, confirmacao):
        print(f'Cartão: {confirmacao}')

class Pix(Pagar):
    def pagar(self, confirmacao):
        print(f'Pix: {confirmacao}')

class Boleto(Pagar):
    def pagar(self, confirmacao):
        print(f'Boleto: {confirmacao}')

#-----------------------------------------------------------------------------------------

# Herança

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):
        print(f'Nome: {self.nome} | Salário: {self.salario}')

class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario)
        self.cargo = cargo


    def mandar(self):
        print(f'{self.cargo} está trabalhando')

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def programando(self):
        print(f'O desenvolvedor está programando em {self.linguagem}')

class Estagiario(Funcionario):
    def __init__(self, nome, salario, fazendo):
        super().__init__(nome, salario)
        self.atividade = fazendo

    def executando(self):
        print(f'O estagiário esta {self.atividade}')

#-----------------------------------------------------------------------------------------

class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f'Ligando {self.modelo}')

    def desligar(self):
        print(f'Desligando {self.modelo}')

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_de_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade = capacidade_de_carga

    def peso(self):
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Capacidade: {self.capacidade}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_de_portas):
        super().__init__(marca, modelo, ano)
        self.portas = numero_de_portas

    def qtnd_portas(self):
        print(f'{self.modelo} tem {self.portas} portas')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def qtnd_cilindradas(self):
        print(f'{self.modelo} contém {self.cilindradas} cilindradas')

