precios_cafe = [('capuchino', 1.5), ('espresso', 2.0), ('latte', 2.5), ('americano', 1.8)]

for cafe, precio in precios_cafe:
    print(f"El precio del {cafe} es ${precio}.")


def cafe_mas_caro(lista_precios):
    precio_mas_caro = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precios:
        if precio > precio_mas_caro:
            precio_mas_caro = precio
            cafe_mas_caro = cafe

    return (cafe_mas_caro, precio_mas_caro)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es {cafe} a un precio de ${precio}.")