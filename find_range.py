def find_range(input_list, input_number):
    tracker = {first: -1, last: -1}
    for index, num in enumerate(input_list):
        if num == input_number:
            if tracker.first == -1:
                tracker.first = index
            else:
                tracker.last = index
    results = Range(tracker.first, tracker.last)
