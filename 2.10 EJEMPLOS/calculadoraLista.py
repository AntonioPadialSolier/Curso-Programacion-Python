def calculadora_divisa(*gastos:int, divisa:str):  
    total=0

    for gasto in gastos:
        total+=gasto

    print("Este mes te has gastado:", total, divisa) 

calculadora_divisa(99, 456, 699, 45, 345, divisa="€")
