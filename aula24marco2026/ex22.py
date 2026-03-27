# 22) Solicite peso e altura e calcule o imc, apresente a mensagem conforme o resultado
# Imc=peso/altura²
# Tabela de Valores IMC (Adultos)
# Abaixo de 18,5: Abaixo do peso
# 18,5 – 24,9: Peso normal (Eutrófico)
# 25,0 – 29,9: Sobrepeso (Pré-obesidade)
# 30,0 – 34,9: Obesidade Grau I
# 35,0 – 39,9: Obesidade Grau II (Severa)
# Maior que 40,0: Obesidade Grau III (Mórbida)



print("TESTE DE I.M.C : Índice de Massa Corporal ")

def calcular_imc(peso, altura):
    return peso / (altura * altura)


def mostrar_resultado(imc, peso, altura):
    print(f"\nIMC: {imc:.2f}")

    peso_min = 18.5 * (altura * altura)
    peso_max = 24.9 * (altura * altura)

    if imc < 18.5:
        print("Você está abaixo do peso ideal")
        print(f"Seu peso mínimo deveria ser: {peso_min:.2f} Kg(s)")
        print(f"Você precisa aumentar: {peso_min - peso:.2f} Kg(s)")

    elif 18.5 <= imc <= 24.9:
        print("Você está com o peso ideal")
        print(f"Você pode ter até {peso_max:.2f} Kg(s)")

    elif 25 <= imc <= 29.9:
        print("Sobrepeso")
        print(f"Você precisa diminuir: {peso - peso_max:.2f} Kg(s)")

    elif 30 <= imc <= 34.9:
        print("Obesidade Grau I")
        print(f"Você precisa diminuir: {peso - peso_max:.2f} Kg(s)")

    elif 35 <= imc <= 39.9:
        print("Obesidade Grau II (Severa)")
        print(f"Você precisa diminuir: {peso - peso_max:.2f} Kg(s)")

    else:
        print("Obesidade Grau III (Mórbida)")
        print(f"Você precisa diminuir: {peso - peso_max:.2f} Kg(s)")


# Programa principal
print("TESTE DE I.M.C : Índice de Massa Corporal")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)
mostrar_resultado(imc, peso, altura)

    

