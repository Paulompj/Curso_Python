print("------BEM VINDO A QUITANTA DO SEU JOAO------")
print("Produtos disponíveis: Maçãs")
print("Preço: se comprar menos que 12, é 0,30 a unidade. Se comprar uma duzia ou mais, custará 0,25 a unidade")
quantidade_comprada=int(input("Digite a quantidade maça que você deseja comprar:"))
if quantidade_comprada<12:
    preco_unid=0.30
    preco_total_compra=float(quantidade_comprada*0.30)
    print(f"Preço total da sua compra:{preco_total_compra:.0f}reais")
    print("Obrigado. Volte sempre!")
elif quantidade_comprada>=12:
    preco_unid=0.25
    preco_total_compra=quantidade_comprada*preco_unid
    print(f"Preço total da sua compra:{preco_total_compra} reais")
    print("Obrigado. Volte sempre!")


