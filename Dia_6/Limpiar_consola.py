from os import system

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# para que se funcione en la terminal hay que configurar Emulate terminal in output console
system("cls")

print(f"Tu nombre es {nombre} y tienes {edad} años")