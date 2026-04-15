#12) Ler 5 números e mostrar o menor 
#Enunciado 
#Crie um programa que leia 5 números
# e determine qual deles é o menor.

#11) Soma de números pares em um intervalo 
#Enunciado 
#Peça ao usuário um número inteiro N e 
# calcule a soma de todos os números pares entre 1 e N. 


i=0;
valor=0;
numeros=[];
menor=0;
teste=0;



for i in range(5):
    valor = int(input("Digite um número : "));
    numeros.append(valor);
   

menor=numeros[i];

for i in range(5):
    if (numeros[i] <menor):
        menor=numeros[i];

print(menor);

