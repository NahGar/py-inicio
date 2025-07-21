
def suma(a, b):
    return a + b

print(suma(5,6))

def suma_args(*args):
    #resultado = 0
    #for num in args:
    #    resultado += num
    #return resultado
    return sum(args)

print(suma_args(1, 2, 3, 4, 5))