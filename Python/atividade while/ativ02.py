#um programa que calcule e exiba a média aritmética de N notas fornecidas pelo usuário.

n = int(input("Quantas notas você tem que por? "))

soma = 0
contador = 0

while contador < n:
    nota = float(input(f"Digite a nota {contador+1}: "))
    soma += nota
    contador += 1

media = soma/n
print(f"Sua Média é: {media}")