class Campo:
    def __init__(self):  # Campo Crea el espacio en el que se va a mover el borracho 
        self.coordenadas_de_borrachos = {}

    def añadir_borracho(self, borracho, coordenada): 
        self.coordenadas_de_borrachos[borracho] = coordenada 

    def mover_borracho(self, borracho):     #cuando camina el borracho regresa una tupla, aleatorio.
        delta_x, delta_y = borracho.camina() 
        coordenada_actual = self.coordenadas_de_borrachos[borracho] 
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)  #Se vuelve a llamar la Clase Coordenada

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada      #guardamos nuevamente la coordenada del borracho en el diccionario.

    def obtener_coordenada(self, borracho):  #consulta de donde anda un borracho al final del programa.
        return self.coordenadas_de_borrachos[borracho] #devuelve el valor actual del diccionario.


        
         


         
         