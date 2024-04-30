'''
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com as regras a seguir, verifique 
e mostre a classificação da pessoa:

Se altura for menor que 1,20m e o peso até 60kg, categoria A.
Se altura for maior que 1,20m e menor ou igual a 1,70m e o peso até 60kg, categoria B.
Se a altura for maior que 1,70 e o peso até 60kg, categoria C.

Se altura for menor que 1,20m e o peso for maior que 60kg e menor ou igual a 90kg, categoria D.
Se altura for maior que 1,20m e menor ou igual a 1,70m e o peso  for maior que 60kg e menor ou igual a 90kg, categoria E.
Se a altura for maior que 1,70 e o peso  for maior que 60kg e menor ou igual a 90kg, categoria F.

Se altura for menor que 1,20m e o peso for maior que 90kg, categoria G.
Se altura for maior que 1,20m e menor ou igual a 1,70m e o peso for maior que 90kg, categoria H.
Se a altura for maior que 1,70 e o peso for maior que 90kg, categoria I.
'''

def classificar_pessoa(altura, peso):
    if altura < 1.20:
        if peso <= 60:
            categoria = 'A'
        elif peso <= 90:
            categoria = 'D'
        else:
            categoria = 'G'
    elif altura <= 1.70:
        if peso <= 60:
            categoria = 'B'
        elif peso <= 90:
            categoria = 'E'
        else:
            categoria = 'H'
    else:
        if peso <= 60:
            categoria = 'C'
        elif peso <= 90:
            categoria = 'F'
        else:
            categoria = 'I'
    return categoria

def main():
    altura = float(input("Digite a altura da pessoa (em metros): "))
    peso = float(input("Digite o peso da pessoa (em quilogramas): "))

    categoria = classificar_pessoa(altura, peso)

    print("Categoria da pessoa:", categoria)

if __name__ == "__main__":
    main()
