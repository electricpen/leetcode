def is_palindrome(input_string):
    return input_string == input_string[::-1]


print(is_palindrome('racecar'))
