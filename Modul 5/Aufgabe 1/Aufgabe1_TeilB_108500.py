def sum_odd_numbers(list_numbers):
    """Input a list consisting of numbers.
    The odd numbers are summed."""
    sum_odd = 0
    for x in list_numbers:
        if x % 2 != 0:
            sum_odd += x
    return sum_odd

liste = [1, 5, 8, 58, 85, 805, 510, 24, 4, 16]

print(sum_odd_numbers.__doc__)
print(f"The sum of all odd numbers is {sum_odd_numbers(liste)}.")


