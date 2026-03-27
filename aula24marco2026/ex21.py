# 21) Solicite dois números e solicitar 
# qual operação deseja fazer (+, - , /, *). 
# Apresentar o resultado da operação escolhida


numero1=int(input("Digite um número inteiro :"))
operacao=input("Digite o símbolo da operação: + - * /")

numero2=int(input("Digite o segundo número inteiro : "))


if operacao=='+':
    print("A soma é : ",numero1+numero2)

if operacao=='-':
    print ("A subtração é: ",numero1-numero2)

if operacao=='*':
    print("A multiplicação é :",numero1*numero2)

if operacao=='/':
    print("A divisão é :",numero1/numero2)

elif (operacao !='+') or (operacao !='-') or (operacao !='*') or (operacao !='/'):
    print("voce digitou um operador inválido, tente novamente ")








