class ListaCompra:
    """Objeto que representa una lista de la compra"""
    nombre=None
    num_productos=0
    impt_total=0
    productos=list()

    def __init__(self, nombre:str, impt_total:int, *productos:str):
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
        
# Creamos una nueva instancia de la clase ListaCompra
mi_lista = ListaCompra("Compra fin de semana", 18, "Huevos", "Leche", "Azúcar")

# Mostramos los valores
print(mi_lista.nombre)
print(mi_lista.productos)
print(mi_lista.num_productos)
print(mi_lista.impt_total)

# Creamos una segunda lista de la compra
mi_segunda_lista = ListaCompra("Compra cena con amigos", 35, "Vino", "Tarta", "Aperitivos")

# Mostramos los valores
print(mi_segunda_lista.nombre)
print(mi_segunda_lista.productos)
print(mi_segunda_lista.num_productos)
print(mi_segunda_lista.impt_total)