original=input("Escribe un texto para que lo pueda manipular: ")

print("En mayúsculas:",original.upper())
print("En minúsculas:",original.lower())
print("Cambiando la letra 'a' por la 'e'", original.replace('a','e'))

original=input("Escribe un número (puedes intengar engañarme si quieres): ")

if(original.isnumeric()):
    print("Muy bien, has escrito el número:", original)
else:
    print("Has hecho trampas,",original,"no es un número")

# Vamos a probar ahora la función split
original="Vamos a separar, este texto, y a recorrarelo, como si fuera, una lista"

lista_frases=original.split(",")
i=0
while(i<len(lista_frases)):
    print("[",i,"]:",lista_frases[i])
    i+=1

# Vamos a probar ahora las distintas versiones de split
texto_con_espacios="    Hola Mundo     "
print("*",texto_con_espacios.strip(),"*")
print("*",texto_con_espacios.lstrip(),"*")
print("*",texto_con_espacios.rstrip(),"*")

# Y finalmente find / in
frase=input("Escribe una frase que contenga la palabra 'casa': ")

# In devuelve True / False en función de si la palabra está
# dentro del texto
if('casa' in frase):
    print("Muy bien, en tu frase aparece la plabra 'casa'")
    print("Vamos a ver ahora en qué posición está...")

    # Por su parte find, devuelve la primera posición donde apareza
    posicion=frase.find('casa')
    print("...'casa' está en la posición",str(posicion))
else:
    print("Vaya, en tu frase no aparece la palabra 'casa'")