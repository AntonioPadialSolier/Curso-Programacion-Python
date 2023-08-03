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

        # Desempaquetamos la fila
        CCAA_fila, indicador_fila, anyo_fila, valor_fila = row

        # Buscamos un "Total Nacional" con el indicador "con alquiler imputado" para el año en cuestión
        if CCAA_fila=="Total Nacional" and "(con alquiler imputado)" in indicador_fila and anyo_fila==anyo:
            tasa_nacional=float(row[3].replace(",","."))

        # Misma búsqueda que la anterior pero sin que sea Total Nacional
        # Me guardo el valor si es superior al que ya tengo guardado
        elif CCAA_fila!="Total Nacional" and "(con alquiler imputado)" in indicador_fila and anyo_fila==anyo and float(valor_fila.replace(",","."))>tasa_comunidad_mayor_riesgo:
            comunidad_mayor_riesgo=CCAA_fila
            tasa_comunidad_mayor_riesgo=float(valor_fila.replace(",","."))
        
    # Resultados
    print(f"La tasa de riesgo de probreza general para el año {anyo} es {tasa_nacional}.")
    print(f"La comunidad con mayor tasa es {comunidad_mayor_riesgo} y su valor es {tasa_comunidad_mayor_riesgo}, {tasa_comunidad_mayor_riesgo-tasa_nacional} puntos superior a la nacional.")