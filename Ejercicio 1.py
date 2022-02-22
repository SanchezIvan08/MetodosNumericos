print("Primer Método")
import math
x=int (input("Ingrese a qué potencia desea elevar euler:"))
n = int (input("Ingrese el valor de n: "))
def funcion_exponencial(x):
    suma=0
    for n in range(0, 50):
        suma += math.pow(x,n)/math.factorial(n)
    return suma

print('Resultado con la funcion_exponencial: ',funcion_exponencial(x))
print('Resultado con la funcion math.exp: ',math.exp(n))



print("Segundo método")
import math 

def aproximar_valor(x, pot):
    
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

# Valor real de e^x
e_x = round(math.exp(x), 4)
print("Valor real de e: ", e_x)

# Imprimimos la aproximación
print("Valor aproximado: ", aproximar_valor(x, 1))



print("Tercer método")
x=int (input("Ingresa la potencia a elevar euler:"))
n = int (input("Ingresa el valor de n:"))
fact=1
i=1
acumulador=0
while(i<=n):
    fact=fact*i
    elevar = pow (x,i)
    division = elevar / fact
    acumulador+=division
    i=i+1
print("")
print ("el valor del factorial es", acumulador+1)