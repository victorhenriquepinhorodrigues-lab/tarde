#um programa que leia 5 números e calcule a soma e a média desses números, exibindo os resultados.
numero = 0
total = 0
for numero in range(1,6):
    nota = int(input(f"Digite a {numero}ª nota: "))
    if numero > 0:
        total += nota
        print(numero)
        print(nota)
        print(total)
media = total/5
print(int(media))

"""total = 0
numero = 0
lista = [1,2,3,4,5]
for numero in lista:
    total += numero
media = total/5
print(int(media))"""