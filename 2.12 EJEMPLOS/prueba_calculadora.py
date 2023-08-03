from calculadora import *

# Creamos el objeto
mi_calculadora = Calculadora()

# Guardamos el valor en la memoria
mi_calculadora.guardar_en_memoria(12)

# Escribimos el resultado
print("Valor guardado:", mi_calculadora.leer_memoria())

# Probamos a crear un objeto _Memoria
print("Probamos a crear un objeto memoria")
mi_memoria = _Memoria()
print("He podido crearlo")

# Probamos a borrar la memoria
mi_calculadora.__borrar_memoria()
