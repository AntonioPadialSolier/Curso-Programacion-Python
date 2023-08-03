import datetime

# Definimos las clases que representan los errores

class NombreError(BaseException):
    nombre:str

    def __init__(self,nombre):
        self.nombre=nombre

class Apellido1Error(BaseException):
    apellido_1:str

    def __init__(self,apellido_1):
        self.apellido_1=apellido_1

class Apellido2Error(BaseException):
    apellido_2:str

    def __init__(self,apellido_2):
        self.apellido_2=apellido_2

class FechaNacimientoError(BaseException):
    fecha_nacimiento:str

    def __init__(self,fecha_nacimiento):
        self.fecha_nacimiento=fecha_nacimiento

# Definimos la clase persona
class Persona:
    nombre:str
    apellido_1:str
    apellido_2:str
    fecha_nacimiento:str

    def __init__(self, nombre:str, apellido_1:str, apellido_2:str, fecha_nacimiento:str):
        """Constructor de la clase. Valida todos los datos y genera excepciones personalizadas"""
        
        # Nombre >= 3 caracteres
        if len(nombre) < 3:
            raise NombreError(nombre)
        else:
            self.nombre=nombre
        
        # Apellido 1 >= 3 caracteres
        if len(apellido_1) < 3:
            raise Apellido1Error(apellido_1)
        else:
            self.apellido_1=apellido_1

        # Apellido 2 >= 3 caracteres
        if len(apellido_2) < 3:
            raise Apellido2Error(apellido_2)
        else:
            self.apellido_2=apellido_2

        # Controlar una fecha es muy complejo. Como strptime ya lo hace,
        # capturo el error y lanzo un error personalizado.
        try:
            self.fecha_nacimiento=datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')
        except:
            raise FechaNacimientoError(fecha_nacimiento)
        else:
            self.fecha_nacimiento=fecha_nacimiento
    
    def __str__(self):
        texto=f"* Nombre: {self.nombre}"
        texto+=f"\n* Apellidos: {self.apellido_1} {self.apellido_2}"
        texto+=f"\n* Fecha de nacimiento: {self.fecha_nacimiento}"
        return texto

if __name__=="__main__":

    # Solicitamos los datos
    nombre=input("Nombre: ")
    apellido_1=input("Apellido_1: ")
    apellido_2=input("Apellido_2: ")
    fecha_nacimiento=input("Fecha Nacimiento [YYYY-MM-DD]: ")

    # Construimos la clase
    persona=Persona(nombre,apellido_1, apellido_2, fecha_nacimiento)

    # Mostramos el resultado por pantalla
    print(persona)

