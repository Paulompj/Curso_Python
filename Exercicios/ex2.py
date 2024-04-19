print("------Bem vindo ao sistema de medias escolares------")
nota1=int(input("Digite a nota 1:"))
nota2=int(input("Digite a nota 2:"))
media=float((nota1+nota2)/2)
if media<7:
    print("Voce esta reprovado")
elif media>=7 and media<10:
    print("Parabéns!Voce foi aprovado")
elif media==10:
    print("Paraben! Voce foi aprovado com distinção")