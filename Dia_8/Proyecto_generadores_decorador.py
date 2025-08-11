def siguiente_numero_perf():
    num = 0
    while True:
        num += 1
        yield f"P - {num}"

def siguiente_numero_farm():
    num = 0
    while True:
        num += 1
        yield f"F - {num}"

def siguiente_numero_cosm():
    num = 0
    while True:
        num += 1
        yield f"C - {num}"


def decorar_saludo(generador):

    def funcion_decorada():
        print("-" * 50)
        print("Su turno es:")
        print(next(generador))
        print("Aguarde y será atendido")
        print("-" * 50)

    return funcion_decorada