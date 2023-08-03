class ListaCompra:
    """Objeto que representa una lista de la compra"""
    nombre=None
    num_productos=0
    impt_total=0
    productos=list()

# Creamos una nueva instancia de la clase ListaCompra
mi_lista = ListaCompra()

# Modificamos los valores de los atributos
mi_lista.nombre="Compra fin de semana"
mi_lista.productos.extend(["Huevos","Leche","Azúcar"])
mi_lista.num_productos=len(mi_lista.productos)
mi_lista.impt_total=18

# Mostramos los valores
print(mi_lista.nombre)
print(mi_lista.productos)
print(mi_lista.num_productos)
print(mi_lista.impt_total)

# Creamos una segunda lista de la compra
mi_segunda_lista = ListaCompra()

mi_segunda_lista.nombre="Compra cena con amigos"
mi_segunda_lista.productos.extend(["Vino", "Tarta", "Aperitivos"])
mi_segunda_lista.num_productos=len(mi_segunda_lista.productos)
mi_segunda_lista.impt_total=35

# Mostramos los valores
print(mi_segunda_lista.nombre)
print(mi_segunda_lista.productos)
print(mi_segunda_lista.num_productos)
print(mi_segunda_lista.impt_total)