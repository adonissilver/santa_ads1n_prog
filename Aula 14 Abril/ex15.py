
#15) Soma da série simples 
#Enunciado 
#Calcule a soma da série: 
#S=1+2+3+4+...+NS=1+2+3+4+...+N


a1=0;
an=0;

a1=int(input("Digite o primeiro termo da série: "))

an=int(input("Digite o último termo da série: "))

n= an-a1 +1;


print("Soma: ", ((a1+an)*n)/2);


