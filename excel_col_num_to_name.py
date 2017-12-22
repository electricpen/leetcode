def excel_column_number_to_name(column_number):
    if column_number < 27:
        return chr(column_number + 64)
    else:
        letter = chr((column_number %
                      26) + 64) if column_number % 26 != 0 else chr(90)
        return excel_column_number_to_name((column_number - 1) // 26) + letter
