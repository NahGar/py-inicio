palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

# Utilizando comprensión de listas
lista = [letra for letra in palabra]
print(lista)

lista = [letra for letra in 'python']
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)

lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lista)

pies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
metros = [pie / 3.281 for pie in pies]
print(metros)