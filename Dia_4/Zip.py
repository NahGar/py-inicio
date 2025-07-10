nombre = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
edades = [20, 22, 19, 21, 23, 20, 22, 99]
ciudades = ["Lima", "Montevideo", "Valencia"]
# El largo es de la lista más corta

combinados = list(zip(nombre, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
