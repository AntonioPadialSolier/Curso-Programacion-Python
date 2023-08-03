import datetime

# Fecha (sólo año, mes, día)
fecha=datetime.datetime(2022,10,18)
print(fecha)

# Hora
fecha=datetime.datetime(1,1,1,hour=18, minute=34, second=00)
print(fecha)

# Fecha errónea
# fecha=datetime.datetime(2022,2,29)
# print(fecha)

# Fecha (sólo año, mes, día)
fecha=datetime.datetime.strptime('2022-10-18','%Y-%m-%d')
print(fecha)

# Hora
hora=datetime.datetime.strptime('18:34:00','%H:%M:%S')
print(hora)

# Fecha errónea
# fecha=datetime.datetime.strptime('2022-02-29','%Y-%m-%d')
# print(fecha)