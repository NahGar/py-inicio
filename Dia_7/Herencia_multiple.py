class Padre:
    def habla(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja ja")

    def habla(self):
        print("Que tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.habla() # ejecuta de Padre por ser primero en la lista de herencia
mi_nieto.reir()

print(Nieto.__mro__) # orden de resolución de metodos