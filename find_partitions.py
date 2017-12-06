def find_partitions(input_list):
    def create_range(begin, end):
        if end and begin != end:
            return str(begin) + '-' + str(end)
        else:
            return str(begin)

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
        if current == begin:
            results.append(create_range(begin, None))
        else:
            results.append(create_range(begin, current))

    return results
