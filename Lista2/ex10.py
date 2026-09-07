numeros = [18, 5, 12, 3, 20, 7, 9]
print("A lista original é:", numeros)
numeros.sort()
print("A lista com ordem crescente:", numeros)
numeros.sort(reverse=True)
print("A lista com ordem decrescente:", numeros)
# diferença entre sort() e sorted()
# sort --> sorteia os elementos da lista modificando a própria.
#sorted--> sorteia os elementos da lista, porém mantendo a original e criando uma nova lista.