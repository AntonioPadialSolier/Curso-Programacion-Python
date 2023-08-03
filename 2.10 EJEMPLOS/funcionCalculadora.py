def calculadora_lista(gastos:list):
    total=0

    for importe in gastos:
        total+=importe

    print("Este mes te has gastado:", total, "€")

def calculadora_argumento(*gasto:int):
    total=0

    for importe in gasto:
        total+=importe

    print("Este mes te has gastado:", total, "€")

def calculadora_divisa(*gasto:int, divisa:str):  
    total=0

    for importe in gasto:
        total+=importe

    print("Este mes te has gastado:", total, divisa) 

calculadora_lista([99, 456, 699, 45, 345])

calculadora_argumento(99, 456, 699, 45, 345)

calculadora_divisa(99, 456, 699, 45, 345, divisa="€")
