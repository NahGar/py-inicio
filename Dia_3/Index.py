
mi_texto = "Esta es una prueba"

resultado = mi_texto[0]
print("Indice 0: {}".format(resultado))

resultado = mi_texto[9]
print("Indice 9: {}".format(resultado))

# posicion negativa Ejemplo palabra de 6 letras 0 -5 -4 -3 -2 -1
resultado = mi_texto[-4]
print("Indice -4: {}".format(resultado))

resultado = mi_texto.index("n")
print("Indice de 'n': {}".format(resultado))

resultado = mi_texto.index("prueba")
print("Indice de 'prueba': {}".format(resultado))

resultado = mi_texto.index("a")
print("Indice de primera 'a': {}".format(resultado))

resultado = mi_texto.index("a", 5)
print("Indice de siguiente 'a': {}".format(resultado))

# Rindex busca de derecha a izquierda
resultado = mi_texto.rindex("a")
print("R Indice de 'a': {}".format(resultado))