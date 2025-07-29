from pathlib import Path
import os
import shutil

directorio_script = Path(__file__).resolve().parent
path_recetas = Path(directorio_script, "proyecto", "recetas")
path_recetas_absoluto = str(path_recetas.absolute())

def elegir_menu():
    print("[1] - leer receta") # pide categoría, muestra recetas, pide receta, muestra receta
    print("[2] - crear receta") # pide categoría, pide nombre y contenido, crea archivo
    print("[3] - crear categoría") # pide nombre de categoría, crea carpeta
    print("[4] - eliminar receta") # pide categoría, muestra recetas, pide receta, elimina
    print("[5] - eliminar categoría") # pide categoría, elimina
    print("[6] - finalizar programa")
    while True:
        opcion = input("Elige una opción:")
        if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= 6:
            return opcion
        else:
            print("Opción incorrecta")

def elegir_categoria():

    dic_categorias = carga_categorias()
    for key, value in dic_categorias.items():
        print(f"[{key}] - {value[0]}")

    print(f"[{len(dic_categorias)+1}] - cancelar")

    while True:
        opcion = input("Elige una opción:")
        if int(opcion) >= 1 and int(opcion) <= len(dic_categorias):
            for key, value in dic_categorias.items():
                if key == int(opcion):
                    return True, value
        elif int(opcion) == len(dic_categorias)+1:
            return False, ()
        else:
            print("Opción incorrecta")

def elegir_receta(categoria):

    dic_recetas = carga_recetas(categoria)
    for key, value in dic_recetas.items():
        print(f"[{key}] - {value[0]}")

    print(f"[{len(dic_recetas) + 1}] - cancelar")

    while True:
        opcion = input("Elige una opción:")
        if int(opcion) >= 1 and int(opcion) <= len(dic_recetas):
            for key, value in dic_recetas.items():
                if key == int(opcion):
                    return True, value
        elif int(opcion) == len(dic_recetas)+1:
            return False, ()
        else:
            print("Opción incorrecta")

def carga_categorias():

    dic_categorias = {}

    # Obtener solo carpetas (directorios)
    carpetas = [carpeta for carpeta in path_recetas.iterdir() if carpeta.is_dir()]

    contador = 1
    for carpeta in carpetas:  # busca en subcarpetas
        dic_categorias[contador] = (carpeta.name, carpeta)
        contador += 1
    return dic_categorias

def carga_recetas(categoria):
    dic_recetas = {}
    contador = 1
    for txt in Path(categoria).glob("**/*.txt"):  # busca en subcarpetas
        nombre_archivo = txt.stem
        #path_archivo = txt.resolve()
        dic_recetas[contador] = (nombre_archivo, txt)
        contador += 1
    return dic_recetas

def crea_receta(categoria):
    print("Ingrese nombre de la receta:")
    nombre = input()
    nombre = nombre.replace(" ", "_") + ".txt"
    print("Ingrese receta:")
    contenido = input()
    path_archivo = Path(categoria[1], nombre)
    if not path_archivo.exists():
        # archivo = open(path_archivo, "w")
        # archivo.write(contenido)
        path_archivo.write_text(contenido)
        print("Receta generada")
    else:
        print("La receta ya existe")

def crea_categoria():
    nombre = input("Ingrese nombre de la categoría:")
    if nombre == "":
        print("Debe indicar un nombre")
        return

    nombre = nombre.replace(" ", "_")

    dir = Path(path_recetas,nombre)
    if not os.path.exists(dir):
        os.makedirs(dir)
        print("Categoría creada")
    else:
        print("Ya existe esa categoría")

def elimina_categoria(categoria):

    dic_recetas = carga_recetas(categoria[1])
    if len(dic_recetas) == 0:
        os.rmdir(categoria[1])
        print("Categoría eliminada")
    else:
        eliminar = input("La categoría contiene recetas. Desea eliminar de todas formas (s/n)?")
        if eliminar.lower() == "s":
            shutil.rmtree(categoria[1])
            print("Categoría eliminada")

def contar_recetas():
    contador = 0
    for txt in Path(path_recetas).glob("**/*.txt"):  # busca en subcarpetas
        contador += 1
    return contador


# Programa
while True:
    # para que se funcione en la terminal hay que configurar Emulate terminal in output console
    os.system("cls")
    print("-" * 50)
    print("Bienvenido al administrador de recetas")
    print("-" * 50)
    print("Las recetas están en: " + path_recetas_absoluto)

    print(f"Total recetas: {contar_recetas()}")

    opcionMenu = elegir_menu()
    match opcionMenu:
        case "1": # pide categoría, muestra recetas, pide receta, muestra receta
            seguir, opcion_categoria =  elegir_categoria()
            if seguir:
                seguir, opcion_receta = elegir_receta(opcion_categoria[1])
            if seguir:

                # archivo = open(opcion_receta[1])
                # print(f"Receta: {archivo.read()}")
                print(f"Receta: {Path.read_text(opcion_receta[1])}")
                input("Presione cualquier tecla para continuar")

        case "2": # pide categoría, pide nombre y contenido, crea archivo
            seguir, opcion_categoria = elegir_categoria()
            if seguir:
                crea_receta(opcion_categoria)
                input("Presione cualquier tecla para continuar")

        case "3": # pide nombre de categoría, crea carpeta
            crea_categoria()
            input("Presione cualquier tecla para continuar")

        case "4": # pide categoría, muestra recetas, pide receta, elimina
            seguir, opcion_categoria = elegir_categoria()
            if seguir:
                seguir, opcion_receta = elegir_receta(opcion_categoria[1])
            if seguir:
                os.remove(opcion_receta[1])
                print("Receta eliminada")
                input("Presione cualquier tecla para continuar")

        case "5": # pide categoría, elimina
            seguir, opcion_categoria = elegir_categoria()
            if seguir:
                elimina_categoria(opcion_categoria)
                input("Presione cualquier tecla para continuar")
        case "6":
            break;

