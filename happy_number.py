def is_happy_number(number, sequence={}):
    if sequence[number]:
        return False
    digits = str(number).split('')
    next_num = reduce(lambda x, y: x * x + y * y, number)
    sequence[number] = next_num
    if number == 1:
        return True
    else:
        return is_happy_number(next_num, sequence)
