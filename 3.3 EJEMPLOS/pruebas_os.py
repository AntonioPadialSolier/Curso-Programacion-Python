import os

# Recorremos la estructura desde la raíz del proyecto VS Code
for directorio, subdirectorios, archivos in os.walk(r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src"):

    # En cada bucle os.walk devuelve

    # Directorio en el que estamos
    print(f"Directorio: {directorio}")

    # Subdirectorios (que os.walk irá recorriendo en orden)
    print(f"\t> Subdirectorios: {subdirectorios}")

    # Archivos
    print(f"\t* Archivos:")
    for archivo in archivos:
        print(f"\t\t> {os.path.join(directorio,archivo)}")