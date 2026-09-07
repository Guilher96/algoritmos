matriz= [
        [2, 4, 4,],          
        [5, 3, 2,],  
        [6, 3, 1,] 
]
print(matriz)
soma=0
for linha in matriz:
    for numero in linha:
        soma = soma + numero
        print(soma)
for linha in matriz:
    soma = 0
    for numero in linha:
        soma = soma + numero
        print(soma)