def make_palindrome(input):
    def is_palindrome(substr):
        return substr == substr[::-1]
    for index in range(len(input)):
        """
        make a slice of input = last len-index chars
        check to see if it is a palindrome
        if it is, return input + first index chars reversed concat onto input
        """
        if is_palindrome(input[index:]):
            append = input[0:index][::-1]
            return input + append


print(make_palindrome('ab'))
