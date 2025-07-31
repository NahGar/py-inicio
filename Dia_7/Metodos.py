class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El {self.especie} {self.color} ha volado {metros} metros")


mi_pajaro = Pajaro('negro','Tucán')
mi_pajaro.piar()
mi_pajaro.volar(50)
