def is_power_of_four(number):
    if number not None and number > 3:
        while number > 0:
            number -= 4
        if number == 0:
            return True
        else:
            return False
