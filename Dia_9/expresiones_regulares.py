r'''
car         desc                        ejemplo         match
/d          digito numérico             v\d.\d\d        v1.02
/w          caracter alfanumérico       \w\w-\w\w       a1-b9
/s          espacio en blanco           num\s\d\d       num 12
/D          NO digito numérico          v\D.\D\D        va.bc
/W          NO caracter alfanumérico    \W\W-\W\W       ##-$$
/S          NO espacio en blanco        num\S\D\D       num1ab
+           1 o más veces               cod\d-\d+       cod1-58245
{n}         se repite n veces           \d-\d{4}        1-6985
{n.m}       se repite de n a m veces    \w{3,5}         hola o sol o mundo
{n.}        se repite n o más veces     -\d{4,}-        -1234- o -213434234234-
*           0 o más veces               \w\s*\w         ab o a        b
?           1 o 0 veces                 casas?          casa o casas
|           OR                          lunes|martes    lunes
.           cualquier caracter          ..jo            rojo antojo
^           al comienzo del string      ^\d             comienza con un número
$           al final del string         \d$             termina con un número
[]          excluye                     [^\s]           excluye los espacios
'''

import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = "nada"
busqueda = re.search(patron,texto)
print(f"No existe nada:{busqueda}")

patron = "ayuda"
busqueda = re.search(patron,texto)
print(f"Existe ayuda:{busqueda}")
print(f"Span ayuda:{busqueda.span()}")
print(f"Start ayuda:{busqueda.start()}")
print(f"End ayuda:{busqueda.end()}")

patron = "ayuda"
busqueda = re.findall(patron,texto)
for hallazgo in re.finditer(patron,texto):
    print(f"Cada ayuda:{hallazgo.span()}")

texto = 'Llama al 564-525-6588 o al 444-333-5555 ya mismo'
#patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron,texto)
print(resultado)
print(f"group:{resultado.group()}")

resultado = re.findall(patron,texto)
for r in resultado:
    print("cada resultado:"+r)

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron,texto)
print(f"group compile:{resultado.group(1)} {resultado.group(2)} {resultado.group(3)}")

clave = input("Clave: ")
patron = r'\D{1}\w{7}' # primer caracter es una letra, y 7 caracteres más

chequear = re.search(patron,clave)
print(chequear)

texto = 'No atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes',texto)
print(buscar)

buscar = re.search(r'demos',texto)
print(buscar)

buscar = re.search(r'....demos',texto)
print(buscar)

buscar = re.search(r'demos.',texto)
print(buscar)

buscar = re.search(r'^\D.',texto)
print(buscar)

buscar = re.search(r'\D$',texto)
print(buscar)

buscar = re.findall(r'[^\s]',texto)
print(buscar)
