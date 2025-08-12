import os

def crear_archivo(nombre):
    archivo = open(nombre, 'w')
    archivo.write('texto de pruebas')
    archivo.close()

print(os.getcwd())

# for arch in os.walk(".\\"):
#    print("walk:",arch)

for carp, subcar, archs in os.walk("..\\"):
    print(f"En la carpeta {carp} las subcarpetas son:")
    for sub in subcar:
        print(f"\t{sub}")
    print('Los archivos son:')
    for arch in archs:
        print(f"\t{arch}")
    print("\n")



crear_archivo('curso.txt')

print(os.listdir())

import shutil

os.makedirs("auxiliar")

# mover archivo
shutil.move('curso.txt','.\\auxiliar')

# elimina carpeta y contenido y no va a la papelera
shutil.rmtree('.\\auxiliar')

import send2trash

crear_archivo('curso1.txt')
# mueve a papelera
send2trash.send2trash('curso1.txt')


