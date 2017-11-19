def better_fibonacci(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        first = 0
        second = 1
        current = first + second

        count = n - 2
        while n > 1:
            current = first + second
            first = second
            second = current
            n -= 1
        return current


print(better_fibonacci(5))

"""
ideal solution:

def better_fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x + y 
    return x
"""
