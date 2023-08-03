valor1 = int(input("Dime un número entre 1 y 100 y averiguaré si es par o impar: "))
if(valor1<1 or valor1>100):
    print("Lo siento, sólo conozco los números del 1 al 100")
else:
    if(valor1%2==0):
        print("Es par")
    else:
        print("Es impar") 

print("Versión mejorada utilizando ""elif""")
valor1 = int(input("Dime un número entre 1 y 100 y averiguaré si es par o impar: "))
if(valor1<1 or valor1>100):
    print("Lo siento, sólo conozco los números del 1 al 100")
elif(valor1%2==0):
    print("Es par")
else:
    print("Es impar")
