# Variable para almacenar la tareas
lista_tareas=list()

# Variable para guardar la opción seleccionada
opcion=None

# Empieza el bucle. Como la variable está vacía, 
# la condición de que sea diferente a "L" se cumple
while(opcion!="L"):

    # Escribimos las opciones
    print("Por favor, elige una opción:")
    print("(A) Añadir una tarea a la lista")
    print("(L) Escribir la lista de tareas y terminar")

    # Recogemos la respuesta
    opcion=input("Opción: ")

    # Si la opción es A, solicitamos un nuevo valor
    if(opcion=="A"):
        lista_tareas.append(input("¿Cuál es la tarea que quieres añadir a la lista?: "))

    # En caso contrario no hay que hacer nada, el bucle vuelve a empezar

# Si hemos salido del bucle es porque el usuario ha
# seleccionado la opción "L"

# Escribimos la lista de tareas
print("La lista de tareas que has guardado es: ")
print(lista_tareas)

# Y ¡fin!