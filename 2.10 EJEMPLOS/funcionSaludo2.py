def conversacion():
    saludar()
    respuesta = input("Cuál es tu hobby?: ")
    responder(respuesta)

def saludar():
    print("Hola. Me encanta aprender Python")

def responder(hobby):
    print("¡Qué bien! A mi también me gusta", hobby)

conversacion()