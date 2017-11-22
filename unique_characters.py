def unique_chars_in_string(input_string):
    tracker = {}
    for letter in input_string:
        if letter in tracker:
            return False
        else:
            tracker[letter] = True
    return True


print(unique_chars_in_string('hello'))
