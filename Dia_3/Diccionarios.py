diccionario = {'c1': 'valor1', 'c2': 'valor2', 'c3': 'valor3'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(f"El valor de 'c1' es: {resultado}")

cliente = {'nombre': 'Pepe', 'apellido': 'Mujica', 'edad': 30, 'activo': True, 'peso': 80, 'altura': 1.75 }
consulta = cliente['apellido']
print(f"El apellido es: {consulta}")

dic = {'c1': 55, 'c2': [10,20,30], 'c3': {'s1': 100, 's2': 200}}
print(f" ['c2'][1]: {dic['c2'][1]}")
print(f" ['c3']['s2']: {dic['c3']['s2']}")

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d','e','f']}
print(f" imprimo la letra e mayúscula: {dic['c2'][1].upper()}")

dic = {1: 'a', 2: 'b'}
dic[3] = 'c'
print(f" agregar a dic {dic}")
dic[2] = 'B'
print(f" sobreescribir dic {dic}")

print(f" dic keys {dic.keys()}")
print(f" dic values {dic.values()}")
print(f" dic items {dic.items()}")