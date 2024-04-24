str1="-"
print(f"{str1:-<7} Verificador de numeros positivos e negativos{str1:-<7}")
numero_digitado=input("Digite o núemro a ser verificado:")
if "-" not in numero_digitado:
    print("O número é postivo")
else:
    print("O número é negativo")