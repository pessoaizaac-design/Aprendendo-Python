from poligono import *

def main():
    q1 = Quadrado(3)
    
    print(f'O perímetro desse quadrado é igual a: {q1.perimetro()}')
    print(f'A área desse quadrado é igual a: {q1.area()}')
    
    c1 = Circulo(5)
    
    print(f'O perímetro desse círculo é igual a: {c1.perimetro():.2f}')
    print(f'A área desse círculo é igual a: {c1.area()}')

if __name__ == '__main__':
    main()