# Abre el archivo texto.txt e imprime su contenido. Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
archivo = open("texto.txt")
print(archivo.read())
archivo.close()

# Imprime la primera línea del archivo texto.txt. No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
archivo = open("texto.txt")
print(archivo.readline())
archivo.close()

# Abre el archivo texto.txt e imprime únicamente la segunda línea.
archivo = open("texto.txt")
lista_contenido = archivo.readlines()
print(lista_contenido[1])
archivo.close()

# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
archivo = open("mi_archivo.txt","w")
archivo.write("Nuevo texto")
archivo.close()

archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()

# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()

archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()


# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# Imprime el contenido completo de "registro.txt" al finalizar.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("registro.txt", "a")
for r in registro_ultima_sesion:
    archivo.writelines(r + "\t")

archivo.close()

archivo = open("registro.txt")
print(archivo.read())
archivo.close()

# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
from pathlib import Path
ruta_base = Path.home()

# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
#from pathlib import Path

ruta = Path("Curso Python","Día 6","practicas_path.py")

# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas
#from pathlib import Path

ruta = Path(Path.home(),"Curso Python","Día 6","practicas_path.py")






