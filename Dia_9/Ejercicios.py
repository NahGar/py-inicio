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



