def match(first, second):
    pointer1, pointer2 = 0, 0
    while pointer1 < len(first) and pointer2 < len(second):
        if first[pointer1] == '*':
            pointer1 += 1
            while second[pointer2] != first[pointer1] and pointer2 < len(second):
                pointer2 += 1
            if pointer2 == len(second):
                return False
        elif first[pointer1] != second[pointer2] and first[pointer1] != '?':
            return False
        pointer1 += 1
        pointer2 += 1

    return pointer1 == len(first) and pointer2 == len(second)
