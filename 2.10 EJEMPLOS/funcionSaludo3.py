def saludo(nombre:str, edad:int, aficion:str=None):
    """Función que escribe un saludo por línea de comando a partir de: 
    * nombre: nombre de la persona
    * edad: edad de la persona"""
    if(aficion==None):
        print("Hola, me llamo", nombre, "y tengo", str(edad), "años")
    else:
        print("Hola, me llamo", nombre, "tengo", str(edad), "años y mi afición favorita es:",aficion)

saludo("Antonio", 40)

saludo("Antonio", 40, "leer")
