from re import L
import xml.etree.ElementTree as ET
from ListaPatrones import nodoDoblemente

from Piso import Piso
from Patron import Patron
from ListaSimple import listasimple as listapisos
from coordenada import Lista_Coordenadas
import graphviz

from coordenada import nodoCoordenada


archivo = ''
contenido = ''
tree = ''
root = ''
pisos = ''
pisoss = listapisos()
#patrones = listapisos()


def cargarArchivo(ruta):
    global root
    global tree
    global piso
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        id = 0
        nombre = elemento.attrib['nombre']
        buscarPiso = pisoss.buscarPiso(nombre)
        if buscarPiso is None:
            r = int(elemento.find('R').text)
            c = int(elemento.find('C').text)
            f = int(elemento.find('F').text)
            s = int(elemento.find('S').text)              
            pisoss.agregar(nombre,r,c,f,s)   
          
            piso = pisoss.buscarPiso(nombre)
    
            for subelemento in elemento.find('patrones'):
                id += 1
                nombrepatron = subelemento.attrib['codigo'].replace("\n","")
                cadenapatron = subelemento.text.replace(" ","").replace("\n","")
                nuevo_patron =str(cadenapatron)
                nuevo_codigo = str(nombrepatron)
                aux_contador = 0
                piso.coordenadas.insertar(nodoCoordenada(r,c,nuevo_codigo,-10,str(nombre)))
                for x in range(int(r)):
                    for y in range(int(c)):
                        patrontemp2 = nodoCoordenada(x,y,nuevo_patron[aux_contador],id,str(nombre))
                        piso.coordenadas.insertar(patrontemp2)
                        aux_contador += 1
                #print('termina el patron')
                piso.coordenadas.insertar(nodoCoordenada(-11,-11,nuevo_codigo,-11,str(nombre)))
                patrontemp = nodoDoblemente(nombrepatron,cadenapatron)
                piso.patrones.insertar(patrontemp)
            piso.coordenadas.recorrer()
            piso.coordenadas.graficar()
            print('termina el patron')
            piso.patrones.recorrer()
        
        print("Pisos ingresados")

        pisoss.mostrarpiso()
        
        




def procesararchivo():
    print("")
    print("---------- Procesar Piso ----------")
    print("")
   
    if pisoss.size == 0:
        print(" ¡ No hay pisos ingresados !")
        print("")
    else:
        print("---- Pisos Disponibles ----")
        for i in range (1, pisoss.size+1):
            print("- ", pisoss.getPiso(i).nombre)
        print("")
        print("Escriba el nombre del piso a procesar:")
        nombrePiso = input("- ")
        piso = pisoss.buscarPiso(nombrePiso)
        if piso is None:
            print("")
            print("¡Error!")
            print("El piso ingresado no existe")
            print("")
        else:
            print("Nombre elegido: ", nombrePiso)


