turmas = int(input("Digite a quantidade de turmas: "))
contador = 0
total_alunos = 0

while turmas >= contador:
    alunos = int(input(f"Digite a quantidade de alunos da turma: "))
    if alunos <= 40:
        total_alunos += alunos
        contador += 1
    else:
        print("ERRO: Não pode ser maior que 40 não.")

media_alunos = total_alunos/contador

print(F"Média de alunos por turma: {media_alunos}")