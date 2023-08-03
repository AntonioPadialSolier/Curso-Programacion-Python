# Vamos a crear un conjunto con las 3 vocales fuertes
# y otro con las débiels
fuertes={"A","E","O"}
debiles={"I","U"}

print("Las vocales fuertes son: ", fuertes)
print("Y las débiles : ", debiles)

# Copiamos las fuertes a una nueva colección
vocales=fuertes.copy()

# Y añadimos las débiles
vocales.update(debiles)

print("Las vocales del alfabeto latino son: ")
print(vocales)

# Y ahora vamos a eliminar elementos
vocales.remove(input("Dime una vocal a eliminar: "))
print("Quedan las siguientes vocales: ", vocales)

vocales.discard(input("Dime otra vocal a eliminar: "))
print("Quedan las siguientes vocales: ", vocales)