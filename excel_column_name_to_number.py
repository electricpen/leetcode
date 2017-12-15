def excel_column_name_to_number(column_title):
    total = 0
    for index in range(len(column_title)):
        total *= 26
        total += ord(column_title[index]) - (ord('A') - 1)
    return total


print(excel_column_name_to_number('ABC'))
