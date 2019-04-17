# --------------------------------------------------------------------------------------------------
# DEFINES:
# --------------------------------------------------------------------------------------------------
POSITION_ID_PARADA = 0 # Posicion dentro de la lista del ID de la parada
POSITION_MEDIA = 5 # Posicion dentro de la lista de la media de los tiempos de espera


# --------------------------------------------------------------------------------------------------
# IMPORTS:
# --------------------------------------------------------------------------------------------------
import pyproj


# --------------------------------------------------------------------------------------------------
# FUNCIONES:
# --------------------------------------------------------------------------------------------------

# Devuelve el segundo elemento de una lista
def takeSecond(elem):
        if(len(elem)>1):
                return elem[1]
        else:
                return 0

# Pasa las coordenadas UTM huso horario 30 a LONGITUD y LATITUD
def coordenadasUTMaLongLat(varX, varY):
        ## Creamos el primer sistema de coordenadas en WGS84
        ## epsg:4326, http://spatialreference.org/ref/epsg/4326/
        p1 = pyproj.Proj(init = "epsg:4326")

        ## Creamos el segundo sistema de coordenadas en ED50 UTM huso horario 30
        ## epsg:23030, http://spatialreference.org/ref/epsg/23030/
        p2 = pyproj.Proj(init = "epsg:23030")

        return pyproj.transform(p2, p1, varX, varY)


# --------------------------------------------------------------------------------------------------
# LECTURA FICHEROS:
# --------------------------------------------------------------------------------------------------

# Lectura de fichero de datos de Tiempos de Espera
dataTiemposEspera = []
with open("EMT_tiempos_espera.txt") as file:
        for lines in file:
                 dataTiemposEspera.append(lines.split('\t'))


# Lectura de fichero de datos de Coordenadas Paradas
dataCoordenadas = []
with open("EMT_coordenadas_paradas.txt") as file:
        for lines in file:
                dataCoordenadas.append(lines.split('\t'))


# --------------------------------------------------------------------------------------------------
# MAIN:
# --------------------------------------------------------------------------------------------------

# Bucle que calcula la media para cada parada


counterFila = 1
idParadaAndMedia = []

while counterFila < len(dataTiemposEspera):

        counterSameID = 0
        sumaDiferenciasEsperas = int(dataTiemposEspera[counterFila - 1][POSITION_MEDIA])

        # Bucle que suma todas las diferencias (Evitando un out of index)
        while ((counterSameID + counterFila) < len(dataTiemposEspera)) and (dataTiemposEspera[counterSameID + counterFila - 1][POSITION_ID_PARADA] == dataTiemposEspera[counterSameID+ counterFila][POSITION_ID_PARADA]):

                sumaDiferenciasEsperas = sumaDiferenciasEsperas + int(dataTiemposEspera[counterSameID + counterFila][POSITION_MEDIA])
                counterSameID = counterSameID + 1

        # Juntar a una lista idParada  Media
        idParadaAndMedia.append([dataTiemposEspera[counterFila][POSITION_ID_PARADA], float(sumaDiferenciasEsperas)/float(counterSameID+1)])
        counterFila = counterFila + counterSameID + 1
# Ordenar los elementos por media descendente
sortedListByMean = sorted(idParadaAndMedia, key = takeSecond, reverse = True)

# Coger las 20 paradas con la media de espera mas alta
top20ParadasUnpunctual = sortedListByMean[:20]

# Unir las coordenadas X e Y a la parada
# Abre archivo para escribir
with open("top20Coordenadas.txt","w") as f:

        for top20 in top20ParadasUnpunctual:
                for parada in dataCoordenadas:
                        # Si coinciden los id de las paradas
                        if (parada[POSITION_ID_PARADA] == top20[POSITION_ID_PARADA]):

                                # Pasar las coordenadas UTM a longitud y latitud
                                long, lat = coordenadasUTMaLongLat(parada[1], parada[2])

                                # Une al final de la lista las coordenadas X e Y separadas por un espacio
                                top20 = top20 + [str(lat) + "::" + str(long)]

                print (top20)

                #Escribe las coordenadas
                f.write(top20[2] + '\n')


