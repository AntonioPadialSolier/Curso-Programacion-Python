class _Memoria:
    """Clase privada que representa la memoria de la calculadora"""

    __valor:int

    def guardar_valor(self, valor:int):
        """Método que permite almacenar un valor en memoria:
        * valor: Número a almacenar"""
        self.__valor=valor

    def recuperar_valor(self)->int:
        """Método que recupera el valor guardado en la memoria"""
        return self.__valor


class Calculadora:
    """Clase que simula una calculadora"""
    
    # Variable utilizada para memorizar un número
    __memoria = _Memoria()

    def guardar_en_memoria(self, valor:int):
        """Método que permite almacenar un valor en memoria:
        * valor: Número a almacenar"""
        self.__borrar_memoria()
        self.__memoria.guardar_valor(valor)

    def leer_memoria(self)->int:
        """Método que recupera el valor guardado en la memoria"""
        return self.__memoria.recuperar_valor()

    def __borrar_memoria(self):
        """Método que borra la memoria"""
        self.__memoria=_Memoria()

if(__name__=="__main__"):

    # Creamos el objeto
    mi_calculadora = Calculadora()

    # Guardamos el valor en la memoria
    mi_calculadora.guardar_en_memoria(12)

    # Escribimos el resultado
    print("Valor guardado:",mi_calculadora.leer_memoria())

    # Probamos a crear un objeto _Memoria
    print("Probamos a crear un objeto memoria")
    mi_memoria = _Memoria()
    print("He podido crearlo")

    # Probamos a borrar la memoria
    mi_calculadora.__borrar_memoria()