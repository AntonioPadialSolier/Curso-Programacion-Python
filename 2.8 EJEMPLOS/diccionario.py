# Creamos la biblioteca inicial
biblioteca = {"978-84-9759-839-2" : "El amor en los tiempos del cólera", "978-84-674-2278-8" : "El juego de Ender"}
num_libros_antes = len(biblioteca)
print("En la biblioteca tenemos", num_libros_antes,"libros: ")
print(biblioteca)

# Solicitamos un nuevo valor
isbn = input("ISBN del nuevo libro a guardar: ")
titulo = input("Título del nuevo libro a guardar: ")

# Actualizamos la colección
biblioteca[isbn] = titulo
num_libros_despues = len(biblioteca)

# Indicamos si hemos guardado algún nuevo libro
if num_libros_despues > num_libros_antes:
    print("Has guardado un nuevo libro. Ahora tenemos", num_libros_despues)
else:
    print("Seguimos teniendo los mismos", num_libros_despues,"libros")

# Mostramos la colección
print(biblioteca)

# Vamos a retirar un libro
a_borrar = input("¿Qué libro quieres retirar de la biblioteca?: ")
print("Has retirado el libro: ", biblioteca.pop(a_borrar))

# Y ahora vamos a retirar otro
a_borrar = input("¿Qué otro libro quieres retirar?: ")
del biblioteca[a_borrar]

print("Ahora en la biblioteca quedan los siguientes libros")
print(biblioteca)
