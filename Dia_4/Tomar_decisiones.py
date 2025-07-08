if 10 > 9:
    print("Es correcto")

x = True
if x:
    print("x es verdadero")

if 5 == 2:
    print("5 es igual a 2")
else:
    print("5 no es igual a 2")

mascota = "perro"
if mascota == "gato":
    print("Es un gato")
elif mascota == "perro":
    print("Es un perro")
else:
    print("No es un gato ni un perro")

edad = 16
calificacion = 9
if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Eres mayor de edad")