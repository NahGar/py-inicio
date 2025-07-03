
texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2]
print("Fragmento 2 : {}".format(fragmento))

fragmento = texto[2:5]
print("Fragmento 2 a 5 : {}".format(fragmento))

fragmento = texto[2:]
print("Fragmento 2 a Final : {}".format(fragmento))

fragmento = texto[:5]
print("Fragmento Inicio a 5 : {}".format(fragmento))

fragmento = texto[2:10:2]
print("Fragmento 2 a 10 (tomando un caracter cada 2) : {}".format(fragmento))

fragmento = texto[::3]
print("Fragmento vacio a vacio (tomando un caracter cada 3) : {}".format(fragmento))

fragmento = texto[::-1] # recorre el texto al reves
print("Fragmento vacio a vacio (tomando un caracter cada -1) : {}".format(fragmento))

fragmento = texto[::-2] # recorre el texto al reves tomando un caracter cada 2
print("Fragmento vacio a vacio (tomando un caracter cada -2) : {}".format(fragmento))