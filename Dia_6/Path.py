from pathlib import Path

base = Path.home()

print("home:",base)
# path soporta strings y objetos Path
guia = Path(base,"España",Path("Barcelona","Sagrada_Familia.txt"))
print(guia)

print("with_name:",guia.with_name("La_pedrera.txt"))
print("parent:",guia.parent)
print("parent parent:",guia.parent.parent)

guia = Path("/Desarrollo/Personal/Python/inicio/Dia_6")
for txt in Path(guia).glob("*.txt"):
    print(txt)
print("---------------------------------------------")
for txt in Path(guia).glob("**/*.txt"): # busca en subcarpetas
    print(txt)

guia = Path("Desarrollo","Personal","Python")
carpeta = guia.relative_to(Path("Desarrollo","Personal"))
print("relative_to:",carpeta)
