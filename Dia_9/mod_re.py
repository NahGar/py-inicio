'''
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
'''
