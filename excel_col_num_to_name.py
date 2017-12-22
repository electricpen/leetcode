def excel_column_number_to_name(column_number):
    if column_number < 27:
        return str(column_number + 64)
    else:
        letter = str(column_number % 26) if column_number % 26 != 0 else str(26)
        return str(excel_column_number_to_name(column_number // 26)) + letter