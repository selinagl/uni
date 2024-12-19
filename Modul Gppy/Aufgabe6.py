"""Calculates a new attribute value with existing ones.
   author: Selina Glatzer
   date: 2024 Dec 19
"""

import arcpy
import os

# Path to gdb
path_dir = os.path.dirname(__file__)
path_gdb = os.path.join(path_dir, "Daten-20241209", "Salzburg.gdb")

# Set arcpy environment
arcpy.env.workspace = path_gdb


def verktypneu():
    """ This function requires the Geodatabase "Salzburg.gdb". Takes the values of the attributes "Typ1", "Typ2",
        "Typ3" and "Shape_Length" from the Feature Class "sbgbahn", and creates a new value for "Verk_Typ".
        Then prints the new values.
    """
    # Read gdb
    with arcpy.da.SearchCursor("sbgbahn", ['Typ1', 'Typ2', 'Typ3', 'Shape_Length' ]) as cursor:
        for row in cursor:
            # Check which "Typ"-attribute has values
            if not row[0] == "-":
                prefix = row[0]
            elif not row[1] == "-":
                prefix = row[1]
            elif not row[2] == "-":
                prefix = row[2]
            else:
                # If no "Typ" was found
                prefix = "NaN"

            # Round length
            number = round(row[3])
            if number < 50:
                number = 50
            if prefix == "NaN":
                # No number added if no "Typ" was found
                final_name = prefix
            else:
                # Construct final name: Typ_Length
                final_name = f"{prefix.upper()}_{number}"

            print(final_name)

# Run
print("New names for attribute 'Verk_Typ:")
verktypneu()


"""
-------------------------------------
Original function in Calculate Field:
--------------------------------------
Verktypneu(!Typ1!, !Typ2!, !Typ3!, !Shape_Length!)

def Verktypneu(t1, t2, t3, length):
    if not t1 == "-":
        prefix = t1
    elif not t2 == "-":
        prefix = t2
    elif not t3 == "-":
        prefix = t3
    else:
        prefix = "NaN"

    number = round(length)
    if number < 50:
        number = 50
    if prefix == "NaN":
        final_name = prefix
    else:
        final_name = f"{prefix.upper()}_{number}"
    return final_name"""