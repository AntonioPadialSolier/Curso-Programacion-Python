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