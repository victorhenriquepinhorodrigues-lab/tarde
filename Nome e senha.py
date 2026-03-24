#Crie um programa que peça o nome de usuário e a senha. O sistema deve permitir o acesso apenas se o usuário for "admin" e a senha for "1234". Caso contrário, deve exibir uma mensagem de acesso negado.

login = "admin"
senha = "1234"

usuario = input("Qual seu Usuario: ")
senhap = int(input("Qual sua senha: "))




if (usuario == login and senha == senhap):
    print("bem vindo admin")
else:
    print("usuario ou senha incorretos")
