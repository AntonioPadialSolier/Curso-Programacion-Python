valor1 = int(input("Dime un número entre 0 y 100: "))
if(valor1<0 or valor1>100):
    print("Lo siento, el número no es correcto")
elif(valor1==0):
    print("El 0 no es divisible por ningún número")
else:
    if(valor1%6==0):
        print("Es divisible entre 6")
    if(valor1%5==0):
        print("Es divisible entre 5")
    if(valor1%4==0):
        print("Es divisible entre 4")
    if(valor1%3==0):
        print("Es divisible entre 3")
    if(valor1%2==0):
        print("Es divisible entre 2")
    print("Es divisible entre 1")  