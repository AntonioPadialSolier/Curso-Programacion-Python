def solicitar_valores()->list:
    """Función que solicita una lista de valores por línea de comando.
    Termina cuando el usuario introduce el valor 0
    * return: lista de valores"""
    
    # Lista donde iremos agregando los valores
    valores=list()

    # Inicializamos la variable que utilizaremos en el bucle
    valor=None

    # Solicitamos valores hasta leer 0
    while(valor!=0):

        valor=int(input("Introduce un valor: "))

        # Sólo lo añadimos a la lista si no es 9
        if(valor!=0):
            valores.append(valor)

    return valores

def agregar_importes(saldo_inicial:int, operacion:str, valores:list)->int:
    """Agrega los importes recibidos por parámetro en función del tipo de operación indicada
    por el usuario (suma o resta).
    * saldo_inicial: saldo inicial al que se sumarán o restarán los valores
    * operacion: tipo de operación. Puede ser "suma" o "resta"
    * valores: lista de valores a sumar
    * return: resultado final"""

    # Guardamos el resultado en una variable
    resultado=saldo_inicial

    # Recorremos la lista de valores
    for valor in valores:
        if(operacion=="suma"):
            resultado+=valor
        else:
            resultado-=valor

    # Devolvemos el resultado
    return resultado

# En primer lugar, solicitamos el saldo inicial
print("Hola. Vamos a calcular el saldo a final de año.")
saldo_inicial=int(input("En primer lugar. ¿Cuál era el saldo al inicio del año?: "))

# A continuación utilizamos una función para leer los ingresos
print("Introduce ahora todos los ingresos del año. Para parar escribe el valor 0")
ingresos=solicitar_valores()

# Y la misma para los gastos
print("Introduce ahora todos los gastos del año. Para parar escribe el valor 0")
gastos=solicitar_valores()

# Ordenamos ambas listas para poder buscar los de mayor cuantía
# En orden inverso para que el primero sea el mayor
ingresos.sort(reverse=True)
gastos.sort(reverse=True)

# Sumamos los ingresos a saldo_inicial
saldo_final = agregar_importes(saldo_inicial,"suma",ingresos)

# Y ahora los gastos a saldo_final
saldo_final = agregar_importes(saldo_final, "resta", gastos)

#Presentamos resultados
print("El saldo a final de año es:", saldo_final)
print("En total has hecho", len(ingresos), "ingresos")
print("Y",len(gastos),"gastos")

print("El ingreso de mayor cuantía ha sido de:",ingresos[0])
print("Y el mayor gasto:",gastos[0])
