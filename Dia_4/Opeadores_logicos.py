mi_bool = 4 < 5 < 6
print(f" 1) {mi_bool}")

mi_bool = 4 < 5 and 5 > 6
print(f" 2) {mi_bool}")

mi_bool = 1 == 10 or 3 == 3
print(f" 3) {mi_bool}")

texto = "esta frase es un breve"
mi_bool = ("frase" in texto) and ("breve" in texto)
print(f" 4) {mi_bool}")

mi_bool = not ('a' == 'a')
print(f" 5) {mi_bool}")