def rotate_left(list_numbers, k):
    offset = k % len(list_numbers)
    for index in range(len(list_numbers)):
        swap_index = abs(index - offset)
        list_numbers[index], list_numbers[swap_index] = list_numbers[swap_index], list_numbers[index]
