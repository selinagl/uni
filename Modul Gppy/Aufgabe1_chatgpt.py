# Python-Version: 3.9

""" Dieses Skript wurde von ChatGPT generiert.
    Prompt:
    ich brauche ein python skript, das die orthodrome zwischen einem bestimmten ort (Hohenfestung Salzburg)
    und einem beliebigen ort berechnet. der beliebige ort wird vom benutzer abgefragt,
    der längen und breitengrad angeben soll. die abfrage soll überpüft werden
    (benutzer darf nur eine floating point number eingeben, breitengrad soll zwischen -90 und 90 sein,
    längengrad zwischen -180 und 180)."""


import math

def is_valid_latitude(lat):
    return -90 <= lat <= 90


def is_valid_longitude(lon):
    return -180 <= lon <= 180


def get_coordinate_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Bitte geben Sie eine gültige Gleitkommazahl ein.")


def haversine_distance(lat1, lon1, lat2, lon2):
    # Erdradius in Kilometern
    R = 6371.0
    # Koordinaten in Bogenmaß umrechnen
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine-Formel
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distanz berechnen
    distance = R * c
    return distance


def main():
    # Koordinaten der Hohensalzburg
    hohensalzburg_lat = 47.7952
    hohensalzburg_lon = 13.0478

    print("Berechnung der Orthodrome von der Hohensalzburg (Salzburg) zu einem beliebigen Ort.")

    # Benutzerkoordinaten abfragen und validieren
    while True:
        user_lat = get_coordinate_input("Bitte geben Sie die Breite (Latitude) des Ziels ein (-90 bis 90): ")
        if is_valid_latitude(user_lat):
            break
        print("Ungültige Eingabe. Die Breite muss zwischen -90 und 90 liegen.")

    while True:
        user_lon = get_coordinate_input("Bitte geben Sie die Länge (Longitude) des Ziels ein (-180 bis 180): ")
        if is_valid_longitude(user_lon):
            break
        print("Ungültige Eingabe. Die Länge muss zwischen -180 und 180 liegen.")

    # Distanz berechnen
    distance = haversine_distance(hohensalzburg_lat, hohensalzburg_lon, user_lat, user_lon)

    print(f"Die Orthodrome zwischen der Hohensalzburg und dem angegebenen Ort beträgt: {distance:.2f} km")


if __name__ == "__main__":
    main()
