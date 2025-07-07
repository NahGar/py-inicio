texto = input("Ingrese un texto: ")
letras = []
letras.append(input("Ingrese la primera letra: "))
letras.append(input("Ingrese la segunda letra: "))
letras.append(input("Ingrese la tercera letra: "))

textoL = texto.lower()

print(f"1) El texto tiene {textoL.count(letras[0].lower())} veces la letra '{letras[0].lower()}' "
      f"{textoL.count(letras[1].lower())} veces la letra '{letras[1].lower()}' y "
      f"{textoL.count(letras[2].lower())} veces la letra '{letras[2].lower()}'")

palabras = texto.split()
print(f"2) La frase tiene {len(palabras)} palabras")

print(f"3) La primera letra es {texto[0:1]} y la última letra es {texto[-1]}")

palabrasAlreves = palabras.copy()
palabrasAlreves.reverse()
textoAlreves = ' '.join(palabrasAlreves)

print(f"4) Palabras en orden inverso {textoAlreves}")

aparecePython = bool(textoL.count("python"))
print(f"5) Aparece python {aparecePython}")
