numeros= [7.5, 6.3, 3.8, 4.9, 8.1, 9.7, 5.6, 2.3, 7.3, 6.6]
soma = sum(numeros)
media = soma / len(numeros)
print(media)
for n in numeros:
    if n > media:
        print("O número", n, "é maior que a média")


