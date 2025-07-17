def chequear_3_cifras(lista):
    for num in lista:
        if 100 <= num < 1000:
            return True
        # else:
        #    pass
    return False


def chequear_3_cifras2(lista):

    lista_3_cifras = []

    for num in lista:
        if 100 <= num < 1000:
            lista_3_cifras.append(num)
        #else:
        #    pass
    return lista_3_cifras

resultado = chequear_3_cifras([44,939,6000])
print(f"Hay número de 3 cifras: {resultado}")

resultado = chequear_3_cifras2([446,939,6000,5])
print(f"Hay número de 3 cifras: {resultado}")