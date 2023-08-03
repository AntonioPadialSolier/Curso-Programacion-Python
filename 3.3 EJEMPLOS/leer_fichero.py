archivo=open(r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\3.3 EJEMPLOS\texto.txt"
            ,mode="r"
            ,encoding="UTF-8")

linea=archivo.readline()

while(linea):
    print(linea,end="")
    linea=archivo.readline()