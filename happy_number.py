def is_happy_number(number):
    def process(num):
        result = 0
        pieces = list(str(num))
        for num in pieces:
            result += int(num) ** 2
        return result

    sequence = {}
    current = number
    while current not in sequence and current != 1:
        sequence[current] = True
        current = process(current)
    return current == 1


print(is_happy_number(19))
