from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('Higor', 18, "Ciência da computação", '117A')
    a1.aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods= True)

    p1 = Professor('Antenor', 69, 'Lógica matemática', 'Mestrado')
    p1.aniversario()
    p1.dar_aula()
    #inspect(p1, methods= True)

    f1 = Funcionario('Carlos', 27, 'Faxineiro', 'Sala de aula')
    f1.aniversario()
    f1.bater_ponto()
    #inspect(f1, methods= True)

if __name__ == "__main__":
    
    main()
    