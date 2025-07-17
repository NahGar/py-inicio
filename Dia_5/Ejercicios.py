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