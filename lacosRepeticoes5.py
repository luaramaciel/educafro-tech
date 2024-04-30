'''
Construir um programa que apresente todos os valores numéricos inteiros divisíveis
por 4 e menores que 200. A variável que controla o contador do laço deve ser
obrigatoriamente iniciada com valor 1. Usar a máscara de apresentação 999

'''

print("Valores numéricos inteiros divisíveis por 4 e menores que 200:")
print("-------------------------------")

contador = 1

while contador < 200:
    if contador % 4 == 0:
        print(f"{contador:3}")
    contador += 1

print("-------------------------------")