def graficoarchivo():
    print("")
    print("---------- Graficar Piso ----------")
    print("")
   
    if pisoss.size == 0:
        print(" ¡ No hay pisos ingresados !")
        print("")
    else:
        print("---- Pisos Disponibles ----")
        for i in range (1, pisoss.size+1):
            print("- ", pisoss.getPiso(i).nombre)
        print("")
        print("Escriba el nombre del piso para generar grafica:")
        nombrePiso = input("- ")
        piso = pisoss.buscarPiso(nombrePiso)
        if piso is None:
            print("")
            print("¡Error!")
            print("El piso ingresado no existe")
            print("")
        else:
            grafo = graphviz.Graph()
            titulo = " ----- " + piso.nombre + " ----- \n" + str(piso.filas) + "x" + str(piso.columnas)
            grafo.attr(label=titulo,labelloc='t',fontsize='25', rankdir = 'LR')
            print("Nombre elegido para graficar: ", nombrePiso)
            print("")
            print("Creando el grafo...")
            print("")

            '''    aux_contador = 0
            aux_contador1 = 0
            empieza = "-44"
            termina = "-45"
            aux = self.raiz
            graph = "digraph G { \nrankdir = LR\n"
        
            while aux is not None:
            if str(aux.id) == empieza:
                graph+="subgraph "
                graph+="{}".format(aux.letra)
                graph+= "{ \n"
                aux_nombre = aux.letra
                aux_filas1 = int(aux.cna_x)
                aux_col1=int(aux.cna_y)
                aux = aux.siguiente
                
            aux_contador1+=1
            if aux.letra == "B" or aux.letra == "W":
                if aux.letra == "B":
                    nombrecolor = "black"
                    colorletra = "white"
                elif aux.letra == "W":
                    nombrecolor = "white"
                    colorletra ="black"
                #for i in range(aux.id):
                
                #    if aux_contador< aux_col1:
                graph += '{}[label="{}",color = "black",fontcolor ="{}",fillcolor="{}",style="filled",shape="box"];\n'.format(aux_contador1,aux_contador1,colorletra,nombrecolor)
                        #f.write('valor' + str(contG) + '->valor' + str(contG + m) + ';\n')
                #    elif aux_contador >= aux_col1 and aux_contador <= (aux_col1 * aux_filas1)-1:
                 #       graph += '{}[label="{}",color = "black",fontcolor ="{}",fillcolor="{}",style="filled",shape="box"];\n'.format(aux_contador1,aux.letra,colorletra,nombrecolor)
                        #f.write(' valor' + str(contG) + '->valor' + str(contG + m) + ';\n')
               #     elif aux_contador == (aux_col1 * aux_filas1) - aux_col1:
                #        break

                    #contG = contG + 1
                    
                aux_contador+=1
                    #graph+='rankdir=UD\n'
                #graph += '{}<-{};\n'.format(aux.letra,aux.siguiente)
                aux=aux.siguiente
            
            if str(aux.id) == termina:
                graph+="}\n"
                aux = aux.siguiente 
            aux = self.raiz
            aux_contador2 = 1
            aux_contador3 = 0
            while aux is not None:
            if str(aux.id) == empieza:
                aux_filas2 = int(aux.cna_x)
                aux_col2=int(aux.cna_y)
                aux = aux.siguiente

            aux_contador3 +=1
            if aux.letra == "B" or aux.letra == "W":
                for i in range(aux_contador):
                    if(aux_contador2 == 1 or aux_contador2 == (aux_contador/2)+1):
                        graph += "\nsubgraph cluster_" + str(0 if i==0 else 1)+ "{\nlabel=\""+ ("Patron Inicial" if i==0 else "Patron Final")+ "\"\nrankdir=TB\n"

                    if(aux_contador2 == aux_contador/2):
                        graph += "\n}"
                    if aux_contador2%aux_col2 == 0:
                        aux_contador2+=1
                        continue
                    elif aux_contador2 < (aux_contador):
                        graph += '{}->{};\n'.format(aux_contador2,aux_contador2+1)
                        aux_contador2+=1
                graph += "\n}"    
                aux=aux.siguiente
            if str(aux.id) == termina:
                aux = aux.siguiente
            graph+="}"

            documentotxt="GraficaPisos"+str(aux_contador)+".txt"
            with open(documentotxt,'w') as grafica: '''
            
            #grafica.write(graph) 

            '''for i in range(1, piso.coordenadas.n+1):
                for j in range(1, piso.matrizpiso.c+1):
                    if i == piso.filas and j == piso.columnas:
                        grafo.node(str(i)+','+str(j), str(piso.matrizpiso.getNodo(i,j)), style='filled', fillcolor='#77FF06')
                    elif i == piso.filas and j == piso.columnas:
                        grafo.node(str(i)+','+str(j), str(piso.matrizpiso.getNodo(i,j)), style='filled', fillcolor='#FF6006')
                    else:
                        if piso.procesado is True:
                            nodoEnRuta = False
                            for k in range (1, pisoss.size +1):
                                coordenada = piso.coordenadas.getCoordenada(k)
                                if coordenada.r == i and coordenada.c == j:
                                    nodoEnRuta = True
                            if nodoEnRuta is True:
                                grafo.node(str(i)+','+str(j), str(piso.matrizpiso.getNodo(i,j)), style='filled', fillcolor='#B2B2B2')
                            else:
                                grafo.node(str(i)+','+str(j), str(piso.matrizpiso.getNodo(i,j)))
                        else:    
                            grafo.node(str(i)+','+str(j), str(piso.matrizpiso.getNodo(i,j)))

            for i in range(1, piso.matrizpiso.r+1):
                for j in range(1, piso.matrizpiso.c+1):
                    nodo = piso.matrizpiso.getNodo(i,j)
                    
                    if nodo.down is not None:
                        grafo.edge(str(nodo.fila) + ','+str(nodo.columna), str(nodo.down.fila) + ','+ str(nodo.down.columna), constraint='true')
                    if nodo.right is not None:
                        grafo.edge(str(nodo.fila) + ','+str(nodo.columna), str(nodo.right.fila) + ','+ str(nodo.right.columna), constraint='false')  '''
            

            print("Reenderizando el grafo a PDF...")
            print("")

            try:
                grafo.render(piso.nombre, view=True)
                print("Grafo reenderizado exitosamente")
                print("Guardado como: " ,piso.nombre, ".pdf\"")
            except:
                print("No se pudo reescribir el archivo PDF")


def grafica2():
    print("Prueba")
    piso.coordenadas.graficar()


def menu():
    opcion = ''
    while opcion != '5':
        print("------Menu principal------")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Generar grafica")
        print("5. Salida")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            Filename = input('Ingrese la ruta del archivo: ')
            file = Filename
            cargarArchivo(file)
        elif opcion == '2':
            procesararchivo()
        elif opcion == '3':
            print("Mostrar datos del estudiante" +"\n" )
        elif opcion == '4':
            graficoarchivo()
            #grafica2()
        elif opcion != "5":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      