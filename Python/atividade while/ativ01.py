#um programa que solicite ao usuário uma nota entre zero e dez. Se o valor
#informado for inválido, exiba uma mensagem de erro e continue solicitando uma
#nota válida até que o usuário a forneça.

nota = int(input('Digite sua nota de ATÉ 0 A 10: '))

while (nota < 0 or nota > 10):
    nota = int(input("Tu tem problema, refaça: "))
print(f"sua nota é {nota}")