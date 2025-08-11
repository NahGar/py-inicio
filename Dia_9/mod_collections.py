from collections import Counter

numeros = [8,5,5,4,8,2,6,2,4,5,4,8,2,6,4,8,1,2,1,5,3,6,7,8,4]
print(Counter(numeros))

print(Counter('mississippi'))

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([8,5,5,4,8,2,6,2,4,5,4,8,2,6,4,8,1,2,1,5,3,6,7,8,4])
print(serie.most_common()) # tuplas de más repetidos
print(serie.most_common(1)) # el más repetido
print(serie.most_common(2)) # los 2 más repetidos
print(list(serie)) # genera valores únicos

from collections import defaultdict

mi_defaultdic = defaultdict(lambda: 'nada')
mi_defaultdic['uno'] = 'verde'
print(mi_defaultdic['uno'])
print(mi_defaultdic['dos']) # no existe y se crea en el dic a partir de lo definido en lambda

from collections import namedtuple

Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)
print(ariel.altura)

