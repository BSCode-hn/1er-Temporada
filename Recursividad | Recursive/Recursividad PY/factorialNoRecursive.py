#-*- coding: utf-8 -*-
class NoRecursive: 
    def __init__(self):
        pass

    #Factorial ascendente
    def factorialAsc(self, num):
        result = 1
        #range(start, stop, step) sino se especifica step, step = 1
        for i in range(1,num +1):
            print("i=%s" %i)
            result = result*i
        return result

    #Factorial Descendente
    def factorialDes(self, num):
        result = 1
        for i in range(num, 0, -1):
            print("i=%s" %i)
            result = result*i
        return result

nr = NoRecursive()
#input se utiliza para guardar los datos introducidos por el usuario
num = int(input("Valor al que se obtendra el factorial: "))

print("El factorial de manera ascendente de %s es %s " %(num, nr.factorialAsc(num)))
print("\n")
print("El factorial de manera descendente de %s es %s " %(num, nr.factorialDes(num)))
