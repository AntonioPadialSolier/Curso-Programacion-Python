import datetime

class Tarea:
    """
    Clase que representa una tarea de la lista. Contiene los siguientes datos:
        * categoria
        * nombre
        * fecha de vencimiento
        * tarea terminada (S/N)
        * fecha de finalización
    """
    categoria:str
    nombre:str
    fecha_vencimiento:datetime
    terminada:str="N"
    fecha_finalizacion:datetime=None

    def __init__(self, categoria:str, nombre:str, fecha_vencimiento:str, terminada:str="N", fecha_finalizacion:str=None):
        """
        Constructor de la clase. 
        Los parámetros opcionales son el indicador de tarea terminada (False por defecto)
        y la fecha de finalización (None por defecto)
        """
        self.categoria=categoria
        self.nombre=nombre
        self.fecha_vencimiento=datetime.datetime.strptime(fecha_vencimiento,"%Y-%m-%d")
        self.terminada=terminada
        # Sólo almacenamos la fecha de finalización si la tarea está terminada
        if (self.terminada=="S"):
            self.fecha_finalizacion=datetime.datetime.strptime(fecha_finalizacion,"%Y-%m-%d")

    def __str__(self):
        """
        Genera una cadena de texto con todos los datos de la tarea
        """
        resultado=f"> Categoria: {self.categoria}\n"
        resultado+=f"   > Tarea: {self.nombre}\n"
        resultado+=f"   > Fecha vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}\n"

        # Sólo mostramos la fecha de finalización si está terminada
        if (self.terminada=="S"):
            resultado+=f"   > Tarea terminada el: {self.fecha_finalizacion.strftime('%Y-%m-%d')}\n"
        return resultado        
    
    def texto_guardar(self)->str:
        """
        Genera una cadena de texto a utilizar para guardar la tarea en disco
        """
        resultado=f"{self.categoria}\n"
        resultado+=f"{self.nombre}\n"
        resultado+=f"{self.fecha_vencimiento.strftime('%Y-%m-%d')}\n"
        resultado+=f"{self.terminada}\n"

        # Sólo guardamos fecha de finalización si la tarea está terminada
        if(self.terminada=="S"):
            resultado+=f"{self.fecha_finalizacion.strftime('%Y-%m-%d')}\n"
        else:
            # Importante, aunque no haya fecha hay que dejar un espacio vacío
            resultado+="\n"

        return resultado
    
    def completar(self):
        """
        Marca una tarea como completada. La fecha de finalización
        será la del momento en el que se completa
        """
        self.terminada="S"
        self.fecha_finalizacion=datetime.datetime.now()
    
class ListaTareas:
    """
    Clase que implementa la lógica necesaria para gestionar una lista de tareas
    """
    # Ruta del archivo donde guardaremos las tareas
    ARCHIVO:str=r"C:\Users\ANTONIO\Google Drive\PROYECTOS PERSONALES\LIBROS APRENDE EN UN FIN DE SEMANA\PROGRAMACIÓN\src\3.8 PROYECTO\tareas.txt"

    # Objeto lista donde guardaremos las tareas
    lista_tareas:list

    def __init__(self):
        """
        Constructor de la clase. Símplemente inicializa el atributo lista_tareas
        """
        self.lista_tareas=list()

    def nueva_tarea(self,categoria:str, nombre:str, fecha_vencimiento:str, terminada:str="N", fecha_finalizacion:str=None):
        """
        Crea un nuevo objeto Tarea y lo guarda en lista_tareas
        """
        tarea=Tarea(categoria,nombre,fecha_vencimiento,terminada,fecha_finalizacion)
        self.lista_tareas.append(tarea)        

    def mostrar_tareas(self, estado:str):
        """
        Muestra la lista de tareas (T:Todas, C:Completadas, P:Pendientes)
        Para mostrar la lista de tareas nos apoyamos en el método __str__ de cada tarea
        """

        if estado=="T":
            resultado=f"** LISTA DE TODAS LAS TAREAS **\n"
        elif estado=="P":
            resultado=f"** LISTA DE TAREAS PENDIENTES **\n"
        else:
            resultado=f"** LISTA DE TAREAS COMPLETADAS **\n"
        
        # Recorremos las tareas
        
        # Utilizamos un índice auxiliar para indicar el orden de la tarea en la lista
        i=0
        for t in self.lista_tareas:

            # Mostramos las tareas según el parámetro. Las tareas se muestran
            # * Si quiero mostrar todas (estado = T)
            # * Si busco completadas (estado = C), sólo aquellas marcadas como terminadas
            # * Si busco pendientes (estado = P), sólo aquellas pendientes
            if((estado=="T") or  (estado=="C" and t.terminada=="S") or (estado=="P" and t.terminada=="N")):
                
                # Mostramos el índice de la tarea
                resultado+=f"[{i}]\n"

                # Mostramos la tarea aprovechando su método __str__
                resultado+=t.__str__()

            i+=1
        
        # Devolvemos la cadena de texto formada
        print(resultado)         

    def texto_guardar(self)->str:
        """
        Genera una cadena de texto a utilizar para guardar la lista de tareas en disco
        """
        resultado=""

        # Nos apoyamos en el método texto_guardar de cada Tarea
        for t in self.lista_tareas:
            resultado+=t.texto_guardar()

        return resultado

    def guardar_lista(self):
        """
        Método que guarda la lista en disco
        """

        # Generamos la cadena de texto que representa la lista
        texto=self.texto_guardar()

        # Abrimos el archivo en modo sobreescribir
        archivo=open(self.ARCHIVO
            ,mode="w"
            ,encoding="UTF-8")
        
        # Guardamos el texto en el archivo
        archivo.write(texto)    

    def recuperar_lista(self):
        """
        Método que recupera una lista de tareas a partir de un fichero
        """
        archivo=open(self.ARCHIVO
            ,mode="r"
            ,encoding="UTF-8")
        
        # Recorremos el fichero teniendo en cuenta
        # que cada tarea ocupa 5 líneas

        # En vez de hacer el control con el método
        # archivo.readline() y comprobando que hemos
        # leído algo, lo haremos con bloques de 5 líneas

        # Variable para controlar el bucle
        mas_tareas=True
       
        while(mas_tareas):

            # Leemos una línea del fichero. Si encontramos valor
            # es que hay una tarea
            categoria=archivo.readline().strip()

            if(categoria):

                # Leemos el resto de valores
                nombre=archivo.readline().strip()
                fecha_vencimiento=archivo.readline().strip()
                terminada=archivo.readline().strip()
                fecha_finalizacion=archivo.readline().strip()

                # Guardamos la tarea
                self.nueva_tarea(categoria,nombre,fecha_vencimiento,terminada,fecha_finalizacion)                

            else:
                mas_tareas=False    

    def buscar_tarea(self,buscado:str)->list():
        resultado=list()

        # Recorremos la lista y buscamos el texto buscado en el nombre
        # de cada tarea
        for t in self.lista_tareas:
            if buscado.upper() in t.nombre.upper():
                resultado.append(t)

        return resultado
