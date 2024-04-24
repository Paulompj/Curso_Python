str1="-"
print(f"{str1:-<10}Bem vindo ao inversor de palavras e números{str1:-<10}")
print("1 - Inverter Nomes")
print("2 - Inverter números")
print("3 - Sair")
escolha=int(input("Escolha:"))
if escolha==1:
    nome=input("Digite seu nome:")
    print(f"Seu nome invertido é:",nome[::-1])
elif escolha==2:
    idade=input("Digite seu idade:")
    print("Sua idade invertida é:",idade[::-1])
elif escolha==3:
    print("Saindo...")
else:
    print("Escolha inválida")
    print("Saindo...")


