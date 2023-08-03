# Vamos a crear estructuras de datos complejas

# Comercios. Tupla: acceso por índice, inmutable
comercios=("AHORRAMAS","LIDL", "ALDI", "MERCADONA", "CARREFOUR", "DIA", "SUPERCOR")

# Tipos de productos. Tupla: acceso por índice, inmutable
tipos_productos=("Fruta y verdura", "Conservas", "Precocinados", "Carne", "Pescado", "Bebidas")

# Lista de la compra. Un diccionario con sus características
lista_compra_1=dict()
lista_compra_1["Comercio"]="AHORRAMAS"
lista_compra_1["Nombre"]="Compra semanal"
lista_compra_1["Total productos"]=3
lista_compra_1["Importe total"]=5.25

# Producto 1. Un diccionario con sus características
l1_producto_1=dict()
l1_producto_1["Tipo"]= "Fruta y verdura"
l1_producto_1["Nombre"]= "Tomates"
l1_producto_1["Cantidad (kg, unidades)"]= 1
l1_producto_1["Precio (kg, unidades)"]= 2.25
l1_producto_1["Importe total"]= 2.25

# Producto 2. Un diccionario con sus características
l1_producto_2=dict()
l1_producto_2["Tipo"]="Conservas"
l1_producto_2["Nombre"]="Ventresca de atún"
l1_producto_2["Cantidad (kg, unidades)"]=1
l1_producto_2["Precio (kg, unidades)"]=3
l1_producto_2["Importe total"]=3

# La lista de productos será eso, una lista
lista_productos_1=[l1_producto_1, l1_producto_2]

# Añadimos la lista al diccionario
lista_compra_1["Productos"]=lista_productos_1

# ¡Y ya tenemos la primera lista de la compra!

# Repetimos con la segunda. Esta vez uso la sintaxis de las llaves
lista_compra_2={
    "Comercio":"MERCADONA",
    "Nombre":"Compra cena familiar",
    "Total productos":3,
    "Importe total":21
}

# Producto 1. Un diccionario con sus características
l2_producto_1={
    "Tipo":"Precocinados",
    "Nombre":"Pizza",
    "Cantidad (kg, unidades)":5,
    "Precio (kg, unidades)":3,
    "Importe total":15
}

# Producto 2. Un diccionario con sus características
l2_producto_2={
    "Tipo":"Precocinados",
    "Nombre":"Tortilla",
    "Cantidad (kg, unidades)":2,
    "Precio (kg, unidades)":3,
    "Importe total":6
}

# La lista de productos será eso, una lista
lista_productos_2=[l2_producto_1, l2_producto_2]

# Añadimos la lista al diccionario
lista_compra_2["Productos"]=lista_productos_2

# Y finalmente creamos la lista de listas de la compra
listas_compra=[lista_compra_1,lista_compra_2]

print("Las dos listas de la compra que tenemos son: ")
print(listas_compra)
