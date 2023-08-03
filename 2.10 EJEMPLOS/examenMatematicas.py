def resultado_examen(respuesta_1, respuesta_2, respuesta_3, respuesta_4, respuesta_5):
    """Función que evalúa el resultado de un examen. Parámetros:
    * respuesta_1: Respuesta a la pregunta "¿Cuál es el resto de una división exacta?"
    * respuesta_2: Respuesta a la pregunta "¿Cuáles son los dos primeros decimales de la constante 'pi'?"
    * respuesta_3: Respuesta a la pregunta "¿Cuántos bytes hay en un kilobyte?"
    * respuesta_4: Respuesta a la pregunta "¿Cuánto es 1000 x 1000?"
    * respuesta_5: Respuesta a la pregunta "¿Cuántos días hay en un año bisiesto"
    """
    nota = 0
    if (respuesta_1 == 0):
        nota += 2
    if (respuesta_2 == 14):
        nota += 2
    if (respuesta_3 == 1024):
        nota += 2
    if (respuesta_4 == 1000000):
        nota += 2
    if (respuesta_5 == 366):
        nota += 2
    
    if nota >= 5:
        print("¡Enhorabuena! has aprobado con un", str(nota))
    else:
        print ("Lo siento, has suspendido con un", str(nota))

print("Hola, vamos a realizar un examen de matemáticas.")
respuesta_1 = int(input("Pregunta 1: ¿Cuál es el resto de una división exacta?: "))
respuesta_2 = int(input("Pregunta 2: ¿Cuáles son los dos primeros decimales de la constante 'pi'?: "))
respuesta_3 = int(input("Pregunta 3: ¿Cuántos bytes hay en un kilobyte?: "))
respuesta_4 = int(input("Pregunta 4: ¿Cuánto es 1000 x 1000?: "))
respuesta_5 = int(input("Pregunta 5: ¿Cuántos días hay en un año bisiesto: "))
resultado_examen(respuesta_1, respuesta_2, respuesta_3, respuesta_4, respuesta_5)