from pathlib import Path, PureWindowsPath

archivo = Path("D:/Desarrollo/Personal/Python/Dia_6/prueba.txt")
print(archivo.read_text(encoding="utf-8"))
print("name:",archivo.name)
print("suffix:",archivo.suffix)
print("stem:",archivo.stem)
if not archivo.exists():
    print("este archivo no existe")
else:
    print("este archivo existe")

ruta_windows = PureWindowsPath(archivo)
print("ruta_windows:",ruta_windows)