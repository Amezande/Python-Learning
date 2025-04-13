##Concatena, convierte formato, redondea
a=float(input("Cantidad depositada en la cuenta de ahorros:"))
b=float(input("Interes al que lo metió al año:"))
c1=a*(1+b)
c2=c1*(1+b)
c3=c2*(1+b)

print("Balance1: " + str(round(c1, 2)))
print("Balance2: " + str(round(c2, 2)))
print("Balance3: " + str(round(c3, 2)))
