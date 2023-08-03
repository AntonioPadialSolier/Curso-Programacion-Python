class EdadIncorrectaError(BaseException):
    """Clase diseñada para gestionar errores producidos
    por edades inferiores a 0. Contiene:
    * edad_introducida: edad errónea"""

    # Atributo utilizado para almacenar la edad
    edad:int

    def __init__(self,edad:int):
        """Constructor de la clase. Almacenamos la edad"""
        self.edad=edad

try:
    # Solicitamos la edad al usuario
    edad=int(input("¿Cuántos años tienes? "))

    # Si es inferior a 0, lanzamos el error
    if edad<0:
        raise EdadIncorrectaError(edad)

except ValueError as e:
    print(f"Vaya, parece que no has introducido una edad correcta")
except EdadIncorrectaError as e:
    print(f"Es imposible que tengas menos de 0 años [{e.edad}]")
else:
    print(f"Hola, tienes {edad} años.")
finally:
    print("Fin del programa")    