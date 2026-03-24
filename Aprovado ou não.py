#Crie um programa que receba a nota final de um aluno e sua frequência (em porcentagem). O aluno será considerado aprovado se tiver nota maior ou igual a 7 ou frequência maior ou igual a 75%. Caso contrário, deverá ser reprovado. O programa deve exibir uma mensagem informando a situação do aluno.

notafinal= int(input("Nota do aluno: "))
frequencia = int(input("Frequencia do aluno: "))

if (notafinal >= 7 or frequencia >= 75):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")