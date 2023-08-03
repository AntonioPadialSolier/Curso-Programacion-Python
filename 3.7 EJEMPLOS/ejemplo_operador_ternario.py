# Vamos a probar el operador ternario
# Solicitaremos 10 números y los:
# * sumaremos si son pares
# * restaremos si son impares
total=0
i=0
while(i<10):

    valor=int(input("¿Qué numero quieres sumar o restar?: "))

    total=total + valor if valor%2==0 else total - valor    
    i+=1

print(f"El resultado es: {total}")
