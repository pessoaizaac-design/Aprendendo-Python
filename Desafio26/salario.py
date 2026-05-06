from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.sal_min = 1491.10

    @abstractmethod
    def calcular_sal(self):  # Ajustado o nome aqui
        pass

    def analisar_sal(self):
        qtd_salarios = self.salario / self.sal_min
        print(f"[{self.nome}] Ganha o equivalente a {qtd_salarios:.1f} salário(s) mínimo(s).")


class Horista(Funcionario):
    def __init__(self, nome, valor_hr, horas_trab):
        super().__init__(nome)
        self.valor_hr = valor_hr
        self.horas_trab = horas_trab
        self.calcular_sal()  # Ajustado o nome aqui

    def calcular_sal(self):  # Ajustado o nome aqui
        self.sal_bruto = self.valor_hr * self.horas_trab
        self.salario = self.sal_bruto * 0.925
        
        print(f"--- Horista: {self.nome} ---")
        print(f"Bruto ({self.horas_trab}h x R$ {self.valor_hr:.2f}): R$ {self.sal_bruto:.2f}")
        print(f"Líquido (-7.5%): R$ {self.salario:.2f}")


class Mensalista(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome)
        self.salario_base = salario_base
        self.calcular_sal()  # Ajustado o nome aqui

    def calcular_sal(self):  # Ajustado o nome aqui
        self.sal_bruto = self.salario_base
        self.salario = self.sal_bruto * 0.925
        
        print(f"--- Mensalista: {self.nome} ---")
        print(f"Bruto Fixo: R$ {self.sal_bruto:.2f}")
        print(f"Líquido (-7.5%): R$ {self.salario:.2f}")
        
        
        
    
    