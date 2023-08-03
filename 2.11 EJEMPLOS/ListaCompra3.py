class ListaCompra:
    """Objeto que representa una lista de la compra"""
    nombre=None
    num_productos=0
    impt_total=0
    productos=list()

    def __init__(self, *productos:str, nombre:str="", impt_total:int=0):
        """Constructor que crea la clase e informa todos los atributos de la misma:
        * nombre: nombre de la lista de la compra
        * impt_total: importe total de la compra
        * productos: lista de productos a comprar        
        * num_productos: calculado por el constructor a partir de "productos"
        """
        self.nombre = nombre
        self.impt_total = impt_total
        self.productos = list(productos)
        self.num_productos = len(self.productos)

    def __str__(self):
        """Devuelve una variable de tipo str con el contenido de la lista incluyendo nombre, importe, total de productos y detalle de los mismos"""
        mensaje = "Lista de la compra: " + self.nombre + "\n"
        mensaje += "Nº total de productos: " + str(self.num_productos) + "\n"
        mensaje += "Importe: " + str(self.impt_total) + "\n"
        mensaje += "Productos: " + "\n"        
        for producto in self.productos:
            mensaje += "> " + producto + "\n"
        return mensaje 
        
    def add_producto(self, producto:str, importe:int):
        """Añade un nuevo producto a la lista de la compra.
        * producto: producto a añadir"""
        self.productos.append(producto)
        self.num_productos+=1
        self.impt_total+=importe

# Creamos una nueva instancia de la clase ListaCompra
mi_lista = ListaCompra("Huevos", "Leche", "Azúcar", nombre="Compra fin de semana", impt_total=18)

# Mostramos los valores
print(mi_lista)

# Creamos una segunda lista de la compra
mi_segunda_lista = ListaCompra("Vino", "Tarta", "Aperitivos", nombre="Compra cena con amigos", impt_total=35)

# Mostramos los valores
print(mi_segunda_lista)

# Añadimos un nuevo artículo a la lista
mi_lista.add_producto("Pan", 1)
print(mi_lista)