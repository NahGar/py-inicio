# Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
num1 = 36
num2 = 17
mi_bool = num1 >= num2

# Crea dos variables (num1 y  num2): Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
# Dentro de num2, almacena el número 5. Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2

# Crea dos variables (num1 y  num2): Dentro de num1, almacena el resultado de la operación 64 x 3
# Dentro de num2, almacena el resultado de la operación 24 x 8. Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2

# Crea tres variables (num1 ,  num2 y num3): Dentro de num1, almacena el valor 36. Dentro de num2, almacena el resultado de la operación 72/2
# Dentro de num3, almacena el valor 48. Verifica si num1 es mayor que num2, y menor que num3.
# Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 > num3

# Crea tres variables (num1 ,  num2 y num3): Dentro de num1, almacena el valor 36 Dentro de num2, almacena el resultado de la operación 72/2
# Dentro de num3, almacena el valor 48. Verifica si num1 es mayor que num2, o menor que num3.
# Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3

# Verifica si las palabras almacenadas en las siguientes variables: palabra1 = "éxito", y palabra2 = "tecnología"
# no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool =  not palabra1 in frase and not palabra2 in frase

# Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):
# Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
# "num1 es mayor que num2"     "num2 es mayor que num1"     "num1 y num2 son iguales"
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

# Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.
# Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:
#     "Puedes conducir"   "No puedes conducir aún. Debes tener 18 años y contar con una licencia"   "No puedes conducir. Necesitas contar con una licencia"
edad = 16
tiene_licencia = False

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

# Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
# Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
# "Cumples con los requisitos para postularte" "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
# "Para postularte, necesitas tener conocimientos de inglés"  "Para postularte, necesitas saber programar en Python"
habla_ingles = True
sabe_python = False

if habla_ingles:
    if sabe_python:
        print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas saber programar en Python")
else:
    if sabe_python:
        print("Para postularte, necesitas tener conocimientos de inglés")
    else:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

# Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"Hola {alumno}")

# Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la
# suma en una variable llamada suma_numeros
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero

# Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables
# suma_pares y suma_impares respectivamente
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero


# Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

# Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
# - Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
# - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
numero = 50

while numero >= 0:

    if numero % 5 == 0:
        print(numero)

    numero -= 1

# Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el
# momento que encuentres un valor negativo:
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)

# Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(2500, 2586))

# Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde
# el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(3,301,3))

# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado
# en una variable llamada suma_cuadrados. Para ello:
# Crea un rango de valores que puedas recorrer en un loop. Para cada uno de estos valores, calcula su valor al cuadrado
# (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional). Suma todos los valores al cuadrado
# obtenidos. Acumula la suma en la variable suma_cuadrados.
suma_cuadrados = 0

lista_numeros = list(range(1, 16))

for numero in lista_numeros:
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado


# Imprime en pantalla frases como la siguiente: '{nombre} se encuentra en el índice {indice}'
# Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

mi_tupple = list(enumerate(lista_nombres))
for indice, nombre in mi_tupple:
    print(f'{nombre} se encuentra en el índice {indice}')

# Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".
# Llama a la lista obtenida con el nombre de variable lista_indices
letras = list("Python")
lista_indices = list(enumerate(letras))

# Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre[0].lower() == "m":
        print(indice)

# Muestra en pantalla frases como la del siguiente ejemplo: La capital de Alemania es Berlín
# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

lista = list(zip(capitales,paises))
for capital,pais in lista:
    print(f"La capital de {pais} es {capital}")

# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ['Adidas','Pepsi','Lays']
productos = ['Camiseta','Refresco','Papas fritas']
mi_zip = zip(marcas,productos)

# Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
# [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
numEsp = ['uno','dos','tres','cuatro','cinco']
numPor = ['um','dois','três','quatro','cinco']
numEng = ['one','two','three','four','five']
numeros = list(zip(numEsp,numPor,numEng))

# Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

# Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)

# Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
# Almacena dicho valor en una variable llamada edad_minima.
# También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)

# Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
from random import randint
aleatorio = randint(1,10)

# Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio
from random import random
aleatorio = random()

# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.
from random import choice
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)

# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]

# Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]

# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:
# °C = (°F - 32) * (5/9)
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(valor - 32) * (5/9) for valor in temperatura_fahrenheit]