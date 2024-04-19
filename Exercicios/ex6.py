primeiro=int(input("Digite um inteiro: ")) 
segundo=int(input("Digite outro inteiro: ")) 
terceiro=int(input("Digite um outro inteiro: ")) 
maior=primeiro
menor=primeiro
meio=primeiro
# DESCOBRIR O MAIOR
if segundo>=maior and segundo>=terceiro:
    maior=segundo
elif terceiro>=maior and terceiro>=segundo:
    maior=terceiro

# DESCOBRIR O MENOR
if segundo<=menor and segundo<=terceiro:
    menor=segundo
elif terceiro<=menor and terceiro<=segundo:
    menor=terceiro

# DESCOBRIR O DO MEIO
if primeiro==maior and terceiro==menor:
    meio=segundo
elif primeiro==maior and segundo==menor:
    meio=terceiro
elif segundo==maior and terceiro==menor:
    meio=primeiro
elif segundo==maior and primeiro==menor:
    meio=terceiro
elif terceiro==maior and primeiro==menor:
    meio=segundo
elif terceiro==maior and segundo==menor:
    meio=primeiro


print("Maior:",maior,"Meio:",meio,"Menor:",menor)
    
