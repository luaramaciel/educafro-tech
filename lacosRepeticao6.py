'''
Elaborar um programa que leia dez valores numéricos reais e apresente no final o
somatório e a média dos valores lido.
'''

# Inicializando variáveis
soma = 0

# Loop para ler os valores e calcular a soma
for i in range(1, 11):
    valor = float(input(f"Digite o {i}º valor: "))
    soma += valor

# Calculando a média
media = soma / 10

# Apresentando o somatório e a média
print("Somatório dos valores:", soma)
print("Média dos valores:", media)
