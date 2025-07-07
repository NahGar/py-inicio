# diferencias con las listas: las tuplas son inmutables, es decir, no se pueden modificar una vez creadas.
# además ocupan menos espacio en memoria que las listas.
mi_tuple = (1, 2, (10,20), 4)

print(type(mi_tuple))
print(mi_tuple[0])
print(mi_tuple[2][1])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1,2,3)
x,y,z = t # Desempaquetado de tuplas funciona si contiene el mismo número de elementos que variables
print(x,y,z)

t = (1,2,3,1)

print(f" len: {len(t)}")
print(f" count de unos: {t.count(1)}") # cuenta el número de veces que aparece el elemento 1
print(f" index 2: {t.index(2)}") # devuelve el índice del primer elemento que coincide con el valor 2