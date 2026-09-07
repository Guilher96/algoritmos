vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]

total = sum(vendas)
media = total / len(vendas)

maior = max(vendas)
menor = min(vendas)

acima_media = 0

for venda in vendas:
    if venda > media:
        acima_media += 1

percentagem = (acima_media / len(vendas)) * 100

print("Total vendido:", total)
print("Média diária:", media)
print("Maior venda:", maior)
print("Menor venda:", menor)
print("Dias acima da média:", acima_media)
print("Percentual acima da média:", percentagem, "%")