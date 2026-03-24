#Crie um programa que receba o salário de um funcionário e seu tempo de empresa (em anos). O funcionário receberá um bônus apenas se tiver salário menor que 3000 e tempo de empresa maior ou igual a 2 anos. Caso contrário, não receberá bônus. O programa deve exibir uma mensagem informando se o bônus foi concedido ou não.

salario = int(input("Qual seu salario atual: "))
tempimpresa = int(input("Quantos anos você esta: "))

if (salario < 3000 and tempimpresa >= 2):
    print("Parabéns, você ganhou um bônus")
else:
    print("Você não ganhou o bônus")