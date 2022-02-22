
print("Primer Método")
import math
x=float (input("Ingrese a qué potencia desea elevar euler:"))
n = int (input("Ingrese el valor de n: "))
def funcion_exponencial(x):
    suma=0
    for n in range(0, 50):
        suma += math.pow(x,n)/math.factorial(n)
    return suma

print('Resultado con la funcion_exponencial: ',1/funcion_exponencial(x))
print('Resultado con la funcion math.exp: ',1/math.exp(n))



print("Segundo método")
import math 

def aproxim_valor(x, pot):
    
    suma = round(math.pow(x, pot) / math.factorial(pot) + 1, 4)
    aux = round(math.pow(x, pot) / math.factorial(pot) + 1, 5)

    while e_x > suma:

        pot += 1
        suma += math.pow(x, pot) / math.factorial(pot)
        suma = round(suma, 4)

        aux += math.pow(x, pot) / math.factorial(pot)
        aux = round(aux, 5)

    return aux

x = float(input("Ingrese el valor de x: "))

e_x = round(math.exp(x), 4)
print("Valor real de e: ", 1/e_x)

print("Valor aproximado: ", 1/aproxim_valor(x, 1))



print("Tercer método")
x=int (input("Ingrese a qué potencia desea elevar euler:"))
n = int (input("Ingrese el valor de n:"))
fact=1
i=1
acum=0
while(i<=n):
    fact=fact*i
    elevar = pow (x,i)
    division = (elevar / fact)
    acum+=division
    i=i+1
print ("Valor de la factorial es", 1/acum+1)