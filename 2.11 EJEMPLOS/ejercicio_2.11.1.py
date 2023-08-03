class Producto:
    """Clase que representa un producto a utilizar en listas de la compra."""
    nombre:str
    cantidad:int
    precio_unitario:int

    def __init__(self, nombre:str, cantidad:int, precio_unitario:int):
        """Crea una nueva instancia de tipo Producto
        * nombre: Nombre del producto
        * cantidad: Cantidad a comprar
        * precio_unitario: Precio de cada unidad"""
        self.nombre=nombre
        self.cantidad=cantidad
        self.precio_unitario=precio_unitario

    def __str__(self):
        """Devuelve un texto con el detalle del producto"""
        texto="    - Producto: " + self.nombre+"\n"
        texto+="      Cantidad: " + str(self.cantidad)+"\n"
        texto+="      Precio Unitario: " + str(self.precio_unitario)+"\n"
        texto+="      Precio Total: " + str(self.precio_total())+"\n"
        return texto

    def precio_total(self)->int:
        """Calcula el precio total del Producto multiplicando el precio unitario por la cantidad"""
        return self.cantidad * self.precio_unitario

class ListaCompra:
    """Clase que representa una lista de la compra"""
    nombre_lista:str
    comercio:str
    productos:list

    def __init__(self, nombre_lista:str, comercio:str):
        """Constructor de la lista de la compra. Los parámetro de entrada son:
        * nombre_lista: nombre de la lista
        * comercio: comercio donde se hará la compra"""
        self.nombre_lista=nombre_lista
        self.comercio=comercio

        # Aparte de almacenar los valores, inicializamos la lista de productos
        self.productos=list()

    def __str__(self):
        """Genera una representación en modo texto de toda la lista"""
        texto="> " + self.nombre_lista + "\n"
        texto+="  Precio Total de la lista: " + str(self.importe_total()) + "\n"
        texto+="  Productos: " + str(self.total_productos()) + "\n"       
                   
        # Recorremos los productos añadiendo al texto la representación
        # en modo texto de cada uno de ellos
        producto:Producto
        for producto in self.productos:
            texto+=producto.__str__()
        
        return texto

    def add_producto(self, nombre:str, cantidad:int, precio_unitario:int):
        """Añade un nuevo Producto a la lista:
        * nombre: Nombre del producto
        * cantidad: Cantidad a comprar
        * precio_unitario: Precio de cada unidad"""

        # Añadimos a la lista una nueva instancia de Producto
        self.productos.append(Producto(nombre, cantidad, precio_unitario))

    def total_productos(self):
        """Devuelve el número total de productos de la lista"""
        return len(self.productos)

    def importe_total(self):
        """Calcula el importe total de la lista de la compra"""
        impt_total=0

        # Utilizamos la función de la clase Producto para calcular su importe
        for articulo in self.productos:
            impt_total+=articulo.precio_total()

        return impt_total

# Variable auxiliar para almacenar las listas de la compra
listas_compra=list()

# Variable auxiliar para almacenar la opción elegida
opcion=None

# El bucle se repite hasta que el usuario selecciona
# la opción nº 4
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
        lista_compra:ListaCompra
        for lista_compra in listas_compra:
            print(lista_compra)

    elif(opcion==2):

        # Solicitamos el nombre de la lista
        nombre_lista = input("¿Cómo se llama la nueva lista? ")

        # Solicitamos el comercio
        comercio_lista = input("¿Para qué comercio es? ")

        # Creamos la lista de la compra
        nueva_lista = ListaCompra(nombre_lista,comercio_lista)

        # Utilizamos un bucle while para añadir productos
        mas_productos = None

        while(mas_productos != "N"):
            
            # Recogemos los valores
            nombre_producto=input("Producto a añadir a la lista: ")
            cantidad_producto=int(input("Cantidad: "))
            precio_unitario_producto=int(input("Precio Unitario: "))

            # Creamos el nuevo producto
            nueva_lista.add_producto(nombre_producto, cantidad_producto, precio_unitario_producto)

            # Preguntamos si el usuario quiere continuar
            mas_productos = input("¿Quieres añadir un nuevo producto [S/N] ")

        # Y finalmente, añadimos la lista a la colección
        listas_compra.append(nueva_lista)
              
    elif(opcion==3):
        # Borrado de listas, sólo si hay alguna

        if(len(listas_compra)> 0):
            print("¿Qué lista quieres borrar?")

            # Hacemos un bucle de tipo while para almacenar
            # en una variable el índice de la lista a borrar
            i=0
            while(i<len(listas_compra)):            
                print("[",i,"]",listas_compra[i].nombre_lista)
                i+=1

            a_borrar=int(input("Selecciona una opción [N] o [-1] si no quieres borrar ninguna: "))

            # Borramos la lista mediante el método pop()
            if(a_borrar!=-1):
                lista_borrada=listas_compra.pop(a_borrar)
                print("Has borrado la lista:",lista_borrada.nombre_lista)
        else:
            print("No tienes ninguna lista guardada")