#6) Números Positivos 
 
#Faça um programa que leia 5 números digitados pelo usuário e, 
# ao final, informe quantos deles são positivos.


numeros = []

for i in range(4):
    valor = int(input("Digite um número: "))
    if (valor>0):
        numeros.append(valor)

print(numeros)