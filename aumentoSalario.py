'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que este sofreu um aumento de 25%.

'''

def calcular_novo_salario(salario_atual):
    aumento = salario_atual * 0.25
    novo_salario = salario_atual + aumento
    return novo_salario

def main():
    salario_atual = float(input("Digite o salário atual do funcionário: R$ "))
    
    novo_salario = calcular_novo_salario(salario_atual)
    
    print("O novo salário do funcionário, com o aumento de 25%, é R$ {:.2f}".format(novo_salario))

if __name__ == "__main__":
    main()
