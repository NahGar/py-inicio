from random import choice
from enum import Enum

class Estado_check_letra(Enum):
    YA_USADA = 1
    CORRECTA = 2
    INCORRECTA = 3

class Estado_gano_perdio(Enum):
    GANO = 1
    PERDIO = 2
    SIGUE_JUGANDO = 3

lista_palabras = []
lista_palabras.append("Automovil")
lista_palabras.append("Escalera")
lista_palabras.append("Ladrillo")
lista_palabras.append("Computadora")
lista_palabras.append("Celular")
lista_palabras.append("Mesa")
lista_palabras.append("Silla")
lista_palabras.append("Ventana")
lista_palabras.append("Puerta")
lista_palabras.append("Teclado")
lista_palabras.append("Monitor")
lista_palabras.append("Bandera")
lista_palabras.append("Cama")

def pedir_letra():
    salir = False
    while not salir:
        letra = input("Ingrese una letra: ").upper()

        if validar_letra(letra):
            salir = True
        else:
            print("Debe ingresar una letra del abecedario")

    return letra

def validar_letra(letra):
    if letra == "" or len(letra) > 1:
        return False
    elif "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".find(letra) != -1:
        return True
    else:
        return False

def check_letra(letra, palabra_juego, lista_letras_usadas, letras_acertadas):

    if letra in lista_letras_usadas:
        print("Ya has usado esa letra")
        return Estado_check_letra.YA_USADA

    lista_letras_usadas.append(letra.upper())

    index = 0
    existe_letra = False
    for letra_juego in palabra_juego:
        if letra_juego == letra:
            letras_acertadas[index] = letra
            existe_letra = True

        index += 1

    if existe_letra:
        print("Letra Correcta")
        return Estado_check_letra.CORRECTA
    else:
        print("Letra Incorrecta")
        return Estado_check_letra.INCORRECTA

def gano_perdio(cantidad_vidas, letras_acertadas):

    if cantidad_vidas <= 0:
        return Estado_gano_perdio.PERDIO
    else:
        if letras_acertadas.count("_") == 0:
            return Estado_gano_perdio.GANO

    return Estado_gano_perdio.SIGUE_JUGANDO

def imprime_avance(letras_acertadas,cantidad_vidas, lista_letras_usadas):
    print(" ".join(letras_acertadas))

    print(f"Vidas restantes: {cantidad_vidas}")
    print(f"Letras utilizadas: {" ".join(lista_letras_usadas)}")



def jugar():
    cantidad_vidas = 6
    palabra_juego = choice(lista_palabras).upper()

    letras_palabra = []
    letras_acertadas = []

    for letra in palabra_juego:
        letras_palabra.append(letra)
        letras_acertadas.append("_")

    lista_letras_usadas = []

    imprime_avance(letras_acertadas, cantidad_vidas, lista_letras_usadas)

    fin_juego = False
    while not fin_juego:
        letra = pedir_letra()
        estado_ckeck = check_letra(letra,palabra_juego,lista_letras_usadas,letras_acertadas)
        if estado_ckeck == Estado_check_letra.INCORRECTA:
            cantidad_vidas -= 1

        estado_gano_perdio = gano_perdio(cantidad_vidas,letras_acertadas)
        if estado_gano_perdio == Estado_gano_perdio.PERDIO:
            fin_juego = True
            print(f"Ha perdido, la palabra era {palabra_juego}")
        elif estado_gano_perdio == Estado_gano_perdio.GANO:
            fin_juego = True
            print(f"Ha acertado la palabra")

        imprime_avance(letras_acertadas,cantidad_vidas, lista_letras_usadas)

jugar()