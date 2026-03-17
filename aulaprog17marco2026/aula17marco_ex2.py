

nota1=int(input("Digite nota 1: "))
nota2=int(input("Digite nota 2: "))
nota3=int(input("Digite nota 3: "))

media=int((nota1+nota2+nota3)/3)

if media>=7:
    print("Aluno Aprovado! Parabéns!! ")
elif media<7:
    print("Prova de Recuperação, estude um pouco mais!!! ")