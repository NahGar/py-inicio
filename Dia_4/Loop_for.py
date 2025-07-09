lista = ['a', 'b', 'c', 'd', 'e']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")


lista = ['pablo', 'maria', 'juan', 'ana', 'luis']

for nombre in lista:
    if nombre.startswith("l"):
        print(nombre)

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
    print(mi_valor)
print(f"Total {mi_valor}")

palabra = 'python' #String es iterable

for letra in palabra:
    print(letra)

for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)
    print(objeto[0])
    print(objeto[1])


for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic:
    print(item) #imprime las claves

for item in dic.items():
    print(item) #imprime las tuplas (clave, valor)

for item in dic.values():
    print(item) #imprime los valores

for clave, valor in dic.items():
    print(f"{clave} : {valor}")