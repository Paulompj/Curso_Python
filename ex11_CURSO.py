nome=input("Digite  seu nome:") 
tamanho_nome=int(len(nome))
idade=input("Digite sua idade:")
print("Seu nome invertido é",nome[-1::-1])
print("Sua idade ao contrario é:",idade[::-1])
if " " in nome: #Verifica se tem espaço no nome
    print("Seu nome contem espaços")
else:
    print("Seu nome noa contem espaços")
#-1 é o ulimo caractere
# [início:final:de quanto em quanto]
