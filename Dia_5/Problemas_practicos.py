# Ejercicio 1

def devolver_distintos(int1, int2, int3):
    suma = int1 + int2 + int3
    lista = [int1, int2, int3]
    lista.sort(reverse=True)

    if suma > 15:
        return lista[0]
        #return max(lista)
    elif suma < 10:
        return lista[2]
        #return min(lista)
    else:
        return lista[1]

print(devolver_distintos(5,2,9))
print(devolver_distintos(1,2,9))
print(devolver_distintos(1,2,3))

#Ejercicio 2

def palabra_a_letras_sin_repetir(palabra):
    letras = set(palabra)
    lista = list(letras)
    lista.sort()
    print(f"Letras sin repetir: {lista}")

palabra_a_letras_sin_repetir("programacion")

# Ejercicio 3

def existe_cero_consecutivo_en_args(*args):

    cant_ceros = 0
    for arg in args:
        if arg == 0:
            cant_ceros += 1
            if cant_ceros > 1:
                return True
        else:
            cant_ceros = 0
    return False

print(existe_cero_consecutivo_en_args(1, 2, 0, 3, 3, 5))

# Ejercicio 4

def contar_primos(numero_hasta):
    primos = []

    for num in range(2,numero_hasta+1):
        es_primo = True
        for div in range(2, num):
            if num % div == 0 and num != div:
                es_primo = False
                break
        if es_primo:
            primos.append(num)

    print("Primos:", primos)
    return len(primos)

print(contar_primos(150))

"""
def contar_primos(numero):
    
    primos = [2]
    iteracion = 3
    
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        
        for n in range(3,iteracion,2):
            
            if iteracion % n == 0:
                iteracion += 2
                break
            else:
                primos.append(iteracion)
                iteracion += 2
                
    print(primos)
    return len(primos)
"""