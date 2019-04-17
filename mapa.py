import gpxpy
import gpxpy.gpx
import folium
import numpy as np

# PUNTOS

points = list()

with open('top20Coordenadas.txt', 'rt') as reader:
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

with open('centroides.txt', 'rt') as reader:
    for point in reader:
        centroides.append(np.asarray([float(x) for x in point.split("::")]))

ave_lat = sum(p[0] for p in centroides)/len(centroides)
ave_lon = sum(p[1] for p in centroides)/len(centroides)

#add a markers
for each in centroides:  
    folium.Marker(each, icon=folium.Icon(color='red')).add_to(my_map)


# Save map
my_map.save("./gpx.html")
