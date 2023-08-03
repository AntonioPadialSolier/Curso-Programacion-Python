nombre, apellido_1, apellido_2="Antonio","Padial","Solier"
print(f"Hola, me llamo {nombre} {apellido_1} {apellido_2}")

dia_nacimiento, mes_nacimiento, anyo_nacimiento, aficiones = 4, "Noviembre", 1981, ("Leer", "Escribir", "Viajar")

print(f"Nací el {dia_nacimiento} de {mes_nacimiento} de {anyo_nacimiento}")
print(f"Mis aficiones son {aficiones}")

ciudades_esp_favoritas="Granada","Pontevedra","Madrid"
print(type(ciudades_esp_favoritas))

libros=("Aprende SQL en un fin de semana", "Aprende a programar con Python en un fin de semana")
libro_1, libro_2=libros
print(f'Aparte de "{libro_2}", que espero te esté gustando, he escrito otro libro: "{libro_1}".')