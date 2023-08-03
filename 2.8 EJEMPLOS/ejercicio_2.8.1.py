# Definimos la lista donde almacenaremos los valores
palabras = []

# Solicitamos 4 palabras
palabras.append(input("Hola, escribe una palabra: "))
palabras.append(input("Escribe otra palabra, por favor: "))
palabras.append(input("Una más: "))
palabras.append(input("Y la última: "))

# Contamos las repeticiones
print("La palabra",palabras[0], "la has escrito",palabras.count(palabras[0]),"veces")
print("La palabra",palabras[1], "la has escrito",palabras.count(palabras[1]),"veces")
print("La palabra",palabras[2], "la has escrito",palabras.count(palabras[2]),"veces")
print("La palabra",palabras[3], "la has escrito",palabras.count(palabras[3]),"veces")

# Las escribimos en orden alfabético
palabras.sort()
print("En orden alfabético: ", palabras)

# Las escribimos en orden alfabético inverso
palabras.sort(reverse=True)
print("En orden alfabético descendente: ", palabras)

# Quitamos la primera palabra
palabras.pop(0)

# Y ahora la  última
palabras.pop()

# Mostramos el resultado
print("Quitando la primera y la última: ", palabras)

