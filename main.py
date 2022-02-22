import xml.etree.ElementTree as ET

from Piso import Piso
from ListaSimple import listasimple

archivo = ''
contenido = ''
tree = ''
root = ''
pisos = ''

def cargarArchivo(ruta, pisos):
    global root
    global tree
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        print('Nombre',elemento.attrib['nombre'],'ha sido insertado.')
        pisos.crearpiso(elemento.attrib['nombre']) # inserta piso




def menu():
    opcion = ''
    Lista_Pisos = listasimple()
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
            cargarArchivo(file, Lista_Pisos)
            print(Lista_Pisos.mostrarpiso())
        elif opcion == '2':
            print("Procesar archivo" +"\n" )
            #print(Lista_Terrenos.getTerreno('terreno1'))
        elif opcion == '3':
            print("Mostrar datos del estudiante" +"\n" )
        elif opcion == '4':
            print("Generar grafica" +"\n" ) 
        elif opcion != "5":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      