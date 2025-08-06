
def suma():
    n1 = int(input("numero 1:"))
    n2 = int(input("numero 2:"))
    print(n1 + n2)

try:
    # codigo a probar
    suma()
except TypeError:
    print("Error de tipos")
except ValueError:
    print("Error de valor")
except:
    # si hay error
    print("error")
else:
    print("no error")
finally:
    print("ejecuta siempre al final")


def pedir_numero():
    while True:
        try:
            numero = int(input("Escribe un número"))
        except:
            print("Valor incorrecto")
        else:
            break

pedir_numero()