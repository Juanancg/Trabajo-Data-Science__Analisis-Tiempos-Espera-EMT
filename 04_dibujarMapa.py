'''
    File name: 04_dibujarMapa.py
    Author: Juan Andres Corrochano
    Date created: 16/04/2019
    Date last modified: 17/04/2019
    Python Version: 3.6
    Description: Este script genera un .html con un mapa con la posicion de las 20 paradas con la
		 media de la diferencia de los tiempos de espera mas alta (en azul) y la posicion de 
		 los centroides (en rojo). Los dataset deben estar separados por "::" y estar 
		 presentados como LATITUD::LONGITUD
	 	 Basado en https://stackoverflow.com/questions/54455657/
	 	 	   how-can-i-plot-a-map-using-latitude-and-longitude-data-in-python-highlight-few
'''

# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------
import gpxpy
import gpxpy.gpx
import folium
import numpy as np

# --------------------------------------------------------------------------------------------------
# DEFINES
# --------------------------------------------------------------------------------------------------
DATASET_POINTS = 'top20Coordenadas.txt'
DATASET_CENTROIDES = 'centroides.txt'


# --------------------------------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------------------------------
# PUNTOS

points = list()

with open(DATASET_POINTS, 'rt') as reader:
    for point in reader:
        points.append(np.asarray([float(x) for x in point.split("::")]))

ave_lat = sum(p[0] for p in points)/len(points)
ave_lon = sum(p[1] for p in points)/len(points)

# Load map centred on average coordinates
my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=14)

#add a markers
for each in points:  
    folium.Marker(each).add_to(my_map)


# CENTROIDES

centroides = list()

with open(DATASET_CENTROIDES, 'rt') as reader:
    for point in reader:
        centroides.append(np.asarray([float(x) for x in point.split("::")]))

#add a markers
for each in centroides:  
    folium.Marker(each, icon=folium.Icon(color='red')).add_to(my_map)


# Save map
my_map.save("./gpx.html")

print("Finish!")
