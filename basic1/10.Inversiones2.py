c=float(input("Ingrese la cantidad a invertir: "))
a=int(input("Ingrese el numero de años: "))
z=float(input("Ingrese el interes %:"))


for i in range (a):
    c *= 1 + z/100 #convertimos el porcentaje a decimal 
    #usamos la misma var

    print(f"Balance {i+1} : {round(c,2)} ")
    #usamos la iteracion para el balance  y yl res
    #formateado {func()}