def cuadrado_impares(*valores:float)->list:
    """
    Función que calcula el cuadrado de los números
    """

    # Creamos la variable con el resultado
    resultado=list()

    # Recorremos los valores
    for v in valores:

        # Comprobamos si es par o impar
        if v%2!=0:

            # Si es impar se añade a la colección
            resultado.append(v*v)
    
    # Devolvemos el resultado
    return resultado

def cuadrado_impares_comprension(*valores:float)->list:
    """
    Función que calcula el cuadrado de los números
    """

    # Creamos la variable con el resultado
    resultado=list()

    # Lista por comprensión
    resultado = [n*n for n in valores if n%2 != 0]

    # Devolvemos el resultado
    return resultado

res = cuadrado_impares(1,2,3,4,5,6,7,8,9)
print(res)

res = cuadrado_impares_comprension(1,2,3,4,5,6,7,8,9)
print(res)