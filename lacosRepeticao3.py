'''Elaborar um programa que apresente o somátorio dos valores pares existentes na faixa
de 1 até 500
'''

soma_pares = 0

for num in range(2, 501, 2):
    soma_pares += num

print("A soma dos valores pares na faixa de 1 até 500 é:", soma_pares)
