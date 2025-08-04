# Crea una clase llamada Personaje y a continuación, crea un objeto a partir de ella, por ejemplo: harry_potter
class Personaje:
    pass

harry_potter = Personaje()

# Crea una clase llamada Dinosaurio, y tres instancias a partir de ella: velociraptor, tiranosaurio_rex y braquiosaurio
class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio  = Dinosaurio()

# Crea una clase llamada PlataformaStreaming y crea los siguientes objetos a partir de ella: netflix, hbo_max, amazon_prime_video
class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)

# Crea una clase llamada Cubo, y asígnale el atributo de clase: caras = 6 y el atributo de instancia: color
# Crea una instancia cubo_rojo, de dicho color.
class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:   real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia: especie = "Humano"  magico = True  edad = 17
class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)

# Crea una clase Perro. Dicho perro debe poder ladrar. Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".
class Perro:

    def ladrar(self):
        print("Guau!")

mi_perro = Perro()
mi_perro.ladrar()

# Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

# Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"
class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

# Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

#Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.
class Mascota:

    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

#Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

# La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.
# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objetos = [palabra,lista,tupla]
for obj in objetos:
    print(len(obj))

# Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.
# Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()
personajes = [arquero1, mago1, samurai1]

for personaje in personajes:
    personaje.atacar()

# Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
# Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

# Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

# Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")





