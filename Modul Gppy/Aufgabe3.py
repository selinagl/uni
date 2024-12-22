"""Enter custom buffers around the rivers of Salzburg.
   author: Selina Glatzer
   date: 2024 Dec 11
"""

import arcpy
import os
from datetime import datetime


def set_environment(gdb):
    """ Configures the arcpy environment.

    :param gdb: Path to 'Salzbug.gdb'
    """
    arcpy.env.overwriteOutput = 1
    arcpy.env.workspace = gdb


def fcname_validator(prefix, custom_buffer):
    """Creates and validates the name for the new features class. The name consists
       of the prefix, date and costum_buffer.

    :param prefix: Name entered by the user of the script
    :param custom_buffer: Buffer distance entered by the user
    :return out_fcname: Validated name for the new user class
    """
    get_date = datetime.now().strftime("%Y%d%m")
    name_test = f"{prefix}_{get_date}_{custom_buffer}Meter"
    validated_name = arcpy.ValidateTableName(name_test)
    print("")
    print(f"Created name: {validated_name}")
    if arcpy.Exists(validated_name):
        out_fcname = arcpy.CreateUniqueName(validated_name)
        print(f"Changed to unique name:'{validated_name}' --> '{out_fcname}'\n")
    else:
        out_fcname = validated_name
    return out_fcname


def river_buffer(out_name, distance):
    """Creates the custom buffer around the Rivers of Salzburg.
       New features class is added to 'Salzburg.gdb'.

    :param out_name: Validated name
    :param distance: Buffer distance entered by the user
    """
    sbgFluesse = "sbg_fluesse"
    out_distance = f"{str(distance)} Meters"

    print(f"Buffering {out_distance} ...")
    arcpy.Buffer_analysis(in_features=sbgFluesse, out_feature_class=out_name,
                          buffer_distance_or_field=out_distance, line_side="FULL", line_end_type="ROUND",
                          dissolve_option="ALL", method="")


# Path to 'Salzburg.gdb'
path_dir = os.path.dirname(__file__)
path_gdb = os.path.join(path_dir, "Daten-20241209", "Salzburg.gdb")
# Configure arcpy environment
set_environment(path_gdb)

# User-Input: name
user_fcname = input("Enter a name for the new feature class: ")
print("")

# User-Input: buffer distances
list_buffer = []
print("You can enter your buffer distances in sequence. Enter 'quit' if you have entered all your buffers.")
while True:
    user_buffer = input("Enter the buffer distance: ")
    try:
        user_buffer = int(user_buffer)
        list_buffer.append(user_buffer)
    except ValueError:
        if user_buffer == "quit":
            break
        else:
            print("Error. Enter only integers or 'quit'.")

# Run
for buffer in list_buffer:
    fcname = fcname_validator(user_fcname, buffer)
    river_buffer(fcname, buffer)


