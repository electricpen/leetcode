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
        return -1
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
