"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import folium
import matplotlib.pyplot as plt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control,size):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    mt = controller.load_data(control,size)
    lista = control["lista_accidentes"]
    
    lista_pr = []
    frstelement = lt.getElement(lista,1)
    scndelement = lt.getElement(lista,2)
    thrdelement = lt.getElement(lista,3)
    thrdlast = lt.getElement(lista,((lt.size(lista))-2))
    scndlast = lt.getElement(lista,((lt.size(lista))-1))
    last = lt.getElement(lista,((lt.size(lista))))
    lista_pr.append(frstelement)
    lista_pr.append(scndelement)
    lista_pr.append(thrdelement)
    lista_pr.append(thrdlast)
    lista_pr.append(scndlast)
    lista_pr.append(last)
    headers = ["FECHA_OCURRENCIA","HORA_OCURRENCIA","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONIGTUD"]
    lista_tab = []
    lista_tab.append(headers)
    for item in lista_pr:
        tabulatelist2 = []
        tabulatelist2.append(item["FECHA_OCURRENCIA_ACC"])
        tabulatelist2.append(item["HORA_OCURRENCIA_ACC"])
        tabulatelist2.append(item["LOCALIDAD"])
        tabulatelist2.append(item["DIRECCION"])
        tabulatelist2.append(item["GRAVEDAD"])
        tabulatelist2.append(item["CLASE_ACC"])
        tabulatelist2.append(item["LATITUD"])
        tabulatelist2.append(item["LONGITUD"])
        lista_tab.append(tabulatelist2)
    print(str(mt) )   
    print(tabulate(lista_tab,headers="firstrow",tablefmt="fancy_grid"))
    
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,fecha_inicio,fecha_final):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    datos = controller.req_1(control,fecha_inicio,fecha_final)
    print(str(datos[1])+"/"+str(datos[2]))
    print("existen "+ str(datos[0][1]) + " accidentes entre las fechas dadas")
    print(tabulate(datos[0][0],headers = "firstrow", tablefmt="fancy_grid"))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control,gravedad,fecha_inicio,fecha_final):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    answer = controller.req_4(control,gravedad,fecha_inicio,fecha_final)
    tab = answer[0][1]
    tab = tab[0:6]
    print(str(answer[1])+"/"+str(answer[2]))
    print("Hay " + str(answer[0][0]) + " entre las fechas dadas")
    print(tabulate(tab,headers="firstrow",tablefmt="fancy_grid"))


def print_req_5(control, month, year, location):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    answer = controller.req_5(control, month, year, location)
    months = 0
    if month == "01":
        months = "Enero"
    elif month == "02":
        months = "Febrero"
    elif month == "03":
        months = "Marzo"
    elif month == "04":
        months = "Abril"
    elif month == "05":
        months = "Mayo"
    elif month == "06":
        months = "Junio"
    elif month == "07":
        months = "Julio"
    elif month == "08":
        months = "Agosto"
    elif month == "09":
        months = "Septiembre"
    elif month == "10":
        months = "Octubre"
    elif month == "11":
        months = "Noviembre"
    elif month == "12":
        months = "Diciembre"
        
    exit = ("Hay "+ str(answer[0][0]) + " accidentes ocurridos en la localidad de "+location+" en el mes de "+months+" del año "+year+".")
    print(str(answer[1])+"/"+str(answer[2]))
    print (exit)
    print(tabulate(answer[0][1],headers = "firstrow", tablefmt="fancy_grid"))


def print_req_6(control, month, year, latitude_coordenate, longitude_coordenate, radio_area, accidents_number):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    answer = controller.req_6(control, month, year, latitude_coordenate, longitude_coordenate, radio_area, accidents_number)
    months = 0
    if month == "01":
        months = "Enero"
    elif month == "02":
        months = "Febrero"
    elif month == "03":
        months = "Marzo"
    elif month == "04":
        months = "Abril"
    elif month == "05":
        months = "Mayo"
    elif month == "06":
        months = "Junio"
    elif month == "07":
        months = "Julio"
    elif month == "08":
        months = "Agosto"
    elif month == "09":
        months = "Septiembre"
    elif month == "10":
        months = "Octubre"
    elif month == "11":
        months = "Noviembre"
    elif month == "12":
        months = "Diciembre"
    exit = "Los " + str(accidents_number) + " accidentes más cercanos al punto (" + str(latitude_coordenate) + "," + str(longitude_coordenate) + ") dentro de un radio de " + str(radio_area) + " Km para el mes de " + months + " de " + str(year) + "."
    print(str(answer[1])+"/"+str(answer[2]))
    print (exit)
    print(tabulate(answer[0],headers = "firstrow", tablefmt="fancy_grid"))


