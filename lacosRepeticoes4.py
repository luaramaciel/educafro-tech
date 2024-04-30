'''
Elaborar um programa que apresente todos os valores numéricos inteiros ímpares
situados na faixa de 0 a 20. Usar a máscara de apresentação 999.
'''

print("Valores numéricos inteiros ímpares na faixa de 0 a 20:")
print("-------------------------------")

for num in range(1, 21, 2):
    print(f"{num:3}")

print("-------------------------------")
