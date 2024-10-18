# Python-Version: Python 3.9

def convert_height(metric):
    """Körpergröße in Meter oder Centimeter eingeben.
    Die Größe wird in Feet und Inch ausgegeben.
    Eingabe-Beispiel: 1.75 m oder 175 cm
    Ist keine Einheit angegeben, wird von Centimeter ausgegangen.
    ---
    Parameter:
    metric = Eingegebene Körpergröße (cm, m)
    ---
    Rückgabewerte:
    number_str = Zahlenwert der eingegebenen Körpergröße als string
    unit = Eingegebene Einheit
    height_imperial = Umgewandelte Größe in Feet und Inch
    """

    number_str = ""
    unit = ""
    # Eingabe in Zahlenwert (1.75) und Einheit (m or cm) teilen
    for x in metric:
        if x.isalpha():
            unit += x
        else:
            number_str += x

    # cm in m umwandeln
    # keine Einheit: cm wird angenommen
    if unit == "cm" or unit == "":
        number = float(number_str) / 100
        unit = "cm"
    else:
        # string in float umwandeln
        number = float(number_str)

    # Metrisch zu Imperial umwandeln
    feet = (number * 3.2808)
    inch = (feet % 1) * (39.37 / 3.2808)

    # Formatierung des Ausgabe-strings (--> 5'9")
    height_imperial = f"{(feet // 1):.0f}'{inch:.0f}\""

    # Warnung, falls als Einheit nicht cm oder m angegeben wird
    if unit not in ["cm", "m"]:
        print("Warning: Invalid input: unit.")

    return number_str.strip(), unit, height_imperial


print(convert_height.__doc__)
# Eingabe der Größe
user_height = input("Größe? ")

height_result = convert_height(user_height)

print(f"{height_result[0]} {height_result[1]} = {height_result[2]}")
