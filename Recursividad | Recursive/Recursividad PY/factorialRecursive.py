#-*- coding: utf-8 -*-

import random

class Recursive: 
    def __init__(self):
        pass

    #Factorial Recursivo
    def factorial(self, num):
        if(num < 2):
            return 1
        else:
            return num * self.factorial(num - 1)
    
    #Fibonacci Recursivo
    def fibonacci(self, num):
        if(num == 0 or num == 1):
            return num
        recursion = self.fibonacci(num - 2) + self.fibonacci(num - 1)
        return recursion

    #Generar valores Random
    def randomInt(self, min = 0, max = 10):
        r = random.random()
        return int(r * (max-min) + min)

# ------------------------ TEST ------------------------
recursividad = Recursive()
numRandom = recursividad.randomInt()

#Entrada de datos
print('---------------- Recursividad ----------------')
respuesta = int(input("\n1. Factorial \n2.Fibonacci \nIngrese el valor de la operacion a ejecutar "))
modo = int(input("\n1. Manual \n2. Automatica \nManera a efectuar "))

# --------------------- Decisiones ---------------------
#Condiciones Factorial
if(respuesta == 1):
    if(modo == 1):
        numFact = int(input("\nIngrese un numero: "))
        print("\nEl factorial de %s es %s" %(numFact, recursividad.factorial(numFact)))
    else:
        print("\nEl factorial de %s es %s" %(numRandom, recursividad.factorial(numRandom)))
elif(respuesta == 2):
    if(modo == 1):
        numFib = int(input("\nIngrese un numero: "))
        print("\nEl fibonacci de %s es %s" %(numFib, recursividad.fibonacci(numFib)))
    else:
        print("\nEl fibonacci de %s es %s" %(numRandom, recursividad.fibonacci(numRandom)))
    
else: 
    print('El dato introducido no es valido')
        