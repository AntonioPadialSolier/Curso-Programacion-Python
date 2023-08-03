# Vamos a combinar while con una pregunta al usuario

# Preguntamos cuántas series ha visto el usuario
num_series = int(input("Cuántas series has visto este último mes: "))

# Creamos una variable para guardar las series
series = list()
# Otra para controlar el bucle
i =  1

# Bucle para consultar las series
while(i <= num_series):
    series.append(input("Nombre de la serie: "))
    # Ojo, tenemos que ir avanzando porque si no el bucle sería infinito    
    i+=1

print("Este mes has visto las siguientes series:",series)
