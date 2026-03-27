#Crie um programa em Python que peça a idade de uma pessoa e se ela possui autorização dos responsáveis (responda com "sim" ou "não"). O programa deve permitir a entrada no evento caso a pessoa tenha 18 anos ou mais ou tenha autorização. Caso contrário, deve informar que a entrada não é permitida.

idade = int(input("Digite sua idade: "))
autorizacao = input("Você possui uma autorização\n" \
"s / n: ")

if (idade >= 18 or autorizacao == "s"):
    print("Entrada Permitida")
else:
    print("Entrada proibida")

