# Python-Version: Python 3.9

import math

def calc_volumen(r, h):
    """Berechnet das Volumen eines Zylinders.
    Eingabe soll in Metern erfolgen.
    ---------
    Parameter:
    r = Radius des Zylinders
    h = Höhe des Zylinders
    --------
    returns:
    Ergebnis der Volumensberechnung als Float"""
    volume = r**2 * math.pi * h
    return volume

print(calc_volumen.__doc__)

#Benutzer wird nach Höhe und Radius gefragt.
#Erfolgt eine falsche Eingabe (zb. string), kann sie wiederholt werden.
user_input = False
while user_input == False:
    try:
        user_r = float(input("Radius? "))
        user_h = float(input("Höhe? "))
        user_input = True
    except ValueError:
        print("Keine Buchstaben eingeben. Komma mit '.', nicht ','.")

#Ergebnis ausgeben. Für Codierung von Kubikmetern wird Unicode verwendet.
print(f"Das Volumen des Zylinders beträgt {calc_volumen(user_r, user_h):.3f} m\u00b3.")


