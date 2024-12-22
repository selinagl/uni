"""Add a new field to a Feature Class or Layer.
    This script is operating a Script Tool in an ArcGIS-Toolbox.

   author: Selina Glatzer
   date: 2024 Dec 13
"""

# Execution

# Import system modules
import arcpy
import os

# Read Input Feature Class
inputFC = arcpy.GetParameterAsText(0)

# Read other input parameters
inputString = arcpy.GetParameterAsText(1)
fieldList = inputString.split(";")
fieldType = arcpy.GetParameterAsText(2)
fieldLength = arcpy.GetParameterAsText(3)

# Setup for checking existing field names
list_fieldTest = []
fieldTest = arcpy.ListFields(inputFC)
for test in fieldTest:
    list_fieldTest.append(test.name)

for fieldName in fieldList:
    # Validate new field name
    fieldName = arcpy.ValidateFieldName(fieldName, os.path.dirname(inputFC))
    # Checking for existing field names
    if fieldName in list_fieldTest:
        arcpy.AddWarning(f"Field '{fieldName}' already exists and will not be created.")
    else:
        # Create new field
        arcpy.AddField_management(inputFC, fieldName, fieldType, "", "", fieldLength)
        arcpy.AddMessage(f"Field created: {fieldName}")
    if fieldType == "TEXT":
        arcpy.management.CalculateField(inputFC, fieldName, "'no data'")
arcpy.AddMessage("Calculation completed.")

# Validation

def updateParameters(self):
    # Modify the values and properties of parameters before internal
    # validation is performed.

    if self.params[2].value == "TEXT":
        self.params[3].enabled = 1
    else:
        self.params[3].enabled = 0