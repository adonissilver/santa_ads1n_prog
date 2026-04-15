#13) Classificação de notas com if...elif 
#Enunciado 
#Peça 5 notas ao usuário. Para cada nota, classifique: 
#•	Aprovado se nota for maior ou igual a 7  
#•	Recuperação se nota for maior ou igual a 5 e menor que 7  
#•	Reprovado se nota for menor que 5  

nota=0;

for i in range(1, 6):
    nota=int(input("Digite a nota: "));
    if (nota>=7):
        print("Aprovado")

    elif(nota>=5 and nota<7):
        print("Recuperacao ")

    elif(nota<5):
        print("Reprovado")