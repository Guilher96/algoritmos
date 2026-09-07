produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
quantidades = [12, 25, 4, 3, 8]

produto = input("Digite o produto que deseja consultar: ")

if produto in produtos:
    posicao = produtos.index(produto)
    print("Quantidade em estoque:", quantidades[posicao])

    nova_quantidade = int(input("Digite a nova quantidade: "))
    quantidades[posicao] = nova_quantidade
else:
    print("Produto não encontrado")

print("\nProdutos com estoque inferior a 5:")

for i in range(len(produtos)):
    if quantidades[i] < 5:
        print(produtos[i], "-", quantidades[i])

maior = quantidades[0]
produto_maior = produtos[0]

for i in range(len(quantidades)):
    if quantidades[i] > maior:
        maior = quantidades[i]
        produto_maior = produtos[i]

print("\nMaior estoque:", produto_maior, "-", maior)