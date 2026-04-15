#8) Ler 5 números e mostrar a média 
#Enunciado 
#Crie um programa que leia 5 números e calcule
#  a média aritmética entre eles. 

media=0
numeros=[]
soma=0;

for i in range(5):
    valor = int(input("Digite um número: "))
    numeros.append(valor)


for i in range(5):
        soma=soma+ numeros[i]

media=soma/5;
print(media)
