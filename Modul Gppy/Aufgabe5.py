"""Move the X- and Y-Coordinates of all features in a dataset. Output number of features outside of Salzburg.
   Read height of lowest point.

   author: Selina Glatzer
   date: 2024 Dec 17
"""

import arcpy
import os

# Path to gdb
path_dir = os.path.dirname(__file__)
path_gdb = os.path.join(path_dir, "Salzburg.gdb")

# Set arcpy environment
arcpy.env.workspace = path_gdb
arcpy.env.overwriteOutput = 1

# Read input parameters
input_fc = arcpy.GetParameterAsText(0)
shift_x = float(arcpy.GetParameterAsText(1))
shift_y = float(arcpy.GetParameterAsText(2))

# Create variables
new_name = 'alpenv_huetten_modified'
spatial_ref = arcpy.Describe(input_fc).spatialReference
test_height = 5000
geom1 = arcpy.Geometry()
geom2 = arcpy.Geometry()
geom3 = arcpy.Geometry()

# Create new 3D feature class
new_fc = arcpy.CreateFeatureclass_management(out_path=arcpy.env.workspace, out_name=new_name, geometry_type="POINT",
                                             has_z="ENABLED", spatial_reference=spatial_ref)

insert_cur = arcpy.da.InsertCursor(new_fc, ['SHAPE@X', 'SHAPE@Y', 'SHAPE@Z'])

# Insert into new 3D feature class. Moves X and Y-Coordinates by a given number from the user.
# Z-Coordinate is attribute 'HOEHE' from input feature class
with arcpy.da.SearchCursor(input_fc, ['SHAPE@X', 'SHAPE@Y', 'HOEHE']) as cursor:
    for row in cursor:
        coord_x = row[0] + shift_x
        coord_y = row[1] + shift_y
        coord_z = row[2]
        insert_cur.insertRow([coord_x, coord_y, coord_z])
        if row[2] < test_height:
            test_height = row[2]

del insert_cur

# Output lowest point
arcpy.AddMessage(f"Lowest point: {test_height}m")

# Create lists for checking inside points
geomList1 = arcpy.CopyFeatures_management("sbggde", geom1)
geomList2 = arcpy.CopyFeatures_management(input_fc, geom2)
geomList3 = arcpy.CopyFeatures_management(new_name, geom2)

list_within_og = []
list_within_shift = []

# Checking for inside points
for poly in geomList1:
    for pt_og in geomList2:
        if pt_og.within(poly):
            list_within_og.append(pt_og)
    for pt_shift in geomList3:
        if pt_shift.within(poly):
            list_within_shift.append(pt_shift)

# Output number of features outside of Salzburg (All features - inside points)
arcpy.AddMessage(f"Original points outside of Salzburg: {len(geomList2) - len(list_within_og)}")
arcpy.AddMessage(f"Moved points outside of Salzburg: {len(geomList3) - len(list_within_shift)}")
