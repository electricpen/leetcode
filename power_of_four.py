def is_power_of_four(number):
    compare = 1
    while compare < number:
        temp = compare
        for index in range(3):
            compare += temp
    return compare == number


print(is_power_of_four(12))

"""
My naieve solution works. The below solution is the suggested one which uses bitwise to get a multiplied value.
def is_power_of_four(number):
    test = 1
    while test < number:
        test = test << 2
    return test == number
"""
