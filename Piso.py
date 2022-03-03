from ListaPatrones import ListaPatrones
from Matriz import Matriz

class Piso(): 
    def __init__(self, nombre,r,c,f, s,cod,cadena):
        self.nombre = nombre
        self.filas = r
        self.columnas = c
        self.flip_costo = f
        self.slide_costo = s
        self.cod = cod
        self.cadena = cadena
        #self.patrones = ListaPatrones()
        self.matrizpiso = Matriz() #Matriz
        self.siguiente = None
