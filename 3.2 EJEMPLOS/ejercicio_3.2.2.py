import datetime
import locale

# Establecemos el lenguaje español
locale.setlocale(locale.LC_ALL,"es_ES")

# Capturamos la hora local
ahora=datetime.datetime.now()

# Con esta variable controlamos el bucle while
correcto="N"
while(correcto=="N"):

    # Solicitamos la fecha y la convertimos a datetime
    txt_fecha=input("¿En qué día naciste [YYYY-MM-DD]: ")
    fecha_nacimiento=datetime.datetime.strptime(txt_fecha,'%Y-%m-%d')

    # Si es incorrecta, mostramos un mensaje
    if (fecha_nacimiento > ahora):
        print("Fecha incorrecta, no has podido nacer después del día de hoy.")
    # Si es correcta, paramos el bucle
    else:
        correcto="S"

# Mostramos el día de la semana en el que nació el usuario
print(f"Has nacido un {fecha_nacimiento.strftime('%A')}")
