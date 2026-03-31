#Desenvolva um programa que solicite ao usuário um nome e uma senha, garantindo que a senha não seja igual ao nome de usuário.
#Se forem iguais, exiba uma mensagem de erro e peça as informações novamente.

for tentativa in [1,2,3]:
    nome = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")
    if nome == senha:
        print("Erro: a senha não pode ser igual ao nome de usuário.")
    else:
        print("Cadastro realizado com sucesso!")
        break