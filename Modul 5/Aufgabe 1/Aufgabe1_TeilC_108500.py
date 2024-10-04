"1 m = 3.2808 ft und 1 m = 39.37 in"
def convert_height(metric):
    number_str = ""
    unit = ""
    for x in metric:
        if x.isalpha():
            unit += x
        else:
            number_str += x
    if unit == "cm" or unit == "":
        number = float(number_str)/100
        unit = "cm"
    else:
        number = float(number_str)
    feet = (number * 3.2808)
    inch = (feet % 1) * (39.37/3.2808)

    height_imperial = f"{(feet//1):.0f}'{inch:.0f}\""

    if not unit == "cm" or  unit == "m" or unit == "":
        print("Warning: Invalid input for unit.")
        # funktioniert nicht, wird 3x ausgegeben
    return number_str.strip(), unit, height_imperial

user_height = input("Height? ")

print(f"{convert_height(user_height)[0]} {convert_height(user_height)[1]} = {convert_height(user_height)[2]}")