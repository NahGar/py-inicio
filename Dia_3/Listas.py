mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
otra_lista = ['hola', 12, 2.7]

print(type(mi_lista))

resultado = len(mi_lista)
print(f"len: {resultado}")

resultado = mi_lista[0]
print(f"indice 0: {resultado}")

resultado = mi_lista[0:2]
print(f"indice 0 a 2: {resultado}")

print(f"listas sumadas: {mi_lista3}")

mi_lista3[0] = 'alfa'
print(f"sobreescribir lista: {mi_lista3}")

mi_lista3.append("g")
print(f"append: {mi_lista3}")

mi_lista3.pop()
print(f"pop borra ultimo: {mi_lista3}")

eliminado = mi_lista3.pop(0)
print(f"pop borra indice 0: {mi_lista3} y eliminado: {eliminado}")

lista_desordenada = ['g', 'b', 'd', 'a']
lista_desordenada.sort()
print(f"ordena lista: {lista_desordenada}")

lista_desordenada.reverse()
print(f"ordena lista al reves: {lista_desordenada}")