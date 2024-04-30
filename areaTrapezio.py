'''
Faça um programa que calcule e mostre a área de um trapézio

'''

def calcular_area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return area

def main():
    base_maior = float(input("Digite o valor da base maior do trapézio: "))
    base_menor = float(input("Digite o valor da base menor do trapézio: "))
    altura = float(input("Digite o valor da altura do trapézio: "))
    
    area = calcular_area_trapezio(base_maior, base_menor, altura)
    
    print("A área do trapézio é:", area)

if __name__ == "__main__":
    main()
