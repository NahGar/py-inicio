from random import randint, choice, shuffle, uniform, random

aleatorio = randint(1,50)
print("randint enteros:",aleatorio)

aleatorio = round(uniform(1,50),1)
print("uniform con decimales",aleatorio)

aleatorio = random()
print("random de 0 a 1",aleatorio)

aleatorio = choice(["Rojo", "Verde", "Azul", "Amarillo"])
print("choice:",aleatorio)

numeros = list(range(1, 20))
shuffle(numeros)
print("shuffle:",numeros)