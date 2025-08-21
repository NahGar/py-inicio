import zipfile

# comprimir
nombre_archivo = "archivo_comprimido.zip"
mi_zip = zipfile.ZipFile(nombre_archivo,"w")
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()

# descomprimir
zip_abierto = zipfile.ZipFile(nombre_archivo,'r')
zip_abierto.extractall()

# Extraer un archivo a la ubicación actual
# zip_abierto.extract('archivo1.txt')

# Extraer a una ruta específica
# zip_abierto.extract('carpeta/archivo2.txt', 'extracciones/')

import shutil

carpeta_origen = 'D:\\Desarrollo\\Personal\\Python\\inicio\\Dia_9\\carpeta_comprimir'
archivo_destino = 'shutil_comprimido'
shutil.make_archive(archivo_destino,'zip',carpeta_origen)

shutil.unpack_archive(archivo_destino + ".zip",'shutil_extract', 'zip')

