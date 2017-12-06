def find_partitions(input_list):
    results = []
    if input_list:
        current = input_list[0]
        begin = current
        end = -1
        prev = None
        for i in range(1, len(input_list)):
            prev = input_list[i - 1]
            current = input_list[i]
            if current - prev > 1:
                end = prev
                results.append(create_range(begin, end))
                begin = current

    return results
