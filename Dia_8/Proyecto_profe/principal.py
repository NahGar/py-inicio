import numeros

def preguntar():
    print("Bienvenido a farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():

    flag_Preguntar = True
    while True:
        if flag_Preguntar:
            flag_Preguntar = False
            preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? S/N: ").upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                break
            elif otro_turno == "S":
                flag_Preguntar = True


inicio()