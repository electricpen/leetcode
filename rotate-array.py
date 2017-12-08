def rotate_left(list_numbers, k):
    offset = k % len(list_numbers)
    for i in range(offset):
        temp = list_numbers.pop(0)
        list_numbers.append(temp)
    return list_numbers


print(rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))

# [3, 4, 5, 6, 1, 8, 7, 2, 9]

# [3, 4, 5, 6, 7, 8, 9, 1, 2]
