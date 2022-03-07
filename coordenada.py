import os
import webbrowser

from matplotlib.pyplot import contour

class nodoCoordenada:
    def __init__(self, r= None, c = None,patron = None, aux = None, titulo = None):
        self.r = r
        self.c = c
        self.patron = patron
        self.aux = aux
        self.titulo = titulo
        self.siguiente = None
        self.Anterior = None

    def getR(self):
        return self.r
    def setR(self, r):
        self.r = r
    def getC(self):
        return self.c
    def setC(self, c):
        self.c = c
    def getAux(self):
        return self.aux
    def setAux(self,aux):
        self.aux = aux


class Lista_Coordenadas:
    def __init__(self):
        self.raiz = nodoCoordenada()
        self.ultimo = self.raiz

    def insertar(self,nuevonodo):
        if self.raiz.r is None:
            self.raiz = nuevonodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevonodo
            nuevonodo.anterior = self.raiz
            self.ultimo = nuevonodo
        else:
            self.ultimo.siguiente = nuevonodo
            nuevonodo.anterior = self.ultimo
            self.ultimo=nuevonodo

    def recorrer(self):
        actual = self.raiz
        cadena = ''
        while True:
            if actual.r is not None:
                #cadena += " Coordenada en x: " + str(actual.r)+ " Coordenada en y: " + str(actual.c) + " patron del patron: "+ actual.patron
                cadena += "" + actual.patron
                if actual.siguiente is not None:
                    cadena +="\n"
                    actual = actual.siguiente
                else: 
                    break
            else:
                break
        print(cadena)


    def graficopatron(self):
        cont = 0
        cont1 = 0
        empieza = "-10"
        termina = "-11"
        aux = self.raiz
        grafo = "digraph G { \nrankdir = LR\n"
        grafo += 'label="Patron Final"\n'
        
        try:    
            while aux is not None:
                if str(aux.aux) == empieza:
                    grafo+="subgraph "
                    grafo+="{}".format(aux.patron)
                    grafo+= "{ \n"
                    aux_nombre = aux.patron
                    aux_filas1 = int(aux.r)
                    aux_col1=int(aux.c)
                    aux_titulo = aux.titulo
                    aux = aux.siguiente
                
                cont1+=1
                if aux.patron == "B" or aux.patron == "W":
                    if aux.patron == "B":
                        nombrecolor = "black"
                        colorpatron = "gray"
                    elif aux.patron == "W":
                        nombrecolor = "white"
                        colorpatron ="black"
                    grafo += '{}[label="{}",color = "black",fontcolor ="{}",fillcolor="{}",style="filled",shape="box"];\n'.format(cont1,aux.patron,colorpatron,nombrecolor)
                    cont+=1
                    aux=aux.siguiente
            
                if str(aux.aux) == termina:
                    grafo+="}\n"
                    aux = aux.siguiente 
            aux = self.raiz
            cont2 = 1
            cont3 = 0
            while aux is not None:
                if str(aux.aux) == empieza:
                    aux_filas2 = int(aux.r)
                    aux_col2=int(aux.c)
                    aux = aux.siguiente

                cont3 +=1
                if aux.patron == "B" or aux.patron == "W":
                    for i in range(cont):
                        if(cont2 == 1 or cont2 == (cont/2)+1):
                            grafo += "\nsubgraph cluster_" + "{\nlabel=\""+ ("Patron Inicial" )+ "\"\nrankdir=TB\n"
                        if(cont2 == cont/2):
                            grafo += "\n}"
                        if cont2%aux_col2 == 0:
                            cont2+=1
                            continue
                        elif cont2 < (cont):
                            grafo += '{}->{};\n'.format(cont2,cont2+1)
                            cont2+=1
                    #grafo += "}"
                    aux=aux.siguiente
                if str(aux.aux) == termina:
                    aux = aux.siguiente
            grafo+="}"
            grafo+= "}"    

            dotdocument="Piso_"+str(aux_titulo)+".dot"
            with open(dotdocument,'w') as grafica: 
        
                grafica.write(grafo)
            pdf="Piso_"+str(aux_titulo)+".pdf"
            os.system("dot -Tpdf "+dotdocument+" -o "+pdf)
            webbrowser.open(pdf)

        except:
            print("Error")