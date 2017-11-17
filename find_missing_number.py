def find_missing_number(list_numbers):
    """
    given a list from 1-10, find the missing number.
    """
    list_numbers.sort()
    if list_numbers[0] != 1:
        return 1
    for index, num in enumerate(list_numbers):
        if index < len(list_numbers) - 1:
            if list_numbers[index + 1] != num + 1:
                return num + 1
        else:
            return 10


print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""
Best solution:
  return sum(range(11)) - sum(list_numbers)
"""
