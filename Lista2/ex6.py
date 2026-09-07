lista=[1,5,66,754,12,44,57,88,17,99]
pares =[]   
impares =[] 
for n in lista:
    if n % 2 ==0:
        pares.append (n)
    else:
        impares.append(n)
print("os numeros pares sao:", pares)
print("os numeros impares sao:", impares)
       


