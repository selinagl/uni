# Python-Version: Python 3.9

def test_odd_numbers(number):
    """Testet eine Zahl, ob sie gerade oder ungerade ist.
    ----
    Parameter:
    number = Integer
    ----
    returns:
    odd = Boolean
    True → Zahl ist ungerade
    False → Zahl ist gerade"""

    if number % 2 == 0:
        odd = False
    else:
        odd = True
    return odd


# Liste mit geraden und ungeraden Zahlen
list_numbers = [1, 5, 8, 58, 85, 805, 510, 24, 4, 16]

# Iteriert durch die Liste mit Zahlen und addiert zu sum_odd, falls die Zahl ungerade ist.
sum_odd = 0
for x in list_numbers:
    if test_odd_numbers(x) is True:
        sum_odd += x

print(test_odd_numbers.__doc__)
print(f"Die Summe aller ungeraden Zahlen ist {sum_odd}.")
