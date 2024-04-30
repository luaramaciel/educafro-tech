'''
Faça um programa que receba o salário base e o tempo de serviço de um funcionário. Calcule e mostre o 
imposto conforme regras a seguir:
Se o salário base for menor que 200,00 o salário é isento de imposto.
Se o salário for maior ou igual a 200,00 e menor e igual a 450,00 o imposto é de 3%.
Se o salário for maior que 450,00 e menor que 700,00 o imposto é de 8%.
Se o salário for maior ou igual a 700,00 o imposto é de 12%
'''

def calcular_imposto(salario_base):
    if salario_base < 200:
        imposto = 0
    elif salario_base <= 450:
        imposto = salario_base * 0.03
    elif salario_base < 700:
        imposto = salario_base * 0.08
    else:
        imposto = salario_base * 0.12
    return imposto

def calcular_gratificacao(salario_base, tempo_servico):
    if salario_base > 500 and tempo_servico <= 30:
        gratificacao = 20
    elif salario_base > 500 and tempo_servico > 3:
        gratificacao = 30
    elif salario_base <= 500 and tempo_servico >= 3 and tempo_servico < 6:
        gratificacao = 35
    elif salario_base <= 500 and tempo_servico >= 6:
        gratificacao = 33
    else:
        gratificacao = 0
    return gratificacao

def calcular_categoria(salario_liquido):
    if salario_liquido <= 350:
        categoria = 'A'
    elif salario_liquido <= 600:
        categoria = 'B'
    else:
        categoria = 'C'
    return categoria

def main():
    salario_base = float(input("Digite o salário base do funcionário: "))
    tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))

    imposto = calcular_imposto(salario_base)
    gratificacao = calcular_gratificacao(salario_base, tempo_servico)
    salario_liquido = salario_base - imposto + gratificacao
    categoria = calcular_categoria(salario_liquido)

    print("Imposto: R$", imposto)
    print("Gratificação: R$", gratificacao)
    print("Salário líquido: R$", salario_liquido)
    print("Categoria: ", categoria)

if __name__ == "__main__":
    main()

