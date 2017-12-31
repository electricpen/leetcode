def excel_column_name_to_number(column_title):
    if len(column_title) == 1:
        return ord(column_title) - 64
    else:
        return (26 * excel_column_name_to_number(column_title[0:-1])) + (ord(column_title[-1:]) - 64)


print(excel_column_name_to_number('BA'))
