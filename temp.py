def duplicate_items(list_numbers):
    repeater = {}
    repeats = []
    for num in list_numbers:
        if num in repeater:
            if num not in repeats:
                repeats.append(num)
        else:
            repeater[num] = True
    repeats.sort()
    return repeats


duplicate_items([1, 2, 3, 1])
