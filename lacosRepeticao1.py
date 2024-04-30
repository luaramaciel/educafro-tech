'''
Elaborar um programa que apresente como resultado os quadrados calculados a partir
dos números inteiros existentes na faiza de valores de 15 a 200 sem que os valores sejam
armazenados em memória. Usar a máscara de apresentação 99999.
'''

print("Quadrados dos números inteiros na faixa de 15 a 200:")
print("Número | Quadrado")
print("------------------")

for num in range(15, 201):
    quadrado = num ** 2
    print(f"{num:5}   | {quadrado:5}")

print("------------------")
