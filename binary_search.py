def binary_search(a_list, item):
    midpoint = len(a_list) // 2
    if len(a_list) == 0:
        return False
    if a_list[midpoint] == item:
        return True
    elif len(a_list) == 1:
        return False
    else:
        if a_list[midpoint] < item:
            return binary_search(a_list[midpoint + 1:], item)
        else:
            return binary_search(a_list[:midpoint], item)


print(binary_search([1, 2, 3, 4, 5], 10), 'should be false')
print(binary_search([1, 2, 3, 4, 5], 1), 'should be true')
print(binary_search([1, 2, 3, 4, 5], 3), 'should be true')
print(binary_search([1, 2, 3, 4, 5], 5), 'should be true')
print(binary_search([1, 2, 3, 4, 5], 2), 'should be true')
print(binary_search([1, 2, 3, 4, 5], 4), 'should be true')
print(binary_search([], 1), 'should be false')
print(binary_search([1], 1), 'should be true')
print(binary_search([1], 2), 'should be false')
