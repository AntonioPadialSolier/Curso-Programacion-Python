# Solicitamos algunos datos para jugar
nombre=input("Hola, ¿cuál es tu nombre? ")
edad=int(input("¿Y tu edad? "))

# Expresiones
print(f"Hola. Te llamas {nombre} y has vivido {edad*365} días.")

# Aplicar funciones
print(f"Por cierto, tu nombre en mayúsculas es: {nombre.upper()}")

# Saltos de línea
print(f"En un lugar de la Mancha,\nde cuyo nombre no quiero acordarme...")

# Tamaño mínimo de un texto
capital="Madrid"
print(f"\tLa capital de España es >{capital:10}<")

# Números decimales (distinto número de decimales)
pi=3.141592
print(f"El valor de pi es: {pi}")
print(f"El valor de pi es: {pi:.1f}")
print(f"El valor de pi es: {pi:.3f}")
print(f"El valor de pi es: {pi:.10f}")