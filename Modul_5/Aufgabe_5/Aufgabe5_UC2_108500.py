# Python-Version: Python 3.9

import geopandas
from shapely import Point

# Vorgabe Punkt
point1 = "POINT (22.29345, 114.17208)"

# Vorgabe-String formatieren, teilen und x,y-Koordinate auslesen
point1 = point1.replace("(", "").replace(")", "").replace(",", "").split()
point_x = point1[2]
point_y = point1[1]

# Dictionary mit Tabelleninformationen erstellen
d = {"name": ["point1"], "geometry": [Point(point_x, point_y)]}

#Geodataframe erstellen
geodataframe = geopandas.GeoDataFrame(data=d, crs=4326)

# Koordinatenreferenzsystem ändern
geodataframe = geodataframe.to_crs(crs=2326)

print(geodataframe)
