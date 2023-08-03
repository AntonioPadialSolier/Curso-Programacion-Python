# Variable auxiliar para almacenar las listas
listas_compra=list()

# Variable auxiliar para almacenar la opción elegida
opcion=None

while(opcion != 4):
    print("Selecciona una opción:")
    print("[1] Ver las listas ya creadas")
    print("[2] Crear una nueva lista")
    print("[3] Borrar una lista")
    print("[4] Finalizar")

    opcion=int(input("[1,2,3,4]: "))
    
    if(opcion==1):
        # Mostramos un mensaje con el número de listas almacenadas
        print("Tienes",len(listas_compra),"listas de la compra: ")
        
        # Recorremos la colección y mostramos el nombre de cada lista
        for lista_compra in listas_compra:
            print(lista_compra["Nombre"])

    elif(opcion==2):

        # Solicitamos el nombre de la lista
        nombre_lista = input("¿Cómo se llama la nueva lista? ")

        # Creamos la lista de la compra (un diccionario)
        # incorporando el nombre
        nueva_lista = {"Nombre":nombre_lista}

        # Creamos la colección de productos
        lista_productos=list()

        # Utilizamos un bucle while para recopilarlos
        mas_productos = None
        
        while(mas_productos != "N"):
            lista_productos.append(input("Producto a añadir a la lista: "))
            mas_productos = input("¿Quieres añadir un nuevo producto [S/N] ")

        # Añadimos la lista de artículos al diccionario
        nueva_lista["Productos"] = lista_productos

        # Y finalmente, añadimos la lista a la colección
        listas_compra.append(nueva_lista)
              
    elif(opcion==3):

        if(len(listas_compra)> 0):
            print("¿Qué lista quieres borrar?")

            i=0
            while(i<len(listas_compra)):            
                print("[",i,"]",listas_compra[i]["Nombre"])
                
                # Opción "B" en varias líneas
                # lista_compra = listas_compra[i]
                # nombre_lista = lista_compra["Nombre"]
                # print("[",i,"]",nombre_lista)

                i+=1

            a_borrar=int(input("Selecciona una opción [N] o [-1] si no quieres borrar ninguna: "))

            if(a_borrar!=-1):
                lista_borrada=listas_compra.pop(a_borrar)
                print("Has borrado la lista: ",lista_borrada["Nombre"])
        else:
            print("No tienes ninguna lista guardada")