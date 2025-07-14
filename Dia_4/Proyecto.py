from random import randint
cantidad_intentos = 8
intentos = 0
nombre = input("Cuál es tu nombre?")
print("Hola, " + nombre + "! Bienvenido al programa.")
print(f"Tienes {cantidad_intentos} para adivinar un número entre 1 y 100.")

numeroSecreto = randint(1, 100)

while cantidad_intentos > 0:
    numero = int(input("Adivina el número: "))
    intentos += 1

    '''if numero == numeroSecreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif numero < 1 or numero > 100:
        print("El número debe estar entre 1 y 100. Inténtalo de nuevo.")
    elif numero < numeroSecreto:
        cantidad_intentos -= 1
        print("El número es mayor. Te quedan " + str(cantidad_intentos) + " intentos.")
    elif numero > numeroSecreto:
        cantidad_intentos -= 1
        print("El número es menor. Te quedan " + str(cantidad_intentos) + " intentos.")
    '''

    match numero:
        case x if x == numeroSecreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        case x if x < 1 or x > 100:
            print("El número debe estar entre 1 y 100. Inténtalo de nuevo.")
        case x if x < numeroSecreto:
            cantidad_intentos -= 1
            print("El número es mayor. Te quedan " + str(cantidad_intentos) + " intentos.")
        case x if x > numeroSecreto:
            cantidad_intentos -= 1
            print("El número es menor. Te quedan " + str(cantidad_intentos) + " intentos.")

    if cantidad_intentos == 0:
        print("Lo siento, no te quedan más intentos. El número era " + str(numeroSecreto) + ".")

