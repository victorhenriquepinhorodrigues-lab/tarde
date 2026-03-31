#um programa em Python que leia números inteiros do teclado até que o usuário
# digite 0. Ao final, exiba a soma de todos os números digitados.

numero = int(input("Digite um número(0 para sair): "))
total = 0

while numero != 0:
    total += numero
    numero = int(input("Digite um número(0 para sair): "))
print(f"O total de numeros é: {total}")