def print_req_7(control,month,year,escala):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    data = controller.req_7(control,month,year,escala)
    print(str(data[1])+"/"+str(data[2]))
    headers = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
    tuplas_tab = data[0][0]
    horas = data[0][1][0]
    valores = data[0][1][1]
    
    for tupla in tuplas_tab:
        lista_tab2 =[]
        lista_tab = []
        lista_tab2.append(headers)
        temprano = tupla[0]
        tarde = tupla[1]
        lista_tab.append(temprano["CODIGO_ACCIDENTE"])
        lista_tab.append(temprano["FECHA_HORA_ACC"])
        lista_tab.append(temprano["DIA_OCURRENCIA_ACC"])
        lista_tab.append(temprano["LOCALIDAD"])
        lista_tab.append(temprano["DIRECCION"])
        lista_tab.append(temprano["GRAVEDAD"])
        lista_tab.append(temprano["CLASE_ACC"])
        lista_tab.append(temprano["LATITUD"])
        lista_tab.append(temprano["LONGITUD"])
        lista_tab2.append(lista_tab)
        lista_tab = []
        lista_tab.append(tarde["CODIGO_ACCIDENTE"])
        lista_tab.append(tarde["FECHA_HORA_ACC"])
        lista_tab.append(tarde["DIA_OCURRENCIA_ACC"])
        lista_tab.append(tarde["LOCALIDAD"])
        lista_tab.append(tarde["DIRECCION"])
        lista_tab.append(tarde["GRAVEDAD"])
        lista_tab.append(tarde["CLASE_ACC"])
        lista_tab.append(tarde["LATITUD"])
        lista_tab.append(tarde["LONGITUD"])
        lista_tab2.append(lista_tab)
        print(tabulate(lista_tab2,headers="firstrow",tablefmt="fancy_grid"))
    plt.bar(horas,valores) 
    plt.xticks(rotation ="vertical")
    plt.show()   

def print_req_8(control,fecha_inicio,fecha_final,clase):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    datos = controller.req_8(control,fecha_inicio,fecha_final,clase)
    print(str(datos[1])+"/"+str(datos[2]))
    print("hay " + str(datos[0][0]) + " accidentes entre las fechas dadas")
    mapa = datos[0][1]
    mapa.show_in_browser()


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                size = input("Con que tamaño de archivo desea cargar los datos?")
                print("Cargando información de los archivos ....\n")
                data = load_data(control,size)
            elif int(inputs) == 2:
                fecha_inicio = input("Cual es la fecha de inicio (YYYY/MM/D)")
                fecha_final = input("Cual es la fecha final (YYYY/MM/D)")
                print_req_1(control,fecha_inicio,fecha_final)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                fecha_inicio = input("Cual es la fecha de inicio (YYYY/MM/D)")
                fecha_final = input("Cual es la fecha final (YYYY/MM/D)")
                gravedad = input("Cual es la gravedad de los accidentes que desea buscar")
                print_req_4(control,gravedad,fecha_inicio,fecha_final)

            elif int(inputs) == 6:
                month = input("Cual es el mes en el que desea buscar: ")
                year = input ("Cual es el año en el que desea buscar: ")
                location = input("Cual es la locación en la que desea buscar: ")
                print_req_5(control, month, year, location)

            elif int(inputs) == 7:
                month = str(input("Escriba el mes del cual quiere indigar los accidentes ocurridos (Ejemplo: Enero: 01): "))
                year = str(input("Escriba el año del cual quiere indigar los accidentes ocurridos: "))
                latitude_coordenate = float(input("Escriba la latitud del centro del área: "))
                longitude_coordenate = float(input("Escriba la longitud del centro del área: "))
                radio_area = float(input("Escriba el radio del área en Km: " ))
                accidents_number = int(input("Escriba el número de accidentes que desea observar: "))
                print_req_6(control, month, year, latitude_coordenate, longitude_coordenate, radio_area, accidents_number)

            elif int(inputs) == 8:
                month = input("Para que mes desea consultar")
                year = input("para que año desea consultar")
                escala = input("con que escala desea la grafica")
                print_req_7(control,month,year,escala)

            elif int(inputs) == 9:
                fecha_inicio = input("Cual es la fecha de inicio para la que que quiere visualizar los accidentes: ")
                fecha_final = input("Cual es la fecha final para la que que quiere visualizar los accidentes:")
                clase = input("Que clase de accidentes desea ver: ")
                print_req_8(control,fecha_inicio,fecha_final,clase)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)