
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    # atributo nuevo en el hijo
    def __init__(self, edad, color, altura_vuelo):
        #self.edad = edad
        #self.color = color
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    # sobrescribe
    def hablar(self):
        print("Pio")
    # metodo del hijo
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")


print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolin = Pajaro(2,'amarillo',20)
piolin.nacer()
print(piolin.color)

piolin.hablar()
piolin.volar(50)