import os
import csv

# returns the path to the script
SCRIPT_PATH = os.path.dirname(__file__)  # note: no error in this line

CSV_FILE = f"{SCRIPT_PATH}/data/restaurants.csv"

def find_location(name):
    with open(CSV_FILE, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            if name == row.get("Name"):
                return row.get("Lat"), row.get("Lon")
    return None

location1 = find_location("Hotel Gasthaus Adler")
print(location1)  # location1 should be ('48.05', '7.93')

location2 = find_location(None)
print(location2)  # location2 should be None

location3 = find_location("Café Öbergska")
print(location3)  # location3 should be ('57.61', '11.79')