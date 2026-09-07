lista = [11, 30, 65, 90]

maior = lista[0]
segundo = lista[0]

for n in lista:
    if n > maior:
        segundo = maior
        maior = n
    elif n > segundo and n != maior:
        segundo = n
print("O maior numero é:", maior)
print("O segundo maior é :", segundo)