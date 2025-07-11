
menor = min(58,69,24,87,35,96)
mayor = max(58,69,24,87,35,96)

print(f"El menor es: {menor}")
print(f"El mayor es: {mayor}")

lista_numeros = [58,69,24,87,35,96]
print(f"El menor de la lista es: {min(lista_numeros)} y el mayor es: {max(lista_numeros)}")

nombres = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
print(f"El primer nombre es: {min(nombres)} y el último es: {max(nombres)}")

# Considera mayúsculas primero y minúsculas después
nombre = "María"
print(f"La primer letra es: {min(nombre)} y la última es: {max(nombre)}")
print(f"La primer letra es: {min(nombre.lower())} y la última es: {max(nombre.lower())}")

dic = {"C1": 45, "C9": 11}
print(min(dic)) # busca en las claves
print(min(dic.values())) # busca en los valores