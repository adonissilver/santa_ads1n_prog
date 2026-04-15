# 10) Ler 5 idades e contar maiores de idade 
#Enunciado 
#Faça um programa que leia 5 idades 
# e informe quantas pessoas têm 18 anos ou mais.

maior=0;
numeros=[]
soma=0;

for i in range(5):
    valor = int(input("Digite uma idade: "))
    if(valor>=18):
       numeros.append(valor)
       maior=maior+1;





print("total de maiores de idade:  ",maior)
