# Utilizamos open para abrir el fichero en modo lectura
archivo=open(file=r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\3.3 EJEMPLOS\pruebas_leer_ficheros.py",mode="r")

# Escribimos el contenido del mismo por pantalla
print(">> El contenido del archivo es:")
print(archivo.read())
print(">> Fin del archivo")