# Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.
def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")


# Implementa para la siguiente función cociente(), un manejador de errores:
# Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"
# Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"
# En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) entre los dos números entregados como argumento.
def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


# Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():
# En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"
# En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
# Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
# En todos los casos, al finalizar, imprimir: "Finalizando ejecución"
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

# Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.
def mi_generador():
    x = 0
    while True:
        x += 1
        yield x

generador = mi_generador()

# Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
def mi_generador():
    x = 0
    while True:
        x += 7
        yield x

generador = mi_generador()

# Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
# "Te quedan 3 vidas" "Te quedan 2 vidas" "Te queda 1 vida" "Game Over" Almacena el generador en la variable perder_vida
def mi_generador():
    vidasMax = 3
    for vidas in range(vidasMax, -1, -1):
        if vidas == 0:
            yield "Game Over"
        else:
            str_vida = "vida" if vidas == 1 else "vidas"
            str_queda = "queda" if vidas == 1 else "quedan"
            yield f"Te {str_queda} {vidas} {str_vida}"

perder_vida = mi_generador()














