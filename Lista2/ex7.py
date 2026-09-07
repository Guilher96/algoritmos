lista = [16,87,45,32,96,78,90,123]
numero = int(input("Digite um número: "))
for n in lista:
    if numero == n:
        print("O numero está na lista")
    else:
        print("O número não está na lista!")
        
    break