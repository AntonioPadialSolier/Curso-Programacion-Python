# Creamos un diccionario
mis_libros_favoritos=dict()

# Añadimos algunos valores
mis_libros_favoritos["Ciencia Ficción"]="El juego de Ender"
mis_libros_favoritos["Novela"]="Los pilares de la tierra"
mis_libros_favoritos["Fantasía"]="El Silmarillion"
mis_libros_favoritos["Clásico"]="La Ilíada"

# Vamos a recorrer primero los géneros
print("Géneros: ")
for genero in mis_libros_favoritos.keys():
    print("- " + genero)

# Y ahora los libros
print("Libros: ")
for libro in mis_libros_favoritos.values():
    print("- " + libro)    