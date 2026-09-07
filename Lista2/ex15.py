nome =["João", "Márcio", "Daniel", "Larissa", "Joyce"]
notas = [5.5, 7.7, 6.8, 9.5, 7.2]
for nome, notas in zip(nome, notas):
    if notas >= 6:
        print(nome, notas, "Aprovado")
    else:
        print(nome, notas, "Reprovado")

