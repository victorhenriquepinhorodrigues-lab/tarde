#um programa que funcione da seguinte maneira: Solicite ao usuário que informe a quantidade total de pessoas em um grupo. 
#Para cada pessoa, peça que ousuário registre o sexo, utilizando a letra 'm' ou 'M' para masculino.
#O programa deve contar e, ao final, exibir o total de pessoas do sexo masculino.

n_pessoas = int(input("Digite o número de pessoas: "))
masculino = 0
feminino = 0
for pessoa in range(0,n_pessoas,1):
    print("M/m - Masculino \n \
    F/f - Feminino")
    genero = input(f"Qual o genero da pessoa {pessoa}? ").lower()
    if genero == "m" or genero == "Masculino":
        masculino +=1
    else:
        feminino +=1
print(f"De todas as pessoas, {masculino}, eram do genero Masculino.")
print(f"e {feminino} eram do genero Feminino.")