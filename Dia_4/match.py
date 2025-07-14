serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No se ha encontrado la serie")

# Utilizando match
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No se ha encontrado la serie")


cliente = {'nombre': 'Juan', 'edad': 30, 'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix', 'ficha_tecnica': {'protagonista':'Keanu Reeves', 'director': 'Lana Wachowski y Lilly Wachowski'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print("Es cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print("Es pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es")