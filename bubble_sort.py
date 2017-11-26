def bubble_sort(a_list):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(a_list[:len(a_list) - 1])):
            number = a_list[index]
            next_number = a_list[index + 1]
            if number > next_number:
                a_list[index] = next_number
                a_list[index + 1] = number
                swapped = True


arr = [3, 2, 1]
bubble_sort(arr)
print('Expect [1,2,3]', arr)
