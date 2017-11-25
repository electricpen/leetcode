def merge_ranges(input_range_list):
    index = 0
    item = input_range_list[0]
    next_item = input_range_list[1]
    while index < len(input_range_list) - 1:
        if item.upper_bound >= next_item.lower_bound:
            if item.upper_bound < next_item.upper_bound:
                item.upper_bound = next_item.upper_bound
            input_range_list.pop(index + 1)
            next_item = input_range_list[index + 1]
        else:
            index += 1
            item = next_item
            next_item = input_range_list[index + 1]
    return input_range_list
