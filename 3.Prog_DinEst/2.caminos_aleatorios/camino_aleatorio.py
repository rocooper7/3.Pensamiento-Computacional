from borracho import BorrachoTradicional 
from campo import Campo #campo es el modulo y Campo es la clase.
from coordenada import Coordenada 
from bokeh.plotting import figure,show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho) #cual es el inicion, nos  debe dar al inicio (0, 0)
     
    for _ in range(pasos): #10 pasos  el primer for de main 
        campo.mover_borracho(borracho) 
    return inicio.distancia(campo.obtener_coordenada(borracho))   #(mod coordenada) Distancias a las coordenadas finales

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    #llamada a tipo de borracho, a diferencia de llamarlo directamente como borracho tradicional, se lo recibe como parametro de la funcion
    # lo que se hace es inicializar una instancia de borracho tradicional o de cualquier tipo de borracho que se le mande. "agnostica" recibe un borracho, cualquie tipo.
    borracho = tipo_de_borracho(nombre="David") 
    origen = Coordenada(0, 0)
    distancias = []  #variable que guarda las distancias en cada una de las simulaciones.

    """por cada intento, el _ indica que no utilizaremos variable """
    for _ in range(numero_de_intentos):   #100
        campo = Campo() #simulacion 
        campo.añadir_borracho(borracho, origen) #se añade un borracho y un origen de coordenada. 
        simulacion_caminata = caminata(campo, borracho, pasos) #resultado de la funcion caminata, (todavia no esta implementada)
        distancias.append(round(simulacion_caminata, 1)) #añadir a las distancias la simulacion de la caminata, round permite que no tenga ningun decimal.
     
    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend_label='distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_medias_por_caminata = []

    for pasos in distancias_de_caminata: # 10, 100, 1000, 10000
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)             
        distancia_media = round(sum(distancias) / len(distancias), 4) #4 son 3 decimales, es la media de los datos.
        distancias_medias_por_caminata.append(distancia_media)
        distancia_maxima = max(distancias) #el dato maximo de la distancia
        distancia_minima = min(distancias)
        #__name__ nos da el nombre de la clase, 
        print(f"{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos")
        print(f"Media = {distancia_media}")
        print(f"Max = {distancia_maxima}")
        print(f"Min = {distancia_minima}")
    graficar(distancias_de_caminata,distancias_medias_por_caminata)
        
if __name__ == "__main__": #Entry point
    distancias_de_caminata = [10, 100, 1000, 10000] #simulacion de 10 pasos, 100 pasos, ... , 
    numero_de_intentos = 100           #las simulaciones se corren varias veces para obtener su media.
    
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)   # Recibe clase de borracho, en vez inizializar la clase la vamos a poner como referencia
    

    