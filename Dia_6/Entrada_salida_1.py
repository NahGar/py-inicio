mi_archivo = open('prueba.txt',encoding='utf-8')

print(mi_archivo)
print("read():"+mi_archivo.read())

mi_archivo.close()

mi_archivo = open('prueba.txt')

una_linea = mi_archivo.readline()
print("readline():"+una_linea.upper())
una_linea = mi_archivo.readline()
print("readline():"+una_linea.rstrip()) # quita CRLF
una_linea = mi_archivo.readline()
print("readline():"+una_linea)

mi_archivo.close()

mi_archivo = open('prueba.txt')

for l in mi_archivo:
    print("for:"+l)

mi_archivo.close()

mi_archivo = open('prueba.txt',encoding='utf-8')

lista_todas = mi_archivo.readlines()
print("readlines():",lista_todas)

mi_archivo.close()
