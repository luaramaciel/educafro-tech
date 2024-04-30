""" 
Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os
dados necessários para executar cada operação.
Menu de opções:
- Somar dois números.
- Raiz quadrada de um número.
- Digite a opção desejada 

"""

import math

def somar_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)

def calcular_raiz_quadrada():
    num = float(input("Digite o número para calcular a raiz quadrada: "))
    if num >= 0:
        raiz = math.sqrt(num)
        print("A raiz quadrada de", num, "é:", raiz)
    else:
        print("Não é possível calcular a raiz quadrada de um número negativo.")

def mostrar_menu():
    print("Menu de opções:")
    print("1. Somar dois números.")
    print("2. Calcular a raiz quadrada de um número.")
    print("3. Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            somar_numeros()
        elif opcao == "2":
            calcular_raiz_quadrada()
        elif opcao == "3":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
