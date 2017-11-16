def duplicate_items(list_numbers):
    duplicates = {}
    results = set([])
    for number in list_numbers:
        if number in duplicates:
            results.add(number)
        else:
            duplicates[number] = 1
    return sorted(results)
