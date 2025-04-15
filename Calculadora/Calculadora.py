import math

print("Calculadora Básica en Python")

def suma(n1,n2):
    s=n1+n2
    print (s)

def resta(n1,n2):
    r=n1-n2
    print (r)

def mult(n1,n2):
    m=n1*n2;

def menu ():
    print("1-.Suma")
    print("2-.Resta")
    print("3-.Multiplicación")

while True:
    menu()

    opera = int(input("Ingresa el numero de Operación: "))
    if opera == 1:
        print("Suma")
        n1=int(input("Ingrese n1:"))
        n2=int(input("Ingrese n2:"))
        suma(n1,n2)
    elif opera == 2:
        print("resta")
        n1=int(input("Ingrese n1:"))
        n2=int(input("Ingrese n2:"))
        resta(n1,n2)
else: 
    print("hola")