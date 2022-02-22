from Piso import Piso

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

    def mostrarpiso(self):
        tmp = self.inicio
        while tmp is not None:
            print("Nombre del piso: ", tmp.nombre)
            tmp = tmp.siguiente    