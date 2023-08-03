def conversacion():
    saludo()
    pregunta()

def saludo():
    print("Hola. Me encanta aprender Python")

def pregunta():
    respuesta = input("Cuál es tu hobby?: ")
    print("¡Qué bien! A mi también me gusta", respuesta)

conversacion()
