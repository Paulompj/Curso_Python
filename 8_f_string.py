'''nome="Paulo Moraes Strickland"
peso=95
altura=1.80
imc=peso/(altura*altura)
print("O",nome,"tem",altura,"e pesa",peso,".Tendo um IMC igual a:",imc)
var=f"{nome} tem {altura:.2f} de altura, pesa {peso}, totalizando um imc igual a {imc}"
print("USANDO F-STRING")
print(var)
print("USANDO FORMAT")'''
# ---------------------------------------------------------------------------------
'''nome="Paulo"
peso=65.2
altura=1.80
imc=peso/(altura*altura)
formato="O {} pesa {} e tem {} de altura.Tendo um imc de: {:.1f}".format(nome,peso,altura,imc)
print(formato)
# printf("A idade do usuario1 é:%d. Usuario2: %d",idade,idade2)'''
# ---------------------------------------------------------------------------------
nome="Paulo"
peso=65.2
altura=1.80
imc=peso/(altura*altura)
string="O {} pesa {} e tem {:.2f} de altura.Tendo um imc de {}."
formato= string.format(nome,peso,altura,imc)
print(formato)
# ----------------------------------------------------------------------------------