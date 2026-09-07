lista = [2, 3, 2, 5, 3, 2]
vezes = []

for n in lista:
    if n not in vezes:
        quantidade = lista.count(n)
        print(n, "aparece", quantidade, "vezes")
        vezes.append(n)