
#14) Contar números dentro de um intervalo 
#Enunciado 
#Peça ao usuário 5 números e conte quantos
#  deles estão entre 10 e 20. 



i=0;
numeros=[]
conta=0;
valor=0;




for i in range(5):
    valor = int(input("Digite um número : "));
    numeros.append(valor);
    if(numeros[i]>10 and numeros[i]<20):
        conta=conta+1;

    
print(conta);