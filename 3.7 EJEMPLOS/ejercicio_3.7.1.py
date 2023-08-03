import csv

# Solicitamos el año para el que queremos buscar datos
anyo=input("¿De qué año quieres los datos: ")

# Abrimos el archhivo
with open(file=r'C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\3.5 EJEMPLOS\9963.csv', mode="r") as f:

    # Creamos el objeto reader que nos permite recorrerlo
    reader = csv.reader(f, delimiter=';')
    
    # Las filas son listas de strings. 
    # En la posición 0 está el Total Nacional y la comunidad
    # En la posición 1 el nombre del indicador
    # En la posición 2 el año
    # Y en la 3 el valor

    # Variables auxiliares
    tasa_nacional=0
    comunidad_mayor_riesgo=""
    tasa_comunidad_mayor_riesgo=0

    # Recorremos el archivo
    for row in reader:

        # Desempaquetamos cada fila en varias variables
        fila_comunidad, fila_indicador, fila_anyo, fila_valor = row

        # Buscamos un "Total Nacional" con el indicador "con alquiler imputado" para el año en cuestión
        if fila_comunidad=="Total Nacional" and "(con alquiler imputado)" in fila_indicador and fila_anyo==anyo:
            tasa_nacional=float(fila_valor.replace(",","."))

        # Misma búsqueda que la anterior pero sin que sea Total Nacional
        # Me guardo el valor si es superior al que ya tengo guardado
        elif fila_comunidad!="Total Nacional" and "(con alquiler imputado)" in fila_indicador and fila_anyo==anyo and float(fila_valor.replace(",","."))>tasa_comunidad_mayor_riesgo:
            comunidad_mayor_riesgo=fila_comunidad
            tasa_comunidad_mayor_riesgo=float(fila_valor.replace(",","."))
        
    # Resultados
    print(f"La tasa de riesgo de probreza general para el año {anyo} es {tasa_nacional}.")
    print(f"La comunidad con mayor tasa es {comunidad_mayor_riesgo} y su valor es {tasa_comunidad_mayor_riesgo}, {tasa_comunidad_mayor_riesgo-tasa_nacional} puntos superior a la nacional.")