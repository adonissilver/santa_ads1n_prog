
#7) Ler 5 números e mostrar a soma 
#Enunciado 
#Faça um programa que leia 5 números informados pelo usuário e,
#  ao final, mostre a soma de todos eles.

soma=0;
numeros = []

for i in range(4):
    valor = int(input("Digite um número: "))
    numeros.append(valor)


for i in range(4):
        soma=soma+ numeros[i]

print(soma)
