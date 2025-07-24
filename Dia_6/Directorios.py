import os
from pathlib import Path

from Dia_6.Entrada_salida_1 import mi_archivo

# getcwd() directorio actual
print("getcwd:",os.getcwd())
# cambia el directorio actual
ruta = os.chdir("D:\\Desarrollo\\Personal\\Python\\Dia_6\\otra_carpeta")

archivo = open('documento.txt')
print(archivo.read())

# crea carpeta
dir = "D:\\Desarrollo\\Personal\\Python\\Dia_6\\otra_carpeta2"
if not os.path.exists(dir):
    os.makedirs(dir)

# elimina carpeta
os.rmdir(dir)

ruta = 'D:\\Desarrollo\\Personal\\Python\\Dia_6\\otra_carpeta\\documento.txt'
print("basename:",os.path.basename(ruta)) #nombre archivo
print("dirname:",os.path.dirname(ruta)) #nombre directorio
elemento = os.path.split(ruta)
print(f"split: dir {elemento[0]} arch {elemento[1]}")

# para usar rutas que funcionen en todos los SO
archivo = Path("/Desarrollo/Personal/Python/Dia_6/otra_carpeta") / 'documento.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())