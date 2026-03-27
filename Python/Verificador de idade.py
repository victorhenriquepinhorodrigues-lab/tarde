idade = int(input("Qual sua Idade?: "))

if ( idade >= 18 ):
    print(f"Sua idade é {idade}. Você é um adulto, pode entrar.")
elif( idade >= 12 ):
    print(f"Sua idade é {idade}. Você é um adolecente, Saia do site.")
elif( idade < 12):
    print(f"Sua idade é {idade}. Você é uma criança, vai jogar roblox.")