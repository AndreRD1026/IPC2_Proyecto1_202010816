import imp
from Piso import Piso
from Patron import Patron

class listasimple():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def crearpiso(self,nombre):
        nuevo = Piso(nombre)
        self.size +=1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        
    def crearfilas(self,r):
        nuevo = Piso(r)
        self.size +=1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def crearcolumnas(self,c):
        nuevo = Piso(c)
        self.size +=1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def crearflip_costo(self,f):
        nuevo = Piso(f)
        self.size +=1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def crearslide_costo(self,s):
        nuevo = Piso(s)
        self.size +=1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarpiso(self):
        tmp = self.inicio
        while tmp is not None:
            print("Nombre del piso: ", tmp.nombre)
            print("Filas: ", tmp.filas)
            print("Columnas: " , tmp.columnas)
            print("Costo Flip:", tmp.flip_costo)
            print("Costo Slide:", tmp.slide_costo)
            #print("Nombre del patron: ", tmp.cod)
            #print("Patron: ", tmp.cadena)
            tmp = tmp.siguiente    

    def mostrarpatron(self):
        tmp = self.inicio
        while tmp is not None:
            print("Nombre del patron: ", tmp.cod)
            print("Patron: ", tmp.cadena)
            tmp = tmp.siguiente    

    def buscarPiso(self,nombre):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp 
            tmp = tmp.siguiente
        return None

    def buscarCodigo(self,cod):
        tmp = self.inicio
        while tmp is not None:
            if tmp.cod == cod:
                return tmp 
            tmp = tmp.siguiente
        return None

    def agregar(self, nombre, r, c, f, s):
        nuevoPiso = Piso(nombre, r, c, f,s)
        self.size +=1
        if self.inicio == None:
            self.inicio = nuevoPiso
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevoPiso

    def agregarpatron(self, cod,cadena):
        nuevoPatron = Patron(cod,cadena)
        self.size +=1
        if self.inicio == None:
            self.inicio = nuevoPatron
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevoPatron

 
    def getPiso(self,posicion):
        contador = 1
        tmp = self.inicio
        while tmp is not None:
            if contador is posicion:
                return tmp
            tmp = tmp.siguiente
            contador +=1
        return None

    
    def mostrarelementos(self):
        tmp = self.inicio
        while tmp is not None:
            print("Piso: " + tmp.nombre)
            print("Matriz del Piso - Dimensión " , tmp.matrizpiso.r, "X", tmp.matrizpiso.c , "Y")
            tmp = tmp.siguiente