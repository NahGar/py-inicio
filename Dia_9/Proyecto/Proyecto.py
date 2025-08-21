import shutil
import os
import re
import datetime
import time
import math
from pathlib import Path

from Dia_9.medir_tiempo import duracion

# shutil.unpack_archive("Proyecto+Dia+9.zip",'instrucciones', 'zip')

"""
----------------------------------------------------
Fecha de búsqueda: [fecha de hoy]

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

[N] + [tres carateres de texto] + [-] + [5 números]  Por ejemplo: Nryu-12365
"""

patron_numero_serie = r'N\w{3}-\d{5}'

def recorrer_carpeta(carpeta):
    lista_archivos = []
    lista_busquedas = []
    for carp, subcarpetas, archs in os.walk(carpeta):
        for arch in archs:
            archivo_actual = open(Path(carp,arch), 'r')
            contenido = archivo_actual.read()
            busqueda = re.search(patron_numero_serie,contenido)
            if not busqueda == None:
                lista_archivos.append(arch.title())
                lista_busquedas.append(busqueda)
            archivo_actual.close()

    return  lista_archivos, lista_busquedas


inicio = time.time()

lista_archivos, lista_busquedas = recorrer_carpeta("instrucciones\\Mi_Gran_Directorio")

fin = time.time()
duracion = math.ceil(fin-inicio)

print("----------------------------------------------------")
fecha_actual = datetime.date.today()
fecha_formateada = fecha_actual.strftime("%d/%m/%y")
print(f"Fecha de búsqueda: {fecha_formateada}")
print("\n")
print("ARCHIVO\t\t\tNRO. SERIE")
print("-------\t\t\t----------")
for i in range(len(lista_archivos)):
    print(f"{lista_archivos[i]}\t{lista_busquedas[i].group()}")

print("\n")
print(f"Números encontrados: {len(lista_archivos)}")
print(f"Duración de la búsqueda: {duracion} segundos")

print("----------------------------------------------------")
