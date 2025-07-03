nombre = "Carina"
# nombre[0] = "K" # Esto generará un error porque las cadenas son inmutables en Python
nombre = "K" + nombre[1:]
print(nombre)

n1 = "Kari"
n2 = "na"
print(n1 + n2)  # Concatenación de cadenas
print((n1 + " ") * 10)  # Repetición de cadenas

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

print(f"Existe agua en poema: {"agua" in poema}")
print(f"No existe agua en poema: {"agua" not in poema}")

print(f"Lenght poema: {len(poema)}")  # Longitud del poema