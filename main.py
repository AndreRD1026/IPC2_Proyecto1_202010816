from re import L
import xml.etree.ElementTree as ET
from ListaPatrones import nodoDoble, nodoDoble

from Piso import Piso
from Patron import Patron
from ListaSimple import listasimple as listapisos
from coordenada import Lista_Coordenadas,nodoCoordenada
import graphviz
import time


archivo = ''
contenido = ''
tree = ''
root = ''
pisos = ''
pisoss = listapisos()
grafico = ''


def cargarArchivo(ruta):
    global root
    global tree
    global piso
    global grafico
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
                piso.coordenadas.insertar(nodoCoordenada(-11,-11,nuevo_codigo,-11,str(nombre)))
                patrontemp = nodoDoble(nombrepatron,cadenapatron)
                piso.patrones.insertar(patrontemp)
            piso.coordenadas.recorrer()
            time.sleep(0.5)
            print("Renderizando patron")
            piso.coordenadas.graficopatron()
            print("Patron creado")

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

            print("Reenderizando el grafo a PDF...")
            print("")

            try:
                grafo.render(piso.nombre, view=True)
                print("Grafo reenderizado exitosamente")
                print("Guardado como: " ,piso.nombre, ".pdf\"")
            except:
                print("No se pudo reescribir el archivo PDF")


def grafica2():
        print("")
        print("Renderizando patrones")
        print("")
        piso.coordenadas.graficopatron()


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
            print("Archivo de salida" +"\n" )
        elif opcion == '4':
            graficoarchivo()
            #grafica2()
        elif opcion != "5":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      