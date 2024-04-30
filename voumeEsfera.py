'''
Faça um programa para calcular o volume de uma esfera de raio, onde o dado é fornecido 
pelo usuário.

'''

import math

# Solicitando o raio da esfera ao usuário
raio = float(input("Digite o raio da esfera: "))

# Calculando o volume da esfera
volume = (4/3) * math.pi * raio ** 3

# Exibindo o resultado
print("O volume da esfera é:", volume)
