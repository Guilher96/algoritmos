nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
nome = input("Digite um nome: ")
if nome in nomes:
        print("O índice na lista é:" , nomes.index(nome))
else:
        print("O nome não está na lista")
