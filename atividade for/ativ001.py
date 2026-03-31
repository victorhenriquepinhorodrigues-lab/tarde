numero = int(input("Digite Até onde a Sequencia vai: "))

anterior = 0
atual = 1

while atual <= numero:
    print(atual)
    proxima = anterior + atual
    anterior = atual
    atual = proxima

