def transpose_matrix(matrix):
    start = 0
    end = len(matrix)

    def swap(row, col):
        temp = matrix[col][row]
        matrix[col][row] = matrix[row][col]
        matrix[row][col] = temp

    while start < end:
        for index in range(start, end):
            swap(start, index)
        start += 1


test = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix(test)
for row in test:
    print(row)
