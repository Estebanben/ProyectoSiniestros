"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import folium
import datetime
import matplotlib.pyplot as plt
import math
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {}
    
    data_structs["fechas"] = om.newMap(omaptype="RBT")
    data_structs["lista_accidentes"] = lt.newList("ARRAY_LIST")
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["lista_accidentes"],data)
    fecha_acc = data["FECHA_OCURRENCIA_ACC"] 
    fecha_acc = datetime.datetime.strptime(fecha_acc,"%Y/%m/%d")
    entry = om.get(data_structs["fechas"],fecha_acc)
    
    
    if entry is None:
        datos = lt.newList("ARRAY_LIST")
        lt.addLast(datos,data)
        om.put(data_structs["fechas"],fecha_acc,datos)
    else:
        entry = entry["value"]
        lt.addLast(entry,data)
        om.put(data_structs["fechas"],fecha_acc,entry)
    
    return data_structs
        


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs,fecha_inicio,fecha_final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y/%m/%d")
    fecha_final = datetime.datetime.strptime(fecha_final,"%Y/%m/%d")
    x = 0
    lista_tab = []
    headers = ["(CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","(CLASE_ACC","LATITUD","LONGITUD"]
    lista_tab.append(headers)
    acci = om.values(data_structs["fechas"],fecha_inicio,fecha_final)
    lista_acci = lt.newList("ARRAY_LIST")
    for accidentes in lt.iterator(acci):
        
        x += len(accidentes["elements"])
        for info in accidentes["elements"]:
            lt.addLast(lista_acci,info)
    merg.sort(lista_acci,sortfechas)
    for accid in lista_acci["elements"]:
        lista = []
        lista.append(accid["CODIGO_ACCIDENTE"])
        lista.append(accid["FECHA_HORA_ACC"])
        lista.append(accid["DIA_OCURRENCIA_ACC"])
        lista.append(accid["LOCALIDAD"])
        lista.append(accid["DIRECCION"])
        lista.append(accid["GRAVEDAD"])
        lista.append(accid["CLASE_ACC"])
        lista.append(accid["LATITUD"])
        lista.append(accid["LONGITUD"])
        lista_tab.append(lista)
    return(lista_tab,x)

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass

def hash_gravedad(map,acci):
    value = mp.get(map,acci["GRAVEDAD"])
    gravedad = acci["GRAVEDAD"]
    if value is None:
        datos = lt.newList("ARRAY_LIST")
        lt.addLast(datos,acci)
        mp.put(map,gravedad,datos)
    else:
        value = value["value"]
        lt.addLast(value,acci)
        mp.put(map,gravedad,value)
    return map
def req_4(data_structs,gravedad,fecha_inicio,fecha_final):
    
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    mapa_g = mp.newMap(maptype="PROBING",numelements=8,loadfactor=0.5)
    fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y/%m/%d")
    fecha_final = datetime.datetime.strptime(fecha_final,"%Y/%m/%d")
    x = 0
    accidentes = lt.newList("ARRAY_LIST")
    
    data = om.values(data_structs["fechas"],fecha_inicio,fecha_final)
    for accidente in lt.iterator(data):
        for elemento in accidente["elements"]:
            x += 1
            hash_gravedad(mapa_g,elemento)
            
    accidentes = mp.get(mapa_g,gravedad)
    accidentes = accidentes["value"]
    quk.sort(accidentes,sortfechas)
    headers = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","CLASE_ACC","LATITUD","LONGITUD"]
    lista_tab = []
    lista_tab.append(headers)
    lista_tab2 = []
    for accidente in accidentes["elements"]:
        lista_tab2 = []
        lista_tab2.append(accidente["CODIGO_ACCIDENTE"])
        lista_tab2.append(accidente["FECHA_HORA_ACC"])
        lista_tab2.append(accidente["DIA_OCURRENCIA_ACC"])
        lista_tab2.append(accidente["LOCALIDAD"])
        lista_tab2.append(accidente["DIRECCION"])
        lista_tab2.append(accidente["CLASE_ACC"])
        lista_tab2.append(accidente["LATITUD"])
        lista_tab2.append(accidente["LONGITUD"])
        lista_tab.append(lista_tab2)
    return(lt.size(accidentes),lista_tab)
        
    
    
    

def req_5(data_structs, month, year, location):
    mapTree = data_structs["fechas"]
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "31"
    elif month == "04" or month == "06" or month == "09" or month == "11":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "30"
    elif month == "02":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "29"
    keylo = datetime.datetime.strptime(keylo,"%Y/%m/%d")
    keyhi = datetime.datetime.strptime(keyhi,"%Y/%m/%d")
    newMap = om.values(mapTree, keylo, keyhi)
    newList = lt.newList("ARRAY_LIST")
    for accidents in lt.iterator(newMap):
        for data in lt.iterator(accidents):
            if data["LOCALIDAD"] == location:
                lt.addLast(newList, data)
    sizeListValue = lt.size(newList)
    quk.sort(newList, sortfechas)
    inicial = int(sizeListValue-10)
    nicial = int(sizeListValue-10)
    if sizeListValue >= 10:
        finalList = lt.subList(newList, inicial, 10)
    else:
        finalList = newList
    headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
    tabList = []
    tabList.append(headers)
    for element in lt.iterator(finalList):
        tabList2 = []
        tabList2.append(element["CODIGO_ACCIDENTE"])
        tabList2.append(element["DIA_OCURRENCIA_ACC"])
        tabList2.append(element["DIRECCION"])
        tabList2.append(element["GRAVEDAD"])
        tabList2.append(element["CLASE_ACC"])
        tabList2.append(element["FECHA_HORA_ACC"])
        tabList2.append(element["LATITUD"])
        tabList2.append(element["LONGITUD"])
        tabList.append(tabList2)  
        
    return sizeListValue, tabList

def haversine_formula (first_latitude, second_latitude, first_longitude, second_longitude):
    latitude_1 = math.radians(first_latitude)
    latitude_2 = math.radians(second_latitude)
    longitud_1 = math.radians(first_longitude)
    longitud_2 = math.radians(second_longitude)
    
    latitudes = (math.sin(((latitude_2-latitude_1)/2)))**2
    longitudes = (math.sin(((longitud_2-longitud_1)/2)))**2
    latitude_11 = math.cos(latitude_1)
    latitude_22 = math.cos(latitude_2)
    root = math.sqrt(latitudes + (latitude_11 * latitude_22 * longitudes))
    distance = 2 * math.asin(root) * 6371
    return distance


def req_6(data_structs, month, year, latitude_coordenate, longitude_coordenate, radio_area, accidents_number):
    
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    mapTree = data_structs["fechas"]
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "31"
    elif month == "04" or month == "06" or month == "09" or month == "11":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "30"
    elif month == "02":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "29"
    keylo = datetime.datetime.strptime(keylo,"%Y/%m/%d")
    keyhi = datetime.datetime.strptime(keyhi,"%Y/%m/%d")
    newMap = om.values(mapTree, keylo, keyhi)
    newList = lt.newList("ARRAY_LIST")
    for fecha in lt.iterator(newMap):
        for data in lt.iterator(fecha):
            distance = haversine_formula(latitude_coordenate, float(data["LATITUD"]), longitude_coordenate, float(data["LONGITUD"]))
            data["distancia"] = distance
            if distance <= radio_area:
                lt.addLast(newList, data)
    quk.sort(newList, compareList)
    finalList = lt.subList(newList, 1, accidents_number)
    headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
    tabList = []
    tabList.append(headers)
    for element in lt.iterator(finalList):
        tabList2 = []
        tabList2.append(element["CODIGO_ACCIDENTE"])
        tabList2.append(element["DIA_OCURRENCIA_ACC"])
        tabList2.append(element["DIRECCION"])
        tabList2.append(element["GRAVEDAD"])
        tabList2.append(element["CLASE_ACC"])
        tabList2.append(element["FECHA_HORA_ACC"])
        tabList2.append(element["LATITUD"])
        tabList2.append(element["LONGITUD"])
        tabList.append(tabList2)  
    return tabList
    
            
def compareList(accidente1, accidente2):
    if accidente1["distancia"] < accidente2["distancia"]:
        return True
    else:
        return False
    
def haversine_formula (first_latitude, second_latitude, first_longitude, second_longitude):
    latitude_1 = math.radians(first_latitude)
    latitude_2 = math.radians(second_latitude)
    longitud_1 = math.radians(first_longitude)
    longitud_2 = math.radians(second_longitude)
    
    latitudes = (math.sin(((latitude_2-latitude_1)/2)))**2
    longitudes = (math.sin(((longitud_2-longitud_1)/2)))**2
    latitude_11 = math.cos(latitude_1)
    latitude_22 = math.cos(latitude_2)
    root = math.sqrt(latitudes + (latitude_11 * latitude_22 * longitudes))
    distance = 2 * math.asin(root) * 6371
    return distance


def req_7(data_structs,month,year,escala):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
     # TODO: Realizar el requerimiento 6
    mapTree = data_structs["fechas"]
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "31"
    elif month == "04" or month == "06" or month == "09" or month == "11":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "30"
    elif month == "02":
        keylo = year + "/" + month + "/" + "01"
        keyhi = year + "/" + month + "/" + "29"
        
        
    keylo = datetime.datetime.strptime(keylo, "%Y/%m/%d")
    keyhi = datetime.datetime.strptime(keyhi, "%Y/%m/%d")
        
    datos = om.values(mapTree,keylo,keyhi)
    lista_datos_tab = []
    lista_accidentes_totales = lt.newList("ARRAY_LIST")
    
    for dia in lt.iterator(datos):
        lista_datos_dia = lt.newList("ARRAY_LIST")
        for acci in dia["elements"]:
            lt.addLast(lista_datos_dia,acci)
            lt.addLast(lista_accidentes_totales,acci)
        quk.sort(lista_datos_dia,sorthoras)   
        if lt.size(lista_datos_dia) == 1:
            acci_tard =lt.getElement(lista_datos_dia,1)
            tupla_accis = (acci_tard,acci_tard)
            lista_datos_tab.append(tupla_accis)
        else:     
            acci_temp = lt.getElement(lista_datos_dia,lt.size(lista_datos_dia))
            acci_tard =lt.getElement(lista_datos_dia,1)
            tupla_accis = (acci_temp,acci_tard)
            lista_datos_tab.append(tupla_accis)
            
    plot_list_hours = ["0:00:00","1:00:00","2:00:00","3:00:00","4:00:00","5:00:00","6:00:00","7:00:00","8:00:00","9:00:00","10:00:00","11:00:00","12:00:00","13:00:00","14:00:00","15:00:00","16:00:00","17:00:00","18:00:00","19:00:00","20:00:00","21:00:00","22:00:00","23:00:00"]
    plot_list_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for accidente in lista_accidentes_totales["elements"]:
        hora_accidente = accidente["HORA_OCURRENCIA_ACC"]
        if datetime.datetime.strptime(hora_accidente,"%H:%M:%S").time() < datetime.datetime.strptime("10:00:00","%H:%M:%S").time():
            hora_accidente = hora_accidente[0:1]
        else:
            hora_accidente = hora_accidente[0:2]
        plot_list_values[int(hora_accidente)] += 1
        
    return (lista_datos_tab,[plot_list_hours,plot_list_values])
        
        
def req_8(data_structs,fecha_inicio,fecha_final,clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    fecha_inicio = datetime.datetime.strptime(fecha_inicio,"%Y/%m/%d")
    fecha_final = datetime.datetime.strptime(fecha_final,"%Y/%m/%d")
    info = om.values(data_structs["fechas"],fecha_inicio,fecha_final)
    map = folium.Map(location=[4.636057, -74.110094],zoom_start=14)
    x = 0
    for accidente in lt.iterator(info):
        for elemento in accidente["elements"]:
            if elemento["CLASE_ACC"] == clase:
                x+=1
                lat = elemento["LATITUD"]
                lon = elemento["LONGITUD"]
                color = ""
                tooltip = ""
                if elemento["GRAVEDAD"] == "SOLO DANOS":
                    color = "green"
                    tooltip = "Solo Daños"
                elif elemento["GRAVEDAD"] == "CON HERIDOS":
                    tooltip = "Con Heridos"
                    color = "blue"
                elif elemento["GRAVEDAD"] == "CON MUERTOS":
                    tooltip = "Con Muertos"
                    color = "red"
                folium.Marker([float(lat),float(lon)],icon=folium.Icon(color=color),tooltip=tooltip).add_to(map)
    
    return (x,map)
    
    
            
        


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def cmpfechas(data1,data2):
    return data1>data2

def sortfechas (data_1,data_2):
    fecha1 = datetime.datetime.strptime(data_1["FECHA_OCURRENCIA_ACC"],"%Y/%m/%d").date()
    fecha2 = datetime.datetime.strptime(data_2["FECHA_OCURRENCIA_ACC"],"%Y/%m/%d").date()
    hora1 = datetime.datetime.strptime(data_1["HORA_OCURRENCIA_ACC"],"%H:%M:%S").time()
    hora2 = datetime.datetime.strptime(data_2["HORA_OCURRENCIA_ACC"],"%H:%M:%S").time()
    if (fecha1 > fecha2):
        return True
    elif (fecha1<fecha2):
        return False
    else:
        if (hora1 > hora2):
            return True
        else:
            return False
        
def sorthoras(data1,data2):
    hora1 = datetime.datetime.strptime(data1["HORA_OCURRENCIA_ACC"],"%H:%M:%S").time()
    hora2 = datetime.datetime.strptime(data2["HORA_OCURRENCIA_ACC"],"%H:%M:%S").time()
    
    if hora1 > hora2:
        return True
    else:
        return False
    
def compareList(accidente1, accidente2):
    if accidente1["distancia"] < accidente2["distancia"]:
        return True
    else:
        return False