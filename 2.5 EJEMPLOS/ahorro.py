ahorro=int(input("¿Cuánto dinero tenías en la cartera el lunes? "))

gastos=int(input("¿Cuánto gastaste el lunes? "))
gastos+=int(input("¿Cuánto gastaste el martes? "))
gastos+=int(input("¿Cuánto gastaste el miércoles? "))
gastos+=int(input("¿Cuánto gastaste el jueves? "))
gastos+=int(input("¿Cuánto gastaste el viernes? "))

print("Te has gastado",gastos,"€ entre semana")
print("Te quedan", ahorro-gastos, "€ para el fin de semana")
