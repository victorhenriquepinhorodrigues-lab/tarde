
#Desenvolva um programa em Python que solicite a quantidade de pessoas a serem cadastradas em um evento
#e, para cada uma, peça a idade e se possui convite (1 para sim e 0 para não)
# # aplicando as regras de que menores de 16 anos não entram
# pessoas entre 16 e 17 anos só entram com convite
# maiores de 18 anos entram com ou sem convite
# ao final informe quantas pessoas entraram, quantas foram barradas e quantas entraram sem convite.
    
qtd_pessoas = int(input("Digite o total de pessoas a serem cadastradas: "))
    
contador = 0
entraram = 0
barradas = 0
entradaSemConvite = 0



#Baguio das idade
    
while qtd_pessoas > contador:
    idade = int(input("Digite a idade: "))
    convite = int(input("Possui convite? (1 = sim, 0 = não): "))
    if (idade < 16):
        print("Você Não pode entrar")
        barradas +=1

    if (idade >= 16 and idade <= 17):
        print(convite)
        if(convite == 0):
            print("Acesso Negado")
            barradas += 1
        elif(convite == 1):
            print("Acesso Permitido")
            entraram +=1

    if (idade >= 18):
        if(convite == 0):
            print("Acesso Permitido")
            entradaSemConvite +=1
            entraram +=1
        elif(convite == 1):
            print("Acesso Permitido")
            entraram +=1
    contador += 1
#Contagem dos cara 
print(f"{qtd_pessoas} que foram cadastradas.")
print(f"Foram Barradas {barradas} pessoas.")
print(f"{entraram} Pessoas entraram na festa.")
print(f"{entradaSemConvite} Entraram sem convite.")