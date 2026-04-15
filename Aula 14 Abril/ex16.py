#16) Soma dos números pares 
#Enunciado 
#Calcule a soma da série: 
#S=2+4+6+8+...+NS=2+4+6+8+...+N

soma = 0

n = int(input("Digite um número: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        soma =soma+i

print("Soma dos números pares até", n, "é:", soma)