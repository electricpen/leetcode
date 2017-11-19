def insert_star_between_pairs(a_string):
    if a_string == None:
        return None
    elif len(a_string) == 1:
        return a_string
    if a_string[0] == a_string[1]:
        return a_string[0] + '*' + insert_star_between_pairs(a_string[1:])
    else:
        return a_string[0] + insert_star_between_pairs(a_string[1:])
