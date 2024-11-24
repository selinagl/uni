# Python-Version: Python 3.9

import shapely

# Polygon wird aus dem WKT ausgelesen
polygon1 = shapely.from_wkt("POLYGON ((4.2 0, 1.3 4, -3.4 2.47, -3.4 -2.47, 1.3 -4, 4.2 0))")
polygon2 = shapely.from_wkt("POLYGON ((46.2 0, 43.3 4, 38.6 2.47, 38.6 -2.47, 43.3 -4, 46.2 0))")

# Schwerpunkt des Polygons wird ausgegeben
centroid1 = polygon1.centroid
centroid2 = polygon2.centroid

# Abstand zwischen Polygon-Schwerpunkten berechnet
length_distance = centroid1.distance(centroid2)

print(f"{length_distance:.2f}")
