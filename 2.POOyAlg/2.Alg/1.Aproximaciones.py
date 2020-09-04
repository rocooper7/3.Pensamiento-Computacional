import sys
import time

def factorial(n): #Metodo iterativo
    respuesta = 1 

    while n > 1:
        respuesta *= n  #respuesta = respuesta * n 
        n -= 1

    return respuesta

def factorial_2(n):  #Metodo Recursivo
    if n == 1:
        return 1
    
    return n * factorial_2(n - 1)

if __name__ == '__main__':
    #print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500) # n es el nuevo límite a establecer

    n = 1000

    comienzo = time.time()
    final = time.time()
    print(final - comienzo) #0.0 segundos

    comienzo = time.time()
    factorial_2(n)
    final = time.time()
    print(final - comienzo) #0.0009 segundos


