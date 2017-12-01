def make_palindrome(input):
    def is_palindrome(substr):
        return substr == substr[::-1]
    for index in range(len(input)):
        if is_palindrome(input[index:]):
            append = input[0:index][::-1]
            return input + append


print(make_palindrome('race'))


"""
interesting recursive solution:
def make_palindrome(input):
    if input == input[::-1]:
        return input
    else:
        return input[0] + make_palindrome(input[1:]) + input[0]
"""
