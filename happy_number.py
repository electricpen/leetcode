from functools import reduce


def is_happy_number(number, sequence={}):
    if number in sequence:
        return False
    digits = [int(d) for d in str(number)]
    next_num = reduce(lambda x, y: x * x + y * y, digits)
    sequence[number] = next_num
    if number == 1:
        return True
    else:
        return is_happy_number(next_num, sequence)


print(is_happy_number(100))
