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

# Creamos un nuevo Vehículo para representar un coche
mi_coche=Vehiculo("Coche","Seat","Leon",4)

# Y ahora uno para representar una moto
mi_moto=Vehiculo("Moto","Kawasaki","Ninja",2)    

