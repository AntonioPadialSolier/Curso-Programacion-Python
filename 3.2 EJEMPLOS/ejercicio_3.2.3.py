import datetime

class Nacimiento:
    """Clase que representa una fecha de nacimiento"""

    # Objeto utilizado para representar la fecha
    nacimiento:datetime.datetime

    # Formato YYYY-MM-DD
    FORMATO="%Y-%m-%d"

    def __init__(self, fecha:str):
        """Constructor de la clase a partir de un año, mes y día"""
        self.nacimiento=datetime.datetime.strptime(fecha,self.FORMATO)

    def proximo_cumpleanyos(self)->str:
        """Método que calcula cuándo será el próximo cumpleaños.
        Lo devuelve en formato YYYY-MM-DD"""
        
        # Capturamos el momento actual
        ahora=datetime.datetime.now()
        
        # Creamos un objeto que representa el cumpleaños de este año
        cumple_este_anyo=datetime.datetime(year=ahora.year 
                                        , month=self.nacimiento.month
                                        , day=self.nacimiento.day)

        # Y otro para el año que viene
        cumple_anyo_siguiente=datetime.datetime(year=ahora.year +1
                                        , month=self.nacimiento.month
                                        , day=self.nacimiento.day)

        # Si la fecha aún no ha pasado, el cumpleaños es este año
        if(ahora <= cumple_este_anyo):
            return(cumple_este_anyo.strftime(self.FORMATO))
        else:
            return(cumple_anyo_siguiente.strftime(self.FORMATO))

    def cuantos_anyos_tendre(self, fecha:str)->int:
        """Calcula cuántos años se habrán cumplido en una fecha
        especificada en formato YYYY-MM-DD"""

        # Creamos un objeto "date" a partir de la fecha
        inc_fecha=datetime.datetime.strptime(fecha,self.FORMATO)

        # Calculamos la diferencia respecto a esa fecha
        anyos=inc_fecha-self.nacimiento

        # Devolvemos la diferencia en años
        return anyos.days // 365

    def cuanto_he_vivido(self)->int:
        """Calcula cuántos días han pasado desde el nacimiento"""

        # Capturamos el momento actual
        ahora=datetime.datetime.now()

        # Devolvemos la diferencia respecto al nacimiento en días
        # (esta vez no utilizamos un objeto auxiliar, no es necesario)
        return((ahora-self.nacimiento).days)

    def que_dia_naci(self)->str:
        """Función que devuelve el día de la semana 
        de la fecha de nacimiento"""
        return(self.nacimiento.strftime("%A"))

if(__name__=="__main__"):

    # Solicitamos la fecha de nacimiento
    nacimiento=Nacimiento(input("Hola, ¿qué día naciste? [YYYY-MM-DD]: "))

    # Probamos todas las funciones
    print(f"Tu próximo cumpleaños será el {nacimiento.proximo_cumpleanyos()}.")

    print(f"El 2030-01-01 tendrás {nacimiento.cuantos_anyos_tendre('2030-01-01')} años.")

    print(f"Has vivido {nacimiento.cuanto_he_vivido()} días.")

    print(f"Naciste un {nacimiento.que_dia_naci()}.")
