#11) Soma de números pares em um intervalo 
#Enunciado 
#Peça ao usuário um número inteiro N e 
# calcule a soma de todos os números pares entre 1 e N. 




i=0;
aprovado=0;
numeros=[]
soma=0;

limite=0;


limite=int(input("Digite a quantidade de números que deseja digitar: "))

for i in range(limite):
    valor = int(input("Digite um número : "))
    numeros.append(valor);
    


for i in range(limite):
    soma=soma+numeros[i];


print("total de aprovados: ",soma);
