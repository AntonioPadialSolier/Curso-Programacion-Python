class Vehiculo:
    tipo:str
    marca:str
    modelo:str
    num_ruedas:int
    
    def __init__(self,tipo:str,marca:str,modelo:str,num_ruedas:int):
        self.tipo=tipo
        self.marca=marca
        self.modelo=modelo
        self.num_ruedas=num_ruedas

class Coche(Vehiculo):
    def __init__(self,marca:str,modelo:str):
        self.tipo="Coche"
        self.marca=marca
        self.modelo=modelo
        self.num_ruedas=4

class Moto(Vehiculo):
    def __init__(self,marca:str,modelo:str):
        self.tipo="Moto"
        self.marca=marca
        self.modelo=modelo
        self.num_ruedas=2

# Creamos un nuevo Vehículo para representar un coche
mi_coche=Coche("Seat","Leon")

# Y ahora uno para representar una moto
mi_moto=Moto("Kawasaki","Ninja")    

