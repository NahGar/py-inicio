lista = ['a', 'b', 'c', 'd', 'e']

for item in enumerate(lista): # Enumerador genera item = tapple con el índice y el valor
    print(item)


for indice, valor in enumerate(lista):
    print(indice, valor)


mis_tuples = list(enumerate(lista))  # Convierte el enumerador a una lista de tuplas
print(mis_tuples)
print(mis_tuples[1][1])