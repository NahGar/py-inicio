texto = "Este es el texto de Pepe"

print(f"upper: {texto.upper()}")  # Convierte todo el texto a mayúsculas
print(f"lower: {texto.lower()}")  # Convierte todo el texto a minúsculas

resultado = texto.split()
print(f"split usa espacio por defecto: {resultado}")

resultado = texto.split("t")
print(f"split con letra t: {resultado}")

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(f"join: {e}")

print(f"find: {texto.find("Pe")}")
print(f"find: {texto.find("w")}") # Retorna -1 si no encuentra el caracter

resultado = texto.replace("Pepe", "Juan")
print(f"replace: {resultado}")