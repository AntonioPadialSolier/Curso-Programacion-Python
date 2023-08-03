nombre=input("Hola, ¿cuál es tu nombre? ")
apellido_1=input("¿Y tu primer apellido? ")
apellido_2=input("¿Y el segundo? ")
año=int(input("¿En qué año naciste? "))
ahorros=float(input("Y para terminar, ¿cuánto dinero tienes en el banco? "))

print(f"Tu nombre completo es {nombre.capitalize()} {apellido_1.capitalize()} {apellido_2.capitalize()}.")
print(f"Tienes {2022-año} años.")
print(f"Y {ahorros*1.1323:.2f}$ en el banco.")

