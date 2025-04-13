a=float(input("Ingrses su peso en KG: "))
b=float(input("Ingrese su estatura en metros"))
imc = round(a/b**2,2) 
#Para redondear los decimales round(op,2) o cantidad de numeros 
#que desee presentar
print(imc)
