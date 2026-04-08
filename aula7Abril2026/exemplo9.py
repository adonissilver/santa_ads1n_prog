#Pedir 5 números e mostrar o menor

menor=1


for i in range(1,6):
    numeros=int(input("Digite um  número : "))
    if(numeros<menor):
        menor=numeros

print("o menor é ",menor)

