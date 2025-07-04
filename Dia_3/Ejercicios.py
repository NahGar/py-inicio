# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[4])

# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))

# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
# Pista: "Controlar" tiene un largo de 9 caracteres.
frase = "Controlar la complejidad es la esencia de la programación"
print( frase[:9] )

# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print( frase[8::3])

# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print( frase[::-1])

# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))

# Reemplaza en la siguiente frase: "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras: "difícil" --> "fácil"     "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil","fácil")
resultado = resultado.replace("mala","buena")
print(resultado)

# Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
print("Repetición" * 15)

# Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
# Tierra mojada, mis recuerdos de viaje entre las lluvias
frase = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("agua" not in frase)

# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
print(len("electroencefalografista"))

# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
mi_lista = [1,'4',0,'hola',5.45]

# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

# Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
# manzana     banana     mango     cereza     sandía
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)