from ListaPatrones import ListaPatrones

class Patron():
    def __init__(self, cod, cadena):
        self.cod = cod
        self.cadena = cadena
        self.siguiente = None