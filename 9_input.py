print("------BEM VINDO A CALCULADORA DE IMC------")
nome=input("Digite seu nome:")
altura=float(input("Digite seu altura:"))
peso=float(input("Digite seu peso:"))
imc=peso/(altura*altura)
if imc<18.5:
    print("Voce esta abaixo do peso ?",imc<18.5)
    print(f"Olá,{nome}.Voce pesa {peso}kgs e tem {altura} de altura.")
    print(f"Seu imc é:{imc}")
    print("Voce está abaixo do peso saudável")
elif imc>=18.5 and imc<24.5:
    print(f"Olá,{nome}.Voce pesa {peso}kgs e tem {altura} de altura.")
    print(f"Seu imc é:{imc}")
    print("Voce esta dentro do peso saudável")
elif imc>=24.5:
    print(f"Olá,{nome}.Voce pesa {peso}kgs e tem {altura} de altura.")
    print(f"Seu imc é:{imc}")
    print("Voce esta acima do peso saudável")
