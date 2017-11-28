def rotate_matrix(matrix):
    n = len(matrix)
    start_index = 0
    end_index = n - 1

    def get_rotated_coords(start):
        new_coords = {'row': 0, 'col': 0}
        new_coords['row'] = start['col']
        new_coords['col'] = n - 1 - start['row']
        return new_coords

    def rotate(matrix, origin):
        last_val = matrix[origin['row']][origin['col']]
        start = origin
        target = None
        next_val = None
        while target != origin:
            target = get_rotated_coords(start)
            next_val = matrix[target['row']][target['col']]
            matrix[target['row']][target['col']] = last_val
            start = target
            last_val = next_val

    while start_index < end_index:
        for i in range(start_index, end_index):
            rotate(matrix, {'row': start_index, 'col': i})
        start_index += 1
        end_index -= 1


test = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate_matrix(test)
for row in test:
    print(row)
