def calcular_gastos(divisa:str,**gastos:int):
    """Función que calcula el total de gastos recibido por parámetro en parejas "concepto de gasto=importe"
    * moneda: Tipo de moneda utilizada (por defecto €).
    * gastos: parejas "concepto-gasto"
    """

    importe_total=0
    num_conceptos=len(gastos)

    for concepto in gastos.keys():
        importe_total+=gastos[concepto]

    print("Has registrado",num_conceptos,"conceptos de gasto por un total de:", importe_total, divisa)

calcular_gastos(divisa="€", supermercado=600, luz=80, ocio=150)
