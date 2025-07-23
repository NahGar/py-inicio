archivo = open("prueba1.txt",'w')

archivo.write('nuevo texto1\n')
archivo.write('nuevo texto2\n')

archivo.close()

archivo = open("prueba1.txt",'a')

archivo.write('''nuevo texto3
nuevo texto4
''')

archivo.close()

archivo = open("prueba1.txt",'a')

# escribe en una única linea
archivo.writelines(['hola','que','tal'])

archivo.close()