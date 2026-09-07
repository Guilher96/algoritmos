numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = []
pares = []
maiores = []
for n in numeros:
    quadrados.append(n**2)
    if n % 2 == 0:
        pares.append(n)
    elif n > 5:
        maiores.append(n)

print("O quadrado dos valores são:", quadrados)
print("Os números pares dos valores são:", pares)
print("Os valores maiores que 5 são: ", maiores)


  

    