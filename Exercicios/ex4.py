'''primeiro=int(input("Digite um inteiro: "))
segundo=int(input("Digite outro inteiro: "))
terceiro=int(input("Digite um outro inteiro: "))
menor=0
maior=0
if primeiro>=segundo and primeiro>=terceiro:
    maior=primeiro
elif segundo>=primeiro and segundo>=terceiro:
    maior=segundo
elif terceiro>=primeiro and terceiro>=segundo:
    maior=terceiro

if primeiro<=segundo and primeiro<=terceiro:
    menor=primeiro
elif segundo<=primeiro and segundo<=terceiro:
    menor=segundo
elif terceiro<=primeiro and terceiro<=segundo:
    menor=terceiro

    
print("O menor numero que voce digitou foi:",menor)
print("O maior numero que voce digitou foi:",maior)
'''
primeiro=int(input("Digite um inteiro: ")) 
segundo=int(input("Digite outro inteiro: ")) 
terceiro=int(input("Digite um outro inteiro: ")) 
maior=primeiro
if segundo>=maior and segundo>=terceiro:
    maior=segundo
elif terceiro>=maior and terceiro>=segundo:
    maior=terceiro
    
print("O maior numero que voce digitou foi:",maior)