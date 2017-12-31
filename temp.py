def find_missing_number(list_numbers):
    return sum(list(range(1 - 11))) - sum(list_numbers)


print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))
