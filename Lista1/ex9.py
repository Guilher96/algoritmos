def numeros():
    num1=int(input("Digite um número: "))
    num2=int(input("Digite outro número: "))
    if num1 > num2:
        print("O numero maior é:", num1)
    elif num2 > num1:
        print(" O número maior é:", num2)
    else:
        print("Os números são iguais.")

numeros()