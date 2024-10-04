"""


benötigte Module: math
Abfrage der Koordinaten inkl. Prüfroutine (korrekter Datentyp, Koordinaten innerhalb eines Bereich) --> while, try except
Variablen: lat_user, lon_user (Variablen für Longitude und Latitude des Benutzers
Hardcoded Koordinaten für Festung Hohensalzburg
Variablen: lat_slz, lon_slz
Funktion: Umwandlung in rad, Berechnen der Orthodrome
Variablen: distanz
print() Ergebnis mit f String

"""

import math

#Koordinaten: Festung Hohensalzburg [°]
lat_slz = 47.80
lon_slz = 13.05

#Koordinaten des Benutzers
user_eingabe = False
while user_eingabe is False:
    try:
        lat_user = float(input("Latitude? "))
        lon_user = float(input("Longitude? "))
        if -90 <= lat_user <= 90 and -180 <= lon_user <= 180:
            user_eingabe = True
        else:
            print("Eingabe ungültig. Lat: -90 -> +90. Lon: -180 -> +180")
    except ValueError:
        print("Eingabe ungültig. Nur Zahlen eingeben. Beispiel: 13.05")

def distanz_berechnen(lat, lon):
    # Koordinaten: Festung Hohensalzburg [°]
    lat_slz = math.radians(47.80)
    lon_slz = math.radians(13.05)

    #User_Koordinaten in Radians umwandeln
    lat = math.radians(lat)
    lon = math.radians(lon)

    #Orthodrome berechnen (in km)
    distanz = 6370 * math.acos(math.sin(lat_slz) * math.sin(lat) + math.cos(lat_slz) * math.cos(lat) * math.cos(lon - lon_slz))

    return distanz

print(f"Die Distanz beträgt {distanz_berechnen(lat_user, lon_user):.2f} km.")

