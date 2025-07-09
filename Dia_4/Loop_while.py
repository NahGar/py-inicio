monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más monedas")

respuesta = 's'

while respuesta == 's':
    respuesta = input("¿Quieres seguir? (s/n): ")
else:
    print('Bucle terminado')

nombre = input('Ingresa tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break # sale del bucle
    if letra == 'a':
        continue # salta a la siguiente iteración
    print(letra)
