
# 20) Solicitar um número da semana 
# e indicar o dia iniciando 1 como Domingo e 7 para sábado

semana = input("Digite o dia da semana: ").strip().upper()

if semana == 'DOMINGO':
    print("1")

elif semana == 'SEGUNDA' or semana == 'SEGUNDA-FEIRA' or semana == 'SEGUNDA FEIRA':
    print("2")

elif semana == 'TERÇA' or  semana=='TERCA' or  semana == 'TERÇA FEIRA' or semana == 'TERÇA-FEIRA' or semana == 'TERCA-FEIRA':
    print("3")

elif semana == 'QUARTA' or semana == 'QUARTA FEIRA'  or semana == 'QUARTA-FEIRA':
    print("4")

elif semana == 'QUINTA'  or semana == 'QUINTA FEIRA' or semana == 'QUINTA-FEIRA':
    print("5")

elif semana == 'SEXTA' or semana == 'SEXTA FEIRA' or semana == 'SEXTA-FEIRA':
    print("6")

elif semana == 'SÁBADO' or semana == 'SABADO':
    print("7")

else:
    print(" Dia inválido ")