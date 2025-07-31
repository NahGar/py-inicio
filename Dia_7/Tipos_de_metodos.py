class Pajaro:

    alas = True

    # metodos de instancia
    # acceden y modifican atributos del objeto, accede a otros métodos, modifica el estado de la clase
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El {self.especie} {self.color} ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"El {self.especie} es de color {self.color}")

    # metodos de clase
    # no necesitan instanciarse, no acceden a los atributos de instancia (color, especie), si atributo de clase (alas)
    # no puede acceder a metodos de instancia
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    # metodos estaticos
    # no acceden a la clase ni a la instancia
    @staticmethod
    def mirar():
        print("El pajaro mira")


mi_pajaro = Pajaro('amarillo','canario')
mi_pajaro.pintar_negro()
mi_pajaro.volar(20)
#mi_pajaro.alas = False # modifica el estado de la clase
#print(mi_pajaro.alas)
Pajaro.poner_huevos(3)
Pajaro.mirar()
