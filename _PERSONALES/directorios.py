import os

archivo=open(r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\_PERSONALES\directorios2.txt"
            ,mode="w"
            ,encoding="UTF-8")

anyos=["1994"]
anyos.extend([str(n) for n in range(1998,2000,1)])

for anyo in anyos:

    dir=r"G:\\"+f"{anyo}0000"
    print(f"** Tratando año {anyo} **")
    
    # Recorremos la estructura desde la raíz del proyecto VS Code
    for directorio, subdirectorios, archivos in os.walk(dir):       

        for subdir in subdirectorios:
            archivo.write(f"{os.path.join(directorio,subdir)}\n")