# Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
num1 = 36
num2 = 17
mi_bool = num1 >= num2

# Crea dos variables (num1 y  num2): Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
# Dentro de num2, almacena el número 5. Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 25**0.5
num2 = 5
mi_bool = num1 == num2

# Crea dos variables (num1 y  num2): Dentro de num1, almacena el resultado de la operación 64 x 3
# Dentro de num2, almacena el resultado de la operación 24 x 8. Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 64*3
num2 = 24*8
mi_bool = num1 != num2

# Crea tres variables (num1 ,  num2 y num3): Dentro de num1, almacena el valor 36. Dentro de num2, almacena el resultado de la operación 72/2
# Dentro de num3, almacena el valor 48. Verifica si num1 es mayor que num2, y menor que num3.
# Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 > num3

# Crea tres variables (num1 ,  num2 y num3): Dentro de num1, almacena el valor 36 Dentro de num2, almacena el resultado de la operación 72/2
# Dentro de num3, almacena el valor 48. Verifica si num1 es mayor que num2, o menor que num3.
# Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3

# Verifica si las palabras almacenadas en las siguientes variables: palabra1 = "éxito", y palabra2 = "tecnología"
# no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool =  not palabra1 in frase and not palabra2 in frase