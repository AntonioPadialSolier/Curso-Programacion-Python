# Vamos a hacer un pequeño concurso
# La prueba consiste en adivinar si una serie de números son
# divisibles entre otro

# En primer lugar solicitamos el valor con el que vamos a "jugar"
divisor=int(input("Cuál es el valor por el que se dividirán los números: "))

# A continuación solicitamos el número de preguntas
num_preguntas=int(input("¿Cuántas preguntas quieres que tenga el concurso?: "))

# Ahora vamos a recoger los valores con los que jugaremos
valores=list()
i=1

while(i<=num_preguntas):
    valores.append(int(input("Introduce un número para concursar: ")))
    i+=1

# Vamos a empezar el concurso. Creamos una variable para la puntuación
puntuacion=0

# Recorremos la colección para preguntar al usuario
for valor in valores:
    print("¿", valor,"es divisible entre", divisor, "?")
    respuesta = input("[S/N] ")

    # Si es divisor y hemos respondido "S" sumamos un punto
    if (respuesta=="S" and valor%divisor==0):
        puntuacion+=1
    # Si no es divisor y hemos respondido "N" también sumamos un punto
    elif (respuesta=="N" and valor%divisor!=0):
        puntuacion+=1

# Y para finalizar mostramos la puntuación
print("Has acertado", puntuacion, "de", len(valores), "preguntas.")        

#
# ################################################
#

# Recorremos la colección para preguntar al usuario
# (versión "while")

# Utilizamos una variable auxiliar. El bucle termina cuando
# i = len(valores)
i=0
while(i< len(valores)):

    # Guardamos el valor a tratar en una variable auxiliar
    valor = valores[i]

    print("¿", valor,"es divisible entre", divisor, "?")
    respuesta = input("[S/N] ")

    # Si es divisor y hemos respondido "S" sumamos un punto
    if (respuesta=="S" and valor%divisor==0):
        puntuacion+=1
    # Si no es divisor y hemos respondido "N" también sumamos un punto
    elif (respuesta=="N" and valor%divisor!=0):
        puntuacion+=1

    # Pasamos a la siguiente vuelta
    i+=1        

# Y para finalizar mostramos la puntuación
print("Has acertado", puntuacion, "de", len(valores), "preguntas.")
