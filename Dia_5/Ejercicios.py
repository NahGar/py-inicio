# Remueve los caracteres a la izquierda de nuestro texto principal:
#  , :  % _  #   Utiliza el método lstrip(). Imprime el resultado en pantalla:
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando el método insert():
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")

# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"
def saludar():
    print("¡Hola mundo!")

# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
nombre_persona = "Pepe"

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")


# Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.
un_numero = 2

def cuadrado(un_numero):
    print(un_numero * un_numero)

# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente

def potencia(num1,num2):
    return num1 ** num2

# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.
dolares = 3

def usd_a_eur(dolares):
    return dolares * 0.90

# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.
# Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
# También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.
palabra = "palabra"

def invertir_palabra(palabra):
    letrasAlReves = list(palabra)
    letrasAlReves.reverse()
    return ''.join(letrasAlReves).upper()

# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.
lista_numeros = [8, 5, 9]

def todos_positivos(lista_numeros):
    for num in lista_numeros:
        if num < 0:
            return False

    return True

# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y
# cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
lista_numeros = [-5, 5, 800]

def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma += numero

    return suma

print(suma_menores(lista_numeros))

# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros),
# y devuelva el resultado de dicha cuenta.
lista_numeros = [9, 5, 4, 7, 6, 2]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for num in lista_numeros:
        if num % 2 == 0:
            cantidad += 1
    return cantidad

print(cantidad_pares(lista_numeros))

# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
#     La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
#     Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
# Si la suma es menor o igual a 6: "La suma de tus dados es {suma_dados}. Lamentable"
# Si la suma es mayor a 6 y menor a 10: "La suma de tus dados es {suma_dados}. Tienes buenas chances"
# Si la suma es mayor o igual a 10: "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
from random import randint, choice


def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1, dado2)

def evaluar_jugada(dado1, dado2):
    # suma = sum(tuple_dados)
    suma = dado1 + dado2
    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif suma > 6 and suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    elif suma >= 10:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

tuple_dados = lanzar_dados()

print(evaluar_jugada(tuple_dados[0],tuple_dados[1]))

# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.
# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
lista_numeros = [1, 2, 15, 7, 2, 8, 12, 4]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    return sum(lista) / len(lista)

sin_repetidos = reducir_lista(lista_numeros)
print(promedio(sin_repetidos))

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
#   Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
#   Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
from random import choice

lista_numeros = [1, 2, 15, 7, 2, 8, 12, 4]
def lanzar_moneda():
    return choice(["Cara", "Cruz"])

def probar_suerte(valor_moneda, lista):

    if valor_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista

# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
def suma_cuadrados(*args):
    return sum(num ** 2 for num in args)

print(suma_cuadrados(1,2,3))

# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos
# (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos)
def suma_absolutos(*args):
    suma = 0
    for numero in args:
        suma += numero if numero > 0 else numero * -1
    return suma


# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
# La función debe devolver el siguiente mensaje: "{nombre}, la suma de tus números es {suma_numeros}"
def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus números es {sum(args)}"


