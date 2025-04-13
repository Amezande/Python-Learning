#Compras por peso
p=112;
m=75;

a= int(input("¿Cuántos payasos comprará?"))
b= int(input("¿Cuántas muñecas desea comprar?"))
pa= a*p
mb= b*m
pt= (pa + mb) / 1000 
print("Comprará: ", a ," Payasos", b ,"Muñecas, su paquete pesa", pt, "kg")
