archivo=open(r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\3.3 EJEMPLOS\escribir.txt"
            ,mode="w"
            ,encoding="UTF-8")

archivo.write("Esto es una nueva línea...")
archivo.write("...y esto otra, pero como no he utilizado un salto de línea el texto no se separa")

archivo.write("Acuérdate siempre de añadir un salto al final\n")
archivo.write("Y así el resultado será el esperado\n")

lineas=["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]

archivo.write("### VARIAS LÍNEAS ###\n")
archivo.writelines(lineas)