def max_gain(input_list):
    """
    iterate through the list, for each item
      iterate through the remaining items with index above the current item
        calculate the difference in values and compare to a tracking value
          if it is larger, replace tracking value with current value
    """
    largest = 0
    for index, first in enumerate(input_list):
        for second in input_list[index + 1:]:
            diff = second - first
            if diff > largest:
                largest = diff
    return largest


print(max_gain([10, 2, 3, 1]))
