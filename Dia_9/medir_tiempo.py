import time
import timeit

def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

# time
inicio = time.time()
prueba_while(1000000)
fin = time.time()
print("tiempo",fin-inicio)

inicio = time.time()
prueba_for(1000000)
fin = time.time()
print("tiempo",fin-inicio)

# timeit
mi_declaracion = """
prueba_for(10)
"""
mi_setup = """
def prueba_for(numero):
    lista = []
    for num in range(1,numero+1):
        lista.append(num)
    return lista
"""

# se ejecuta 100000 veces
duracion = timeit.timeit(mi_declaracion,mi_setup,number=100000)
print(duracion)

mi_declaracion2 = """
prueba_while(10)
"""
mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion2 = timeit.timeit(mi_declaracion2,mi_setup2,number=100000)
print(duracion2)



