def is_power_of_four(number):
    while number > 0:
        number -= 4
    if number == 0:
        return True
    else:
        return False
