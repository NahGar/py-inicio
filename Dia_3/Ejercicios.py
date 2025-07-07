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

# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#     nombre: Karen     apellido: Jurgens     edad: 35     ocupacion: Periodista
# Los nombres de las claves y valores deben ser iguales a la consigna.
mi_dic = {'nombre':'Karen', 'apellido':'Jurgens', 'edad':35, 'ocupacion':'Periodista'}

# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

# Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#      nombre: Karen     apellido: Jurgens     edad: 36     ocupacion: Editora     pais: Colombia
# para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'

# Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

# Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

# Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla

# Une los siguientes sets en uno solo, llamado mi_set_3:
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

# Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

# Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")

# Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
print(17834/34 > 87*56)

# Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()
print(25**0.5 == 5)

