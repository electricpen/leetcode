def flip_vertical_axis(matrix):
    """
      offset for left side = index - 0
      offset for right side = length - index - 1
      new position for left = length - offset - 1
      new position for right = offset
    """
    def flip(rows):
        length = len(rows) - 1
        midpoint = length // 2
        temp = None
        for index in range(0, midpoint + 1):
            offset = index - 0
            right_pos = length - offset
            left_pos = offset
            temp = rows[right_pos]
            rows[right_pos] = rows[left_pos]
            rows[left_pos] = temp

    for rows in matrix:
        flip(rows)

    return matrix


TEST = flip_vertical_axis([[1, 0, 2, 4], [1, 3, 5, 7]])
print(TEST)


"""
  Optimal solutions:
  for rows in matrix:
    rows.reverse()
  
  for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
  
  built in methods for reversing
"""
