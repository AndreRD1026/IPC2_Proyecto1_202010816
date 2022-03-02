from Piso import Piso
from ListaPatrones import ListaPatrones

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
            tmp = tmp.siguiente    

    def mostrarpatron(self):
        tmp = self.inicio
        while tmp is not None:
            print("Nombre del patron: ", tmp.codigo)
            print("Patron: ", tmp.patron)
            tmp = tmp.siguiente    

    def buscarPiso(self,nombre):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre == nombre:
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


    def getpatron(self, codigo,patron):
        nuevoPatron = ListaPatrones(codigo,patron)
        self.size +=1
        if self.inicio == None:
            self.inicio = nuevoPatron
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevoPatron

    
    def mostrarelementos(self):
        tmp = self.inicio
        while tmp is not None:
            print("Piso: " + tmp.nombre)
            print("Matriz del Piso - Dimensión " , tmp.matrizpiso.r, "X", tmp.matrizpiso.c , "Y")
            tmp = tmp.siguiente