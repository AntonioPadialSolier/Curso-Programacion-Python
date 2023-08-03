valor1 = int(input("Dime un número del 1 al 100: "))
valor2 = int(input("Dime otro número del 1 al 100: "))
if ((valor1>=1) and (valor1<=100) and (valor2>=1) and (valor2<=100)):
    print("Muy bien, ambos números están entre 1 y 100")
if ((valor1<1) or (valor1>100) or (valor2<1) or (valor2>100)):
    print("Los valores no son correctos. Fin del programa")


print("Versión mejorada utilizando ""if - else""")
valor1 = int(input("Dime un número del 1 al 100: "))
valor2 = int(input("Dime otro número del 1 al 100: "))
if ((valor1>=1) and (valor1<=100) and (valor2>=1) and (valor2<=100)):
    print("Muy bien, ambos números están entre 1 y 100")
else:
    print("Los valores no son correctos. Fin del programa")
