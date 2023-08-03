try:
    edad=int(input("¿Cuántos años tienes? "))
except ValueError as e:
    print("Vaya, parece que no has introducido una edad correcta")
else:
    print(f"Hola, tienes {edad} años.")
finally:
    print("Fin del programa")