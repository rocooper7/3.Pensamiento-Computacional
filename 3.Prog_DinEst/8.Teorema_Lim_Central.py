import random
from bokeh.plotting import figure,show
import collections
from estadisticas import desviacion_estandar,media

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros=[]

    for _ in range(numero_de_tiros):
        tiro_1=random.choice([1,2,3,4,5,6])
        tiro_2=random.choice([1,2,3,4,5,6])
        
        secuencia_de_tiros.append(tiro_1+tiro_2)

    return secuencia_de_tiros

def graficar(x,y):
    grafica=figure(title='Distribucion normal',x_axis_label='sigma',y_axis_label='valores')
    grafica.vbar(x,top=y ,width = 0.8,legend='Distribucion normal')
    show(grafica)



def main(numero_de_tiros,numero_de_intentos):
    X=[] #Almacenaremos los resultados de las veces que corramos la simulacion
    
    
    for _ in range(numero_de_intentos):
        secuencia_de_tiros=tirar_dado(numero_de_tiros)
        X.append(media(secuencia_de_tiros)) #Añadimos la secuencia al arreglod e tiros

 
    counter = dict(collections.Counter(X))
 
    x=list(counter.keys()) #Para X iran las letras es decir, sigma1 sigma 2 etc
 
    y=list(counter.values()) #Para Y iran los valores de las medias
 
    graficar(x,y)

if __name__ == "__main__":

    numero_de_tiros=int(input('Cuantos tiros del dado: '))
    numero_de_intentos=int(input('Cuantos intentos quieres hacer?: '))

    main(numero_de_tiros,numero_de_intentos)