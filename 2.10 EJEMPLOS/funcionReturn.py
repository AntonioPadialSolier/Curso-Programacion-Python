def suma(*valores:int) -> int:
    """Función que suma los valores recibidos por parámetro
    * valores: conjunto de valores a sumar
    * return: resultado de la suma
    """
    total=0
    for valor in valores:
        total+=valor
    return total

print("Vamos a sumar dos valores.")
a =  int(input("Valor A: "))
b =  int(input("Valor B: "))

print("El total es:",suma(a,b))