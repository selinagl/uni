import math

def calc_volumen(r, h):
    '''Berechnet das Volumen eines Zylinders.
    r = Radius
    h = Höhe'''
    vol = r**2 * math.pi * h
    return vol

print(calc_volumen.__doc__)

user_eingabe = False
while user_eingabe == False:
    try:
        user_r = float(input("Radius? "))
        user_h = float(input("Höhe? "))
        user_eingabe = True
    except ValueError:
        print("Keine Buchstaben. Komma mit '.', nicht ','.")

print(f"Das Volumen des Zylinders beträgt {calc_volumen(user_r, user_h):.3f} Kubikmeter.")


