from io import TextIOWrapper


class ListaCompra:
    """Objeto que representa una lista de la compra"""
    nombre:str
    productos:list
    num_productos=0

    # "Constante" que utilizo para almacenar la ruta y el nombre del fichero
    FICHERO=r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\3.3 EJEMPLOS\mi_lista.txt"

    def __init__(self, nombre:str="",productos:list=None):
        """Constructor que crea la clase e informa todos los atributos de la misma:
        * nombre: nombre de la lista de la compra
        * productos: lista de productos a comprar        
        """
        self.nombre=nombre
        self.productos=productos
        if(self.productos!=None):
            self.num_productos = len(self.productos)
        
    def __str__(self):
        """Muestra por pantalla el contenido de la lista de la compra.
        Aplica un poco de formato para que sea más fácil de leer."""
        mensaje=""
        mensaje += f"Lista de la compra: {self.nombre} \n"
        mensaje += f"  Nº total de productos: {self.num_productos}"
        for producto in self.productos:
            mensaje+=f"\n\t > {producto}"

        return mensaje

    def guardar_lista(self):
        """Guarda la lista de la compra."""
       
        # Creamos el archivo
        f=open(self.FICHERO
            ,mode="w"
            ,encoding="UTF-8")

        # Guardamos el título
        f.write(self.nombre)

        # Guardamos los productos. 
        # Añado \n al principio de cada producto para no dejar
        # una línea en blanco al final
        for producto in self.productos:
            f.write("\n"+producto)

    def recuperar_lista(self):
        """Recupera la lista de la compra a partir del fichero mi_lista.txt"""

        # Abrimos el archivo
        f=open(self.FICHERO
            ,mode="r"
            ,encoding="UTF-8")

        # La primera línea será el nombre de la lista
        # Aplico strip para quitar el salto de línea
        linea=f.readline()
        self.nombre=linea.strip()

        # Y ahora recuperamos los productos

        # Creamos una nueva lista para guardarlos
        self.productos=list()
        producto=f.readline()
        while(producto):
            # Aplicamos strip para quitar los saltos de línea
            self.productos.append(producto.strip())   
            producto=f.readline()     

        # Guardamos el número de artículos
        self.num_productos=len(self.productos)    
        
        
if __name__=="__main__":
    
    # Presentamos las opciones
    print("Hola. ¿Qué es lo que quieres hacer?")
    print("(C) Crear una nueva lista")
    print("(R) Recuperar una lista")

    # Solicitamos la opción al usuario
    opcion=input("Opción (C) (R): ")

    # Crear una nueva lista de la compra
    if(opcion=="C"):

        # Solicitamos el nombre
        nombre=input("¿Cuál es el nombre de la lista? ")

        # Creamos la colección de productos
        productos=list()

        # Utilizamos un bucle while para recopilarlos
        mas_productos = None
        
        while(mas_productos != "N"):
            productos.append(input("Producto a añadir a la lista: "))
            mas_productos = input("¿Quieres añadir un nuevo producto [S/N] ")

        # Creamos el objeto
        mi_lista=ListaCompra(nombre,productos)

        # Y lo guardamos en disco
        mi_lista.guardar_lista()

    elif(opcion=="R"):

        # Creamos un objeto lista vacío
        mi_lista=ListaCompra()

        # Recuperamos el contenido
        mi_lista.recuperar_lista()

        # Y lo escribimos por pantalla
        print(mi_lista)

    else:
        print("Opción incorrecta")            