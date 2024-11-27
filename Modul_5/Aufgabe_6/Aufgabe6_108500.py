from geonames_geocoder import GeoNamesGeocoder
from nominatim_geocoder import NominatimGeocoder

# Dictionary zur Abfrage des Geocoding Service. Kann für weitere Services erweitert werden.
dict_geocoder = {1: "Geonames", 2: "Nominatim"}

# Benutzer-Abfrage nach dem gewünschten Geocoding Service.
print("Choose one of the Geocoding services available:")
for key, val in dict_geocoder.items():
    print(f"[{key}]: {val}")
user_service = int(input(f"Which geocoding service should be used? [Enter 1-{len(dict_geocoder)}]"))

# Klasse für den gewünschten Geocoding Service wird aufgerufen. Kann für weitere Services erweitert werden.
if user_service == 1:
    geocoder = GeoNamesGeocoder()
elif user_service == 2:
    geocoder = NominatimGeocoder()
else:
    print("Error: False number entered for the Geocoding Service.")

# User-Name wird abgefragt, wenn notwendig.
geocoder.configure()

# Ausgabe der Koordinaten zu beliebig vielen Ort. Schleife wird mit "quit" vom Benutzer beendet.
quit_option = True
while quit_option is True:
    user_location = input("Input location: ")
    if user_location == "quit":
        quit_option = False
    else:
        coordinates = geocoder.geocodeLocation(user_location)
        print(f"Result: {coordinates} Provided by: {geocoder.attribution}")