nombre = "Tony Soprano"
edad = 51

#################################################################

nombre = "Julia"
apellido = "Roberts"
nombrecompleto= nombre + " " + apellido

#################################################################

curso = "Python"
print("Estás tomando un curso de " + curso)

#################################################################

num_entero=5
print(type(num_entero))

#################################################################

num_decimal = 8.7
print(type(num_decimal))

#################################################################

num1 = 7.5
num2 = 2.5
print(type(num1+num2))

#################################################################

num1 = 7.5
num2 = int(num1)
print(type(num2))

#################################################################

num2 = 10
num3 = float(num2)
print(type(num3))

#################################################################

num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))

#################################################################

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

#################################################################

puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

#################################################################

puntos_anteriores = 875
puntos_nuevos = 350

print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos, puntos_anteriores+puntos_nuevos))

