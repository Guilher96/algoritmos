numero = int(input("Digite um número: "))
maior = numero
menor = numero
for n in range(1, 5):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print("Maior:", maior)
print("Menor:", menor)
