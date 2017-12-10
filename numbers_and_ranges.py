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

    def binary_search(sorted_list, target):
        midpoint = len(sorted_list) // 2
        if target == sorted_list[midpoint]:
            return midpoint
        elif len(sorted_list) < 1:
            return -1
        elif target > sorted_list[midpoint]:
            return midpoint + binary_search(sorted_list[midpoint:], target)
        elif target < sorted_list[midpoint]:
            return binary_search(sorted_list[:midpoint], target)

    def seek_left(input_list, index):
        pos = index
        while pos > 0 and input_list[index] == input_list[pos - 1]:
            pos -= 1
        return pos

    def seek_right(input_list, index):
        pos = index
        while pos < len(input_list) - 1 and input_list[index] == input_list[pos + 1]:
            pos += 1
        return pos

    target_index = binary_search(input_list, input_number)
    if target_index > -1:
        begin = seek_left(input_list, target_index)
        end = seek_right(input_list, target_index)
    else:
        return None
    return Range(begin, end)


print(find_range([1, 2, 5, 5, 8, 8, 10], 8))
