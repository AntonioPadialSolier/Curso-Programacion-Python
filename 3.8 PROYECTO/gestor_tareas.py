# Importamos el fichero donde definimos las clases
import tareas

# Creamos una variable para la lista de tareas
lista_tareas=tareas.ListaTareas()

# Variable de control de bucle
opcion:str=None

print("¡Hola! Bienvenido a tu gestor personal")

# Recuperamos las tareas del fichero
lista_tareas.recuperar_lista()

# Bucle de control
while(opcion!="S"):    
    print("Elige una opción:")
    print("\t (N) Crear una nueva tarea")
    print("\t (P) Listar tareas pendientes")
    print("\t (C) Listar tareas completadas")
    print("\t (F) Marcar una tarea como completada")
    print("\t (X) Borrar una tarea")
    print("\t (B) Buscar tareas")
    print("\t (S) Salir del programa")

    # Pasamos a mayúsculas la opción por si el usuario
    # se ha equivocado al escribir la letra
    opcion=input("Opción elegida: ").upper()

    if(opcion=="N"):
        # Creamos una nueva tarea solicitando antes los datos al usuario        
        categoria=input("Categoría de la tarea: ")
        nombre=input("Tarea: ")
        fecha_vencimiento=input("Fecha de vencimiento (YYYY-MM-DD): ")

        lista_tareas.nueva_tarea(categoria,nombre,fecha_vencimiento)

    elif(opcion=="P"):
        
        # Mostramos la lista de tareas pendientes
        lista_tareas.mostrar_tareas("P")

    elif(opcion=="C"):
        
        # Mostramos la lista de tareas completadas
        lista_tareas.mostrar_tareas("C")

    elif(opcion=="F"):
        # Mostramos la lista de tareas pendientes
        lista_tareas.mostrar_tareas("P")

        # Solicitamos el número de tarea a marcar como completa
        opcion=int(input(f"Tarea a completar [0-{len(lista_tareas.lista_tareas)-1}]: "))

        # Marcamos la tarea como completada
        if(opcion>=0 and opcion<=len(lista_tareas.lista_tareas)-1):
            lista_tareas.lista_tareas[opcion].completar()
        else:
            print("Lo siento, no has indicado un índice de tarea correcto")

    elif(opcion=="X"):
        # Mostramos todas las tareas
        lista_tareas.mostrar_tareas("T")

        # Solicitamos el número de tarea a eliminar
        opcion=int(input(f"Tarea a eliminar [0-{len(lista_tareas.lista_tareas)-1}]: "))

        # Eliminamos la tarea
        if(opcion>=0 and opcion<=len(lista_tareas.lista_tareas)-1):
            eliminada=lista_tareas.lista_tareas.pop(opcion)
            print(f"Has eliminado la tarea: {eliminada.nombre}")
        else:
            print("Lo siento, no has indicado un índice de tarea correcto")

    elif(opcion=="B"):
        # Solicitamos la tarea a buscar
        buscado=input("¿Qué tarea estás buscando: ")

        # Buscamos las tareas cuyo nombre contenga el texto buscado
        resultado=lista_tareas.buscar_tarea(buscado)

        if(len(resultado)==0):
            print("Lo siento, no he encontrado ninguna tarea")
        else:
            print(f"He encontrado {len(resultado)} tareas: ")

            for t in resultado:
                print(t)

# Guardamos la lista
lista_tareas.guardar_lista()

# Y nos despedimos
print("Adiós, y gracias por utilizar este gestor de tareas")