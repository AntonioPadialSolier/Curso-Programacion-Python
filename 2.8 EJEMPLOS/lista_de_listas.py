# Vamos a crear una lista de listas paso a paso

# En primer lugar creamos una lista vacía
biblioteca=list() 

# Ahora creamos una lista para cada una de las baldas
balda_0=["El Incal", "Maus", "El Eternauta", "Diario de un ingenuo", "Blacksad"]
balda_1=["Yo mato", "Carrión", "La familia de Pascual Duarte", "A sangre y fuego"]
balda_2=["El Quijote", "Poeta en Nueva York", "Muerte de un viajante"]

# Y ahora las añadimos a la biblioteca
biblioteca.append(balda_0)
biblioteca.append(balda_1)
biblioteca.append(balda_2)

# Vamos a escribirla por consola
print(biblioteca)

# Dado que es una lista de listas, puedo utilizar acceso posicional en 2 niveles

# Primer libro de la primera balda
print("El primer libro de la primera balda es:", biblioteca[0][0])

# Segundo libro de la tercera balda
print("El segundo libro de la tercera balda es:", biblioteca[2][1])

# Vamos a eliminar un libro
libro = biblioteca[2].pop(1)
print("Hemos sacado el libro:", libro)
print("Ahora el segundo libro de la tercera balda es:", biblioteca[2][1])
