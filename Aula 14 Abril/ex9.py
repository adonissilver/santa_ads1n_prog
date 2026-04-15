#9) Ler 5 notas e informar quantas são aprovadas 
#Enunciado 
#Peça ao usuário 5 notas. 
# Considere aprovado quem tiver nota maior ou igual a 7.
#  Ao final, informe quantos alunos foram aprovados. 


aprovado=0;
numeros=[]
soma=0;

for i in range(5):
    valor = int(input("Digite um número: "))
    if(valor>=7):
       numeros.append(valor)
       aprovado=aprovado+1




print("total de aprovados: ",aprovado)
