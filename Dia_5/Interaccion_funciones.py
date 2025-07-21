from random import shuffle

# Lista inicial
palitos = ['-','--','---','----','-----']

# Mezclar palitos
def mezclar_palitos(palitos):
    """Mezcla la lista de palitos."""
    shuffle(palitos)
    return palitos

# pedir intento
def pedir_intento():
    """Pide al usuario que ingrese un intento."""
    intento = ''

    while intento not in ['1', '2', '3', '4', '5']:
        intento = input("Ingresa tu intento de 1 a 5: ")
        if intento.isdigit() and 1 <= int(intento) <= 5:
            return int(intento)

# Comprobar intento
def comprobar_intento(palitos, intento):
    """Compara el intento del usuario con la lista de palitos."""
    print(f"Tu intento: {palitos[intento - 1]}")
    if len(palitos[intento - 1]) == 5:
        print("Elegiste el palito más largo.")
    elif len(palitos[intento - 1]) == 1:
        print("Elegiste el palito más corto.")

palitos_mezclados = mezclar_palitos(palitos)
intento = pedir_intento()
comprobar_intento(palitos_mezclados, intento)
