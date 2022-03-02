import xml.etree.ElementTree as ET

from Piso import Piso
from ListaSimple import listasimple as listapisos

archivo = ''
contenido = ''
tree = ''
root = ''
pisos = ''
pisoss = listapisos()


def cargarArchivo(ruta):
    global root
    global tree
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        nombre = elemento.attrib['nombre']
        buscarPiso = pisoss.buscarPiso(nombre)
        if buscarPiso is None:
            r = int(elemento.find('R').text)
            c = int(elemento.find('C').text)
            f = int(elemento.find('F').text)
            s = int(elemento.find('S').text)
            fila = r
            pisoss.agregar(nombre,r,c,f,s)         
            piso = pisoss.buscarPiso(nombre)
            piso.matrizpiso.agregarCoordenada(fila,c)
            for subelemento in elemento:
                if subelemento.tag == "patron":
                    codigo = str(subelemento.attrib['codigo'])
                    patron = str(subelemento.text)
                    #pisoss.patrones.getpatron(codigo,patron)
                    #pisoss.agregar(codigo,patron)
        print("Pisos ingresados")

        pisoss.mostrarpiso()
        #pisoss.mostrarpatron()
        #pisoss.mostrarelementos()







def menu():
    opcion = ''
    #Lista_Pisos = listasimple()
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
            #print(Lista_Pisos.mostrarpiso())
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