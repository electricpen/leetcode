import math


class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"


def find_range(input_list, input_number):
    if len(input_list) == 0:
        return None
    else:
        low = 0
        middle = len(input_list) // 2
        high = len(input_list) - 1
        while input_list[middle] != input_number and middle != low:
            if input_list[middle] > input_number:
                high = middle
                middle = (middle + low) // 2
            else:
                low = middle
                middle = math.ceil((high + middle) / 2)
        found_index = middle if input_list[middle] == input_number else -1
        if found_index != -1:
            low_range = found_index
            high_range = found_index
            while low_range > 0 and input_list[low_range] == input_number:
                low_range -= 1
            if input_list[low_range] != input_number:
                low_range += 1
            while high_range < len(input_list) - 1 and input_list[high_range] == input_number:
                high_range += 1
            if input_list[high_range] != input_number:
                high_range -= 1
            return [low_range, high_range]
        else:
            return None


print(find_range([], 1), 'should equal None')
print(find_range([1], 1), 'should equal [0,0]')
print(find_range([1, 1], 1), 'should equal [0,1]')
print(find_range([1, 2], 1), 'should equal [0,0]')
print(find_range([1, 2], 2), 'should equal [1,1]')
print(find_range([1, 1], 2), 'should equal None')
print(find_range([1, 1, 2], 1), 'should equal [0,1]')
print(find_range([1, 1, 1], 1), 'should equal [0,2]')
print(find_range([1, 1, 2], 2), 'should equal [2,2]')
print(find_range([1, 2, 2], 1), 'should equal [0,0]')
print(find_range([1, 1, 2], 3), 'should equal None')
print(find_range([1, 1, 2, 3], 2), 'should equal [2,2]')
print(find_range([1, 1, 1, 1], 1), 'should equal [0,3]')
print(find_range([1, 1, 1, 2], 2), 'should equal [3,3]')
print(find_range([1, 2, 2, 3], 2), 'should equal [1,2]')
print(find_range([1, 2, 2, 3], 1), 'should equal [0,0]')
print(find_range([1, 2, 2, 3], 3), 'should equal [3,3]')
