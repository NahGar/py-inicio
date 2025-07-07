# van llaves de cualquier tipo porque set recibe un único parametro iterable
# los sets no tienen orden, no pueden tener duplicados y no son indexables
# soporta tuplas (por inmutable), no soporta listas
mi_set = set([1,2,3,4,5])
mi_set = set({1,2,3,4,5})
mi_set = set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)

otro_set  = {1,2,3}
print(type(otro_set))
print(otro_set)

print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)

print(f"Unión: {s3}")

s1.add(4)
print(f"Add: {s1}")

s1.remove(4)
print(f"Remove: {s1}")
s1.discard(4)  # No lanza error si no existe el elemento

sorteo = s1.pop()
print(f"Pop al no existir orden, si no recive parametro borra un elemento random: {sorteo}")

s1.clear() # Borra todos los elementos del set

mi_set_c = mi_set.copy()
print(f"Copia {mi_set_c}")

s1 = {1,2,3}
s3 = s1.difference(s2) # elementos que están en s1 pero no en s2
print(f"Differnce {s3}")

s3 = s1.difference_update(s2) # remueve de s1 los elementos que están en s2
print(f"Differnce_update {s3}")

s3 = s1.intersection(s2) # elementos que están en s1 y en s2
print(f"Intersection {s3}")
