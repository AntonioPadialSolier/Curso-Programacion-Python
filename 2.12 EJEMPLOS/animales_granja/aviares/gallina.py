class Gallina:
    """Clase que representa una gallina"""

    def hablar(self):        
        print("Clo Clo Clo")

# Este código sólo se tendrá en cuenta si ejecutas
# directamente el fichero gallina.py
if (__name__ == "__main__"):
    print("Probando la clase Gallina")
    mi_gallina=Gallina()
    mi_gallina.hablar()