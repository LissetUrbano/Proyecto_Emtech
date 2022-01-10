# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:42:21 2022

@author: Lisset F. Urbano
"""

import pandas as pd #Libreria pandas 


dataframe = pd.read_csv('synergy_logistics_database.csv', index_col=0, encoding='utf-8',parse_dates=[4, 5]) #En esta columna definimos que el  indice pertenece la columna 0 / el encoding es para definir que nuestro archivo podria contener caracteres y el uft-8 que engloba mas caracteres  / pharse dates  estamos indicando que en esa seccion tenemos fechas y las debe procesar como tal

exports = dataframe[dataframe['direction'] == 'Exports']#Filtro de Exportaciones

imports = dataframe[dataframe['direction'] == 'Imports']#Filtro de importaciones 

#-----------------------------


combinaciones_rutas = dataframe.groupby(by=['origin', 'destination'])  #Se crea un dataframe de los datos con los que se desea hacer la iteracion 
descripcion = combinaciones_rutas.describe()['total_value']



print("---------LAS RUTAS MÁS DEMANDADAS--------\n")
print(descripcion)
print("")
print(sorted(descripcion))
print("\n")

#-------------------------------

print("--------ANALISIS GENERAL-----------")
combinaciones_transporte = dataframe.groupby(by=['transport_mode'])  #Se crea un dataframe de los datos con los que se desea hacer la iteracion 
                                               
medios_transporte = combinaciones_transporte.describe()['total_value']

print("")
print("---------LOS MEDIOS DE TRANSPORTE MÁS IMPORTANTES--------\n")
print(medios_transporte)
print("")

print(sorted(medios_transporte))



print("--------ANALISIS IMPORTACIONES-----------")

combinaciones_transporte_impor = imports.groupby(by=['transport_mode'])  #Se crea un dataframe de los datos con los que se desea hacer la iteracion 
                                               
medios_transporte_impor = combinaciones_transporte_impor.describe()['total_value']

print("")
print("---------LOS MEDIOS DE TRANSPORTE MÁS IMPORTANTES--------\n")
print(medios_transporte)
print("")

print(sorted(medios_transporte_impor))







print("--------ANALISIS EXPORTACIONES-----------")

combinaciones_transporte_expor = exports.groupby(by=['transport_mode'])  #Se crea un dataframe de los datos con los que se desea hacer la iteracion 
                                               
medios_transporte_expor = combinaciones_transporte_expor.describe()['total_value']

print("")
print("---------LOS MEDIOS DE TRANSPORTE MÁS IMPORTANTES--------\n")
print(medios_transporte)
print("")

print(sorted(medios_transporte_expor))





#------------------------------------------



print("--------------VALOR TOTAL DE LAS IMPORTACIONES Y EXPORTACIONES---------")
def sol_3(df, p):
    pais_total_value = df.groupby('origin').sum()['total_value'].reset_index()
    total_value_for_percent = pais_total_value['total_value'].sum()
    pais_total_value['percent'] = 100 * pais_total_value['total_value'] / total_value_for_percent
    pais_total_value.sort_values(by='percent', ascending=False, inplace=True)
    pais_total_value['cumsum'] = pais_total_value['percent'].cumsum()
    lista_pequena = pais_total_value[pais_total_value['cumsum'] < p]
    
    return lista_pequena

res = sol_3(dataframe, 80)

print(res)
