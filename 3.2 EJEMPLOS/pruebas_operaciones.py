import datetime

txt_fecha=input("¿En qué día naciste [YYYY-MM-DD]: ")
fecha_nacimiento=datetime.datetime.strptime(txt_fecha,'%Y-%m-%d')

ahora=datetime.datetime.now()

diferencia = ahora - fecha_nacimiento
print(f">> {type(diferencia)} <<")
print(f"Hasta hoy has vivido {ahora-fecha_nacimiento}.")

txt_fecha_2=input("Dime una fecha y te diré cuántos años tendrás [YYYY-MM-DD]: ")
fecha_calculo=datetime.datetime.strptime(txt_fecha_2,'%Y-%m-%d')
edad_futura=fecha_calculo-fecha_nacimiento

print(f"En {txt_fecha_2} tendrás {edad_futura.days//365} años.")
print(edad_futura)

dias=int(input("Dime un número de días y te diré qué día de la semana será: "))
incremento_dias=datetime.timedelta(days=dias)

nuevo_dia=ahora+incremento_dias
print(F"Dentro de {dias} días será {nuevo_dia.strftime('%A')}")