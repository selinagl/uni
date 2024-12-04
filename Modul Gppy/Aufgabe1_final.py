# Python-Version: 3.9

import math

def distanz_berechnen(lat, lon):
    """ Berechnet eine Orthodrome zwischen Hohenfestung Salzburg und einem beliebigen Zielort.
        Die Koordinaten des Zielorts werden in Grad übergegeben.

    :param lat: Breite (Latitude) in Grad
    :param lon: Länge (Longitude) in Grad
    :return distanz: Orthodrome (Distanz) in km
    """
    # Koordinaten: Festung Hohensalzburg [°]
    lat_slz = 47.80
    lon_slz = 13.05

    # Koordinaten in Radians umwandeln
    lat, lon, lat_slz, lon_slz = map(math.radians, [lat, lon, lat_slz, lon_slz])

    # Orthodrome berechnen (in km)
    distanz = 6370 * math.acos(
        math.sin(lat_slz) * math.sin(lat) + math.cos(lat_slz) * math.cos(lat) * math.cos(lon - lon_slz))

    return distanz


# Koordinaten vom Benutzer abfragen und überprüfen
print("Berechnung der Orthodrome zwischen der Festung Hohensalzburg und einem beliebigen Zielort.")
user_eingabe = False
while user_eingabe is False:
    try:
        lat_user = float(input("Bitte geben Sie die Breitengrad (Latitude) des Zielorts ein (-90 bis 90): "))
        lon_user = float(input("Bitte geben Sie die Längengrad (Longitude) des Zielorts ein (-180 bis 180): "))
        if -90 <= lat_user <= 90 and -180 <= lon_user <= 180:
            user_eingabe = True
        else:
            print("Eingabe ungültig. Falscher Längen- oder Breitengrad.")
    except ValueError:
        print("Eingabe ungültig. Nur Zahlen eingeben. Beispiel: 13.05")

# Ergebnis ausgeben
print(f"Die Distanz beträgt {distanz_berechnen(lat_user, lon_user):.2f} km.")
