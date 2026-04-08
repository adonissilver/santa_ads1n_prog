#Pedir 5 números e mostrar o maior

maior=0


for i in range(1,6):
    numeros=int(input("Digite um  número : "))
    if(numeros>maior):
        maior=numeros

print("o maior é ",maior)

