# import lista_compra

# mi_lista = lista_compra.ListaCompra(comercio="Alcampo", nombre_lista="Compra semanal")
# mi_lista.add_producto(nombre="Leche", cantidad=6, precio_unitario=1)

# print(mi_lista)

from lista_compra import ListaCompra as LC, Producto

mi_lista = LC(comercio="Alcampo", nombre_lista="Compra semanal")
mi_lista.add_producto(nombre="Leche", cantidad=6, precio_unitario=1)

print(mi_lista)