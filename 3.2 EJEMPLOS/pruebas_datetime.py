# Importamos el módulo datetime
import datetime

# Importamos el módulo locale
import locale

# Establecemos el lenguaje español
locale.setlocale(locale.LC_ALL,"es_ES")

# Creamos un nuevo objeto que represente el momento actual
ahora=datetime.datetime.now()

# Mostramos la fecha por pantalla
print(ahora)

# Vamos a trabajar un poco más la fecha
print(f"Fecha en formato YYYY-MM-DD: {ahora.strftime('%Y-%m-%d')}")
print(f"Hoy es: {ahora.strftime('%A')}")
