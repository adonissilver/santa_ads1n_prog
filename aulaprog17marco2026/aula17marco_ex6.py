valor=float(input("Digite o valor da compra: "))
if valor>=200:
    desconto=(valor*0.9)
    print("Valor com desconto: ",desconto)

elif valor<200:
    print("Sua compra nao tem desconto ")
