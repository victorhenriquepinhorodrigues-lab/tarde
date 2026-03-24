# Aula 1 - Introdução ao Python
# comentario é feito com o simbolo #
"""
comentarios de múltiplas linhas são feitos com o 
"""
# Variavel é um espaço na memória para armazenar um valor
nome = "henrique"
print(nome)

nome = "thais"
nome = "lais"
nome = "jessica"
print(nome)
# vairaveis podem armazenar diferentes tipos de dados

idade = 25 # Variavel tipo inteiro
altura = 1.75 # Variavel do tipo float
print(idade)
print(altura)
# Print é uma função que exibe valor na tela
# Podemos usar operações matematicas com váriaveis númericas

#Operações Matematicas

soma = 10 + 5
divisão = 10 / 2
subtração = 10 - 3
multiplicacao = 10 * 4
expoente = 2 ** 3
resto = 10 % 3

# Operações com strings
nome_completo = nome + "Silva" #Concatenando

# Operadores de comparação
print(10 > 5)  # True
print(10 < 5)  # False
print(10 == 10)  # True
print(10 != 5)  # True  
print(10 >= 10)  # True
print(10 <= 5)  # False

# if é uma estrutura de controle de fluxo que permite executar um bloco de código se uma condição for verdadeira
if (idade >= 18):
    print("Você é maior de idade.")
# elif é usado para verificar outra condição se a primeira for falsa
elif (idade >= 13):
    print("Você é um adolescente.")
# else é usado para executar um bloco de código se todas as condições anteriores forem falsas
else:
    print("Você é uma criança.")