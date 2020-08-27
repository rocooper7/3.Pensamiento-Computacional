class Coordenada:

    def __init__(self, x, y): 
        self.x = x
        self.y = y
    
    def mover(self, delta_x, delta_y): #  Regresa una nueva coordenada con la suma de la coordenada actual + tuplas aleatorias 
        return Coordenada(self.x + delta_x, self.y + delta_y) 
        
    
    def distancia(self, otra_coordenada):    #Se calcula la distancia entre dos coordenadas, origen y final del borracho
        delta_x = self.x - otra_coordenada.x 
        delta_y = self.y - otra_coordenada.y 

        return(delta_x**2 + delta_y**2)**0.5



        