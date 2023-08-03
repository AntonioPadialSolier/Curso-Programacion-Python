import datetime

# Capturamos la fecha
ahora=datetime.datetime.now()

# Almacenamos el mes en una variable
mes = ahora.month

# Calculamos la estación en base al mes
if(mes >= 3 and mes <= 6):
    print("Estamos en primavera")
elif(mes >= 7 and mes <= 9):
    print("Estamos en verano")
elif(mes >= 10 and mes <= 12):
    print("Estamos en otoño")
else:
    print("Estamos en invierno")

# Mostramos un mensaje en función del día de la semana
if(ahora.weekday() <= 4):
    print("Vaya, hoy toca trabajar")
else:
    print("¡Qué bien! Hoy es fin de semana")


# Finalmente determinamos si el año es bisiesto
# Para ello calculamos si es divisible entre 4...
# lo que significa que el resto de la división
# entre el año y 4 es 0
if(ahora.year%4==0):
    print(f"El año {ahora.year} es bisiesto")
else:
    print(f"El año {ahora.year} no es bisiesto")