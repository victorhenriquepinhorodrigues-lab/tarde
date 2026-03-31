#um programa em Python que peça ao usuário para criar uma senha e, em seguida,
# solicite que ele a digite novamente. Continue pedindo até que as duas senhas
# correspondam.

senha1 = input("Digite sua senha: ")
senha = input("Confirme a senha sua senha: ")

while senha1 != senha:
    print("Ta errado mané")
    senha = input("Confirme a senha criada novamente")
print("Acerto rapa")