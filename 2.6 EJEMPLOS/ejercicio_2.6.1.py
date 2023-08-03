numeroA=int(input("Elige un número entre 0 y 100: "))
print("Es par", (numeroA%2)==0)
print("Es impar", (numeroA%2)!=0)

numeroB=int(input("Elige otro número entre 0 y 100: "))
print("Los números son iguales", numeroA==numeroB)
print("La suma es par", ((numeroA+numeroB)%2)==0)
print("La suma es ipar", ((numeroA+numeroB)%2)!=0)
