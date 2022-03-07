class Coordenada:
    def __init__(self, fila, columna,cadena):
        self.fila = fila
        self.columna = columna
        self.cadena = cadena
        self.etiqueta = None
        self.terminal = False
        self.up = None
        self.down = None
        self.left = None
        self.right = None


class Header:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None

class listaHeaders:
    def __init__(self):
        self.inicio = None
        self.long = 0
    def nuevoHeader(self, id):
        nuevo = Header(id)
        if self.inicio is None:
            self.inicio = nuevo
        elif nuevo.id < self.inicio.id:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                if nuevo.id < tmp.siguiente.id:
                    nuevo.siguiente = tmp.siguiente
                    nuevo.anterior = tmp
                    tmp.siguiente.anterior = nuevo
                    tmp.siguiente = nuevo
                    break
                tmp = tmp.siguiente
            if tmp.siguiente is None:
                nuevo.anterior = tmp
                tmp.siguiente = nuevo
        self.long +=1
    def getHeader(self,id):
        tmp = self.inicio
        while tmp is not None:
            if tmp.id is id:
                return tmp
            tmp = tmp.siguiente
        return None


class Matriz:
    def __init__(self):
        self.filas = listaHeaders()
        self.columnas = listaHeaders()
        self.r=0
        self.c=0


    def agregarCoordenada(self,fila,columna,cadena):
        nuevaCoordenada = Coordenada(fila,columna,cadena)
        #insertando el nodo en la fila correspondiente
        efila = self.filas.getHeader(fila)
        if efila is None: #si no existe la fila todavía
            self.filas.nuevoHeader(fila)
            self.filas.getHeader(fila).acceso = nuevaCoordenada

        else: #si la fila ya existe
            tmp = efila.acceso
            if (nuevaCoordenada.columna < tmp.columna): #si hay que insertar al inicio
                tmp.left = nuevaCoordenada
                nuevaCoordenada.right = tmp
                fila.acceso = nuevaCoordenada

            else:
                while tmp.right is not None:
                    if nuevaCoordenada.columna < tmp.right.columna: #si hay que instertar al medio
                        nuevaCoordenada.right = tmp.right
                        tmp.right.left = nuevaCoordenada
                        nuevaCoordenada.left = tmp
                        tmp.right = nuevaCoordenada
                    tmp = tmp.right
                if tmp.right is None:
                    nuevaCoordenada.left = tmp
                    tmp.right = nuevaCoordenada

        #insertando el nodo en la columna correspondiente
        ecolumna = self.columnas.getHeader(columna)
        if ecolumna is None: #si no existe la columna todavía
            self.columnas.nuevoHeader(columna)
            self.columnas.getHeader(columna).acceso = nuevaCoordenada
        else: #si la fila ya existe
            tmp = ecolumna.acceso
            if (nuevaCoordenada.columna < tmp.columna): #si hay que insertar al inicio
                tmp.up = nuevaCoordenada
                nuevaCoordenada.down = tmp
                columna.acceso = nuevaCoordenada
            else:
                while tmp.down is not None:
                    if nuevaCoordenada.fila < tmp.down.fila: #si hay que instertar al medio
                        nuevaCoordenada.down = tmp.down
                        tmp.down.up = nuevaCoordenada
                        nuevaCoordenada.up = tmp
                        tmp.down = nuevaCoordenada
                    tmp = tmp.down
                if tmp.down is None:
                    nuevaCoordenada.up = tmp
                    tmp.down = nuevaCoordenada

        self.r = self.filas.long
        self.c = self.columnas.long

    def recorrerFilas(self):
        tmp = self.filas.inicio
        while(tmp is not None):
            nodoTmp = tmp.acceso
            while(nodoTmp is not None):
                print("[(",nodoTmp.fila, ", ", nodoTmp.columna, ",", nodoTmp.cadena, "]")
                nodoTmp = nodoTmp.right
            tmp = tmp.siguiente

    def recorrerColumnas(self):
        tmp = self.columnas.inicio
        while(tmp is not None):
            nodoTmp = tmp.acceso
            while(nodoTmp is not None):
                print("[(",nodoTmp.fila, ", ", nodoTmp.columna, nodoTmp.cadena, "]")
                nodoTmp = nodoTmp.down
            tmp = tmp.siguiente      

    def getNodo(self,fila,columna):
        tmp = self.filas.inicio
        while(tmp is not None):
            nodoTmp = tmp.acceso
            while(nodoTmp is not None):
                if(nodoTmp.fila is fila and nodoTmp.columna is columna):
                    return nodoTmp
                nodoTmp = nodoTmp.right
            tmp = tmp.siguiente
        return None

