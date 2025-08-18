# Aplica un Counter (contador) sobre la lista de números entregada a continuación, y almacénalo en una variable llamada contador
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

# Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, se cargue con el string "Valor no hallado".
# Carga el diccionario, al menos, con el siguiente par de datos:     palabra clave = edad     valor = 44
from collections import defaultdict
mi_diccionario = defaultdict(lambda:'Valor no hallado')
mi_diccionario['edad'] = 44

# Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
# Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a continuación.
# La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.
from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
from datetime import date
mi_fecha = date(1999,2,3)

# Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
from datetime import date
hoy = date.today()

# En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
# Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
import datetime
hoy = datetime.datetime.now()
minutos = hoy.minute

# Obtén el logaritmo base 10 del número 25, y almacena el resultado en la variable resultado.
import math
resultado = math.log10(25)

# Obten la raíz cuadrada de pi con la constante math.pi y el método math.sqrt() . Almacena el resultado obtenido en la variable resultado.
resultado = math.sqrt(math.pi)

# Encuentra el factorial de 7 y almacena el resultado en la variable resultado.
resultado = math.factorial(7)

# Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).
# Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
import re

def verificar_email(email):
    patron = r'^\w+@\w+\.com(?:\.[a-z]{2,})?$'  # Se agrega ^ al inicio y $ al final para validar toda la cadena
    if re.match(patron, email):  # Cambiamos search() por match() para que la validación sea estricta
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

# Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra
# "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola",
# debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
import re

def verificar_saludo(frase):
    patron = r"^Hola"
    if re.match(patron,frase):
        print("Ok")
    else:
        print("No has saludado")

# El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a
# continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento
# sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
import re

def verificar_cp(cp):
    patron = r"\w{2}\d{4}"
    if re.match(patron,cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
