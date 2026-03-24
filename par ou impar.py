# Faça um programa que receba um número inteiro e diga se ele é par ou ímpar.
numero = int(input("Digite seu numero: "))
resto = numero % 2
print(resto)
if (resto == 0):
    print(f"Seu numero é par")
elif (resto != 0):
    print(f"Seu numero é impar")
