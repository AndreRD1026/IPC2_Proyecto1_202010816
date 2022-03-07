#from ListaPatrones import ListaPatrones
from ListaPatrones import Listad_Patrones
from Matriz import Matriz
from coordenada import Lista_Coordenadas

class Piso(): 
    def __init__(self, nombre,r,c,f, s):
        self.nombre = nombre
        self.filas = r
        self.columnas = c
        self.flip_costo = f
        self.slide_costo = s
        self.patrones = Listad_Patrones()
        self.coordenadas = Lista_Coordenadas()
        #self.matrizpiso = Matriz() #Matriz
        self.procesado = False
        self.siguiente = None
