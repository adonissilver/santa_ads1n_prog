# Exercício 7 – Expressão matemática

# Peça dois números e calcule:

# resultado = (a + b) * 2

# Depois calcule:

# resultado = a + b * 2

# Qual a diferença?


a=float(input("Digite o primeiro valor: "))

b=float(input("Digite o segundo valor"))

resultado = (a + b) * 2
resultado2 = a + b * 2

diferenca= resultado-resultado2

print("Resultado1: ",resultado)
print("Resultado2: ",resultado2)
print("Diferença: ",diferenca)