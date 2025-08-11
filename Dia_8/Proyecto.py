
from Proyecto_generadores_decorador import *

def seleccion_area():
    while True:
        try:
            print("Perfumería (P), Farmacia (F), Cosmética (C)")
            area = input("Seleccione un área: ").upper()
            if area == "P":
                return "perfumería"
            elif area == "F":
                return "farmacia"
            elif area == "C":
                return "cosmética"
            else:
                print("Área incorrecta")
        except:
            print("Ocurrió un error")


def inicio():

    gen_perf = siguiente_numero_perf()
    gen_farm = siguiente_numero_farm()
    gen_cosm = siguiente_numero_cosm()

    while True:
        area = seleccion_area()
        siguiente_numero_decorado = None

        if area == "perfumería":
            siguiente_numero_decorado = decorar_saludo(gen_perf)
        elif area == "farmacia":
            siguiente_numero_decorado = decorar_saludo(gen_farm)
        elif area == "cosmética":
            siguiente_numero_decorado = decorar_saludo(gen_cosm)

        siguiente_numero_decorado()


inicio()